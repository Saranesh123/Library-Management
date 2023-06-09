# Copyright (c) 2023, SARANESH A and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import today, add_days, get_last_day, get_year_start, get_year_ending
from datetime import date
from frappe import _

DAYS = {
	"Jan" : 1,
	"Feb" : 2,
	"Mar" : 3,
	"Apr" : 4,
	"May" : 5,
	"Jun" : 6,
	"Jul" : 7,
	"Aug" : 8,
	"Sep" : 9,
	"Oct" : 10,
	"Nov" : 11,
	"Dec" : 12,
}


def execute(filters=None):
	if filters.get("frequency") == "Today":
		start_date = today()
		end_date = today()
	
	if filters.get("frequency") == "Date Range":
		if filters.get("days"):
			start_date = add_days(today(), -(filters.get("days")))
			end_date = today()
		else:
			frappe.throw("No of Days cannot be empty")

	if filters.get("frequency") == "Monthly":
		start_date = date.today().replace(day=1, month=DAYS[filters.get("month")])
		end_date = get_last_day(start_date)

	if filters.get("frequency") == "Quarterly":
		month = filters.get("quarterly").split(" - ")
		start_date = date.today().replace(day=1, month=DAYS[month[0]])
		end_date = get_last_day(date.today().replace(day=1, month=DAYS[month[1]]))

	if filters.get("frequency") == "Half Yearly":
		month = filters.get("half_yearly").split(" - ")
		start_date = date.today().replace(day=1, month=DAYS[month[0]])
		end_date = get_last_day(date.today().replace(day=1, month=DAYS[month[1]]))

	if filters.get("frequency") == "Yearly":
		start_date = get_year_start(today())
		end_date = get_year_ending(today())

	data = frappe.db.sql(
		"""
		SELECT
			tlt.article,
			count(tlt.name) count,
			ta.available_quantity,
			ta.total_quantity
		FROM
			`tabLibrary Transaction` tlt
		INNER JOIN `tabArticle` ta
			ON ta.title = tlt.article
		WHERE
			tlt.transaction_date BETWEEN %s AND %s
			AND tlt.status = 'Issue'
		GROUP BY
			tlt.article
		ORDER BY
			count DESC
		""",
		(start_date, end_date), as_dict=True
	)

	columns = [
		_("Article") + ":Link/Article:150",
		_("Available Quantity") + ":Data:150",
		_("Total Quantity") + ":Data:150",
	]

	return columns, data