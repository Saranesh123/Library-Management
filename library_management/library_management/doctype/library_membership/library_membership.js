// Copyright (c) 2023, SARANESH A and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Membership', {
	refresh(frm) {
		if(! frm.doc.from_date) {
			frm.set_value("from_date", frappe.datetime.nowdate());
		}

		if(!frm.doc.__islocal && !frm.doc.is_paid) {
			frm.add_custom_button("Payment Entry", () => {
				frappe.call({
					method: "library_management.library_management.doctype.library_membership.library_membership.create_payment_entry",
					args: {
						party: frm.doc.library_member,
						member_name: frm.doc.member_name,
					},
					callback(r) {
						frappe.set_route("Form", "Payment Entry", r.message);
					}
				})
			})
		}
	}
});
