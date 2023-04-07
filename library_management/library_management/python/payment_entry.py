import frappe
from frappe.utils import today

def update_membership(doc, action):
    library_membership = frappe.get_doc("Library Membership", {"library_member": doc.party, "from_date": today()})
    frappe.db.update("Library Membership", library_membership.name, "is_paid", 1)
    
def validate_article(doc, action):