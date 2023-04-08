import frappe
from frappe.utils import today

def update_membership(doc, action):
    frappe.db.update(doc.reference_doctype, doc.reference_name, "is_paid", 1)