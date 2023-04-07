# Copyright (c) 2023, SARANESH A and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import validate_email_address

class Visitor(Document):
    def validate(self):
        self.member_name = " ".join(
			filter(lambda x: x, [self.first_name, self.last_name])
		)
        
        validate_email_address(self.email, True)