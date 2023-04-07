import frappe

def execute():
    frappe.reload_doc("Setup", "doctype", "Party Type")
    
    if not frappe.db.exists("Party Type", "Visitor"):
        doc = frappe.new_doc("Party Type")
        doc.party_type = "Visitor"
        doc.account_type = "Receivable"
        doc.save()