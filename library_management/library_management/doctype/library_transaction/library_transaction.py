# Copyright (c) 2023, SARANESH A and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class LibraryTransaction(Document):
    def on_submit(self):
        qty = frappe.get_value("Article", self.article, "available_quantity")
        frappe.db.update("Article", self.article, "available_quantity", (qty - 1))