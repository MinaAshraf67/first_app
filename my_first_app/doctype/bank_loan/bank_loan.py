# Copyright (c) 2025, mina and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class BankLoan(Document):
    def on_update(self):
        self.schedule = []
        d = self.repayment_date
        amount = self.loan_amount * self.interest / 100
        for i in range(int(self.repayment_months)):
            repayment = self.append("schedule", {})
            repayment.payment_date = d
            repayment.principal_amount = self.loan_amount / self.repayment_months
            repayment.interest_amount = repayment.principal_amount * self.interest / 100
            repayment.total_payment = repayment.principal_amount + repayment.interest_amount
            repayment.balance_loan_amount = amount - repayment.total_payment
            amount = amount - repayment.total_payment
