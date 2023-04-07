import frappe

def execute():
    frappe.reload_doc("Setup", "doctype", "Party Type")
    
    if not frappe.db.exists("Party Type", "Library Member"):
        doc = frappe.new_doc("Part Type")
        doc.party_type = "Library Member"
        doc.account_type = "Receivable"
        doc.save()