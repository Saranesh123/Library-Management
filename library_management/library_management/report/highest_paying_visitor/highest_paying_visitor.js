// Copyright (c) 2023, SARANESH A and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Highest Paying Visitor"] = {
	"filters": [
		{
			"label" : "Company",
			"fieldname" : "company",
			"fieldtype" : "Link",
			"options" : "Company",
			"default" : frappe.defaults.get_user_default("Company"),
			reqd: 1
		}
	]
};
