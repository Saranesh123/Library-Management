# Copyright (c) 2023, SARANESH A and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import validate_email_address

class Visitor(Document):
    def validate(self):
        self.visitor_name = " ".join(
			filter(lambda x: x, [self.first_name, self.last_name])
		)
        
        validate_email_address(self.email, True)

        penalty = frappe.db.get_single_value("Library Management Setting", "penalty")
        lending = frappe.db.get_single_value("Library Management Setting", "lending")

        if not penalty:
            frappe.throw("Please set the Penalty Amount in Library Management Setting.")
        if not lending:
            frappe.throw("Please set the Lending Period for Non-Membership in Library Management Setting.")