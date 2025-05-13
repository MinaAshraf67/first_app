# Copyright (c) 2025, mina and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
    columns, data = [], []
    columns = get_columns(filters=filters)
    banks = frappe.db.get_list("Bank person",)
    for b in banks:
        d = {"bank": b["name"]}
        total_loans = 0
        total_repayments = 0
        loans = frappe.db.get_list("Bank Loan", filters={
                                   "bank_name": b["name"]})
        for l in loans:
            loan = frappe.get_doc("Bank Loan", l["name"])
            total_loans += loan.amount
            total_repayments += loan.repayment

        d["total_loans"] = total_loans
        data.append(d)
    return columns, data



def get_columns(filters=None):
    columns = [
        {"fieldname": "bank", "label": _(
            "Bank"), "fieldtype": "Link", "options": "Bank Loan"},
        {"fieldname": "total_loans", "label": _(
            "Total Loans"), "fieldtype": "Data", },
        {"fieldname": "total_repayments", "label": _(
            "Total repayments"), "fieldtype": "Data"},
        {"fieledname": "outstanding_amount", "label": _(
            "Outstanding Amount"), "fieldtype": "Data"},
    ]
    return columns
