frappe.ui.form.on('Payment Entry', {
    refresh(frm) {
        if(frm.doc.reference_doctype && frm.doc.docstatus == 1) {
            frm.add_custom_button(frm.doc.reference_doctype, () => {
                frappe.call({
                    method: "library_management.library_management.doctype.library_membership.library_membership.submit_library_membership",
                    args: {
                        doc_name: frm.doc.reference_name,
                        doctype: frm.doc.reference_doctype,
                    }
                })
                frappe.set_route("Form", frm.doc.reference_doctype, frm.doc.reference_name);
            })
        }
    }
})