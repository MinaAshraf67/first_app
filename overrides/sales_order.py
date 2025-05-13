from erpnext.selling.doctype.sales_order.sales_order import SalesOrder  # type: ignore
import frappe  # type: ignore
from frappe import _  # type: ignore
from frappe.utils import getdate, date_diff  # type: ignore


class CustomSalesOrder(SalesOrder):
    def before_save(self):
        now = getdate()
        diff = date_diff(self.delivery_date, now)
        self.custom_remaining_time = diff
        print(self.name)

    def update_remaining_time():
        order = frappe.db.get_list(
            "Sales Order",
            filters=[
                ["status", "in", ["Draft", "TO Dliver", "TO Dilver and Bill"]]],
            fields=["name", "delivery_date",
                    "status", "custom_remaining_time"],
        )
        now = getdate()

        for o in order:
            diff = date_diff(o["delivery_date"], now)

            frappe.db.set_value(
                "Sales Order",
                o["name"],
                "custom_remaining_time",
                diff,
                update_modified=False,
            )

        frappe.db.commit()
