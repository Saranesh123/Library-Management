// Copyright (c) 2023, SARANESH A and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Popular Books"] = {
	"filters": [
		{
			"label" : "Frequency",
			"fieldname" : "frequency",
			"fieldtype" : "Select",
			"options" : ["Today", "Date Range", "Monthly", "Quarterly", "Half Yearly", "Yearly"],
			"default" : "",
			"reqd" : 1
		},
		{
			"label" : "No of Days",
			"fieldname" : "days",
			"fieldtype" : "Int",
			"depends_on" : "eval:doc.frequency == 'Date Range'",
			"default" : 1,
		},
		{
			"label" : "Month",
			"fieldname" : "month",
			"fieldtype" : "Select",
			"options" : ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
			"depends_on" : "eval:doc.frequency == 'Monthly'",
			"default" : "Jan"
		},
		{
			"label" : "Quarterly",
			"fieldname" : "quarterly",
			"fieldtype" : "Select",
			"options" : ["Jan - Mar", "Apr - Jun", "Jul - Sep", "Oct - Dec"],
			"depends_on" : "eval:doc.frequency == 'Quarterly'",
			"default" : "Jan - Mar"
		},
		{
			"label" : "Half Yearly",
			"fieldname" : "half_yearly",
			"fieldtype" : "Select",
			"options" : ["Jan - Jun", "Jul - Dec"],
			"depends_on" : "eval:doc.frequency == 'Half Yearly'",
			"default" : "Jan - Jun"
		}
	]
};
