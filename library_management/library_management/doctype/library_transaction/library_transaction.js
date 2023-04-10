// Copyright (c) 2023, SARANESH A and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Transaction', {
	refresh(frm) {
		if(! frm.doc.transaction_date) {
			frm.set_value("transaction_date", frappe.datetime.nowdate());
		}

		if(frm.doc.penalty_amount && frm.doc.docstatus == 0) {
			frm.add_custom_button("Payment Entry", () => {
				frappe.call({
					method: "library_management.library_management.doctype.library_membership.library_membership.create_payment_entry",
					args: {
						party: frm.doc.library_member,
						member_name: frm.doc.member_name,
						doc_name: frm.doc.name,
						doctype: frm.doc.doctype,
						remarks : "Penalty",
					},
					callback(r) {
						frappe.set_route("Form", "Payment Entry", r.message);
					}
				})
			})
		}
	},
	status(frm) {
		frm.set_query("article", () => {
			if(frm.doc.status == "Issue") {
				return{
					filters: {
						status: "Active",
					}
				}
			}
		})
	}
});
