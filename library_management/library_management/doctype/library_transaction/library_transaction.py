# Copyright (c) 2023, SARANESH A and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class LibraryTransaction(Document):
    def on_submit(self):
        qty = frappe.get_value("Article", self.article, "quantity")
        if self.status == "Issue":
            frappe.db.update("Article", self.article, "quantity", (qty - 1))
            if (qty - 1) == 0:
                frappe.db.update("Article", self.article, "status", "Inactive")
        else:
            frappe.db.update("Article", self.article, "quantity", (qty + 1))
            frappe.db.update("Article", self.article, "status", "Active")