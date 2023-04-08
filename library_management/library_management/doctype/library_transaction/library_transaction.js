// Copyright (c) 2023, SARANESH A and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Transaction', {
	refresh(frm) {
		if(! frm.doc.transaction_date) {
			frm.set_value("transaction_date", frappe.datetime.nowdate());
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
