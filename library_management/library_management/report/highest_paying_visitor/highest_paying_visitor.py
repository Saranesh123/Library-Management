# Copyright (c) 2023, SARANESH A and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	data = frappe.db.sql(
		"""
		SELECT
			party,
			sum(paid_amount) amount
		FROM
			`tabPayment Entry`
		WHERE
			party_type = 'Visitor'
			AND custom_remarks = 'Membership'
			AND company = %s
		GROUP BY
			party
		ORDER BY
			amount DESC
		""",
		(filters.get("company")), as_dict=True
	)

	columns = [
		_("Party") + ":Link/Visitor:150",
		_("Amount") + ":Currency:300",
	]

	return columns, data
