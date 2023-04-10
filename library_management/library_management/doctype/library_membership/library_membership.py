# Copyright (c) 2023, SARANESH A and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import add_months, today, add_days
from frappe.utils.background_jobs import enqueue

class LibraryMembership(Document):
    def validate(self):
        if not self.to_date:
            lending_period = frappe.db.get_single_value("Library Management Setting", "lending_period")
            if not lending_period:
                frappe.throw("Please set the Lending Period in Library Management Setting.")
            else:
                self.to_date = add_months(self.from_date, lending_period)

        if frappe.db.exists("Library Membership", {"library_member": self.library_member, "to_date": [">=", self.from_date], "docstatus": 1}):
            frappe.throw("Already an Active Membership available for the Member - {0}".format(frappe.bold(self.library_member)))
                
    def on_submit(self):
        if not self.is_paid:
            frappe.throw("Payment Pending for Membership")
        frappe.db.update("Visitor", self.library_member, "has_membership", 1)

@frappe.whitelist()
def create_payment_entry(party, member_name, doc_name, doctype, remarks):
    doc = frappe.new_doc("Payment Entry")
    doc.reference_name = doc_name
    doc.reference_doctype = doctype
    doc.payment_type = "Receive"
    doc.mode_of_payment = "Cash"
    doc.party_type = "Visitor"
    doc.party = party
    doc.party_name = member_name
    if doctype == "Library Membership":
        amnt = frappe.db.get_single_value("Library Management Setting", "amount")
        if not amnt:
            frappe.throw("Please set the Membership Fee Amount in Library Management Setting.")
    else:
        amnt = frappe.get_value("Library Transaction", doc_name, "penalty_amount")
    doc.paid_amount = amnt
    doc.received_amount = amnt
    doc.custom_remarks = remarks
    doc.source_exchange_rate = 1
    doc.target_exchange_rate = 1
    doc.flags.ignore_mandatory = True
    doc.save()
    return doc.name

def validate_membership_daily_job():
    enqueue("library_management.library_management.doctype.library_membership.library_membership.validate_membership_daily", timeout=14400, queue="long")

@frappe.whitelist()
def validate_membership_daily():
    membership_list = frappe.get_all("Library Membership", {"to_date": add_days(today(), -1), "docstatus": 1}, ["library_member"])
    for member in membership_list:
        frappe.db.update("Visitor", member["library_member"], "has_membership", 0)

@frappe.whitelist()
def submit_library_membership(doc_name, doctype):
    doc = frappe.get_doc(doctype, doc_name)
    doc.save()
    doc.submit()