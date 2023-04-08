# Copyright (c) 2023, SARANESH A and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import add_months

class LibraryMembership(Document):
    def validate(self):
        if not self.to_date:
            lending_period = frappe.db.get_single_value("Library Management Setting", "lending_period")
            if not lending_period:
                frappe.throw("Please set the Lending Period in Library Management Setting.")
            else:
                self.to_date = add_months(self.from_date, lending_period)
                
    def on_submit(self):
        if not self.is_paid:
            frappe.throw("Payment Pending for Membership")

@frappe.whitelist()
def create_payment_entry(party, member_name):
    doc = frappe.new_doc("Payment Entry")
    doc.payment_type = "Receive"
    doc.mode_of_payment = "Cash"
    doc.party_type = "Visitor"
    doc.party = party
    doc.party_name = member_name
    amnt = frappe.db.get_single_value("Library Management Setting", "amount")
    if not amnt:
        frappe.throw("Please set the Membership Fee Amount in Library Management Setting.")
    else:
        doc.paid_amount = amnt
        doc.received_amount = amnt
    doc.source_exchange_rate = 1
    doc.flags.ignore_mandatory = True
    doc.save()
    return doc.name