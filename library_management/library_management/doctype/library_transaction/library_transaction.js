// Copyright (c) 2023, SARANESH A and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Transaction', {
	refresh(frm) {
		if(! frm.doc.transaction_date) {
			frm.set_value("transaction_date", frappe.datetime.nowdate());
		}

		frm.set_query("article", () => {
			return{
				filters: {
					status: "Active",
				}
			}
		})
	}
});
