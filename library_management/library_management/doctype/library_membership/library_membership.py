# Copyright (c) 2023, SARANESH A and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import add_months

class LibraryMembership(Document):
    def validate(self):
        if not self.to_date:
            lending_period = frappe.get_single_value("Library Management Setting", "lending_period")
            if not lending_period:
                frappe.throw("Please set the Lending Period in Library Management Setting / Lending Period cannot be 0.")
            else:
                self.to_date = add_months(self.from_date, lending_period)
                
    def on_submit(self):
        if not self.paid:
            frappe.throw("Payment Pending for Membership")