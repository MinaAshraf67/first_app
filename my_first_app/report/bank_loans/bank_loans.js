// Copyright (c) 2025, mina and contributors
// For license information, please see license.txt

frappe.query_reports["Bank Loans"] = {
	"filters": [
		{fieldName: "compacny", label: __("Company"), fieldtype: "Link", options:"Company", default:frappe.defaults.get_user_default("Company"), reqd: 1},
		{fieldName: "from_date", label: __("From Date"), fieldtype: "Date", default: frappe.defaults.get_user_default("year_start_date"),},
		{fieldName: "to_date", label: __("To Date"), fieldtype: "Date", default: frappe.defaults.get_user_default("year_end_date"),}
	]
};
