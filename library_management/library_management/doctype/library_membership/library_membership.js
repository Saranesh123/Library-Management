// Copyright (c) 2023, SARANESH A and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Membership', {
	refresh: function(frm) {
		if(! frm.doc.from_date) {
			frm.set_value("from_date", frappe.datetime.nowdate());
		}
	}
});
