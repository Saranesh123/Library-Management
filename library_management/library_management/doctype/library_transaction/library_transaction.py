# Copyright (c) 2023, SARANESH A and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import today, date_diff

class LibraryTransaction(Document):
    def on_submit(self):
        qty = frappe.get_value("Article", self.article, "available_quantity")
        if self.status == "Issue":
            frappe.db.update("Article", self.article, "available_quantity", (qty - 1))
            if (qty - 1) == 0:
                frappe.db.update("Article", self.article, "status", "Inactive")
        else:
            frappe.db.update("Article", self.article, "available_quantity", (qty + 1))
            frappe.db.update("Article", self.article, "status", "Active")

        if self.penalty_amount and not self.is_paid:
            frappe.throw("Please Pay the Penalty Amount.")

    def validate(self):
        if frappe.db.exists(self.doctype, {"library_member": self.library_member, "article": self.article, "docstatus": 1}):
            last_doc = frappe.get_last_doc(self.doctype, {"library_member": self.library_member, "article": self.article, "docstatus": 1})
            if last_doc.status == "Issue" and self.status == "Issue":
                frappe.throw("Article - {0} was already Issued".format(frappe.bold(self.article)))
        else:
            if self.status == "Return":
                frappe.throw("Article - {0} is not Issued".format(frappe.bold(self.article)))

        if frappe.db.exists(self.doctype, {"article": self.article, "library_member":self.library_member, "status": "Issue", "docstatus": 1}):
            if self.status == "Return" and not self.has_membership:
                issued_doc = frappe.get_last_doc("Library Transaction", {"library_member": self.library_member, "status": "Issue"})
                doc = frappe.get_last_doc("Library Membership", {"library_member": self.library_member, "docstatus": 1})
                penalty = frappe.db.get_single_value("Library Management Setting", "penalty")
                if issued_doc.transaction_date != self.transaction_date:
                    if issued_doc.transaction_date >= doc.to_date:
                        self.penalty_amount = (abs(date_diff(issued_doc.transaction_date, self.transaction_date))) * penalty
                    else:
                        self.penalty_amount = (abs(date_diff(doc.to_date, self.transaction_date))) * penalty