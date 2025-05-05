// Copyright (c) 2025, mina and contributors
// For license information, please see license.txt

frappe.ui.form.on("Bank Loan", {
	// refresh(frm) {

	// },

	repayment_months: (frm) => { calculate(frm) },

	loan_amount: (frm) => { calculate(frm) },

	interest: (frm) => { calculate(frm) }
});

function calculate(frm) {
	if (frm.doc.loan_amount && frm.doc.repayment_months) {
		var monthly = frm.doc.loan_amount / frm.doc.repayment_months;
		var monthly = monthly + (monthly * frm.doc.interest) / 100;

		frm.doc.monthly_repayment = monthly;
		frm.refresh_field("monthly_repayment");
	} else{
		frm.doc.monthly_repayment = 0;
		frm.refresh_field("monthly_repayment");
	}
}
