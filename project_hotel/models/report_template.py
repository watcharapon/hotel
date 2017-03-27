from netforce.model import Model, fields

class ReportTemplate(Model):
    _inherit = "report.template"
    _fields ={
        "type": fields.Selection([
            ["cust_invoice", "Customer Invoice"],
            ["cust_credit_note", "Customer Credit Note"],
            ["supp_invoice", "Supplier Invoice"],
            ["payment", "Payment"],
            ["account_move", "Journal Entry"],
            ["sale_quot", "Quotation"],
            ["sale_order", "Sales Order"],
            ["purch_order", "Purchase Order"],
            ["purchase_request", "Purchase Request"],
            ["prod_order", "Production Order"],
            ["goods_receipt", "Goods Receipt"],
            ["goods_transfer", "Goods Transfer"],
            ["goods_issue", "Goods Issue"],
            ["pay_slip", "Pay Slip"],
            ["tax_detail", "Tax Detail"],
            ["hr_expense", "HR Expense"],
            ["cust_invoice", "Customer Invoice"],
            ["cust_credit_note", "Customer Credit Note"],
            ["supp_invoice", "Supplier Invoice"],
            ["payment", "Payment"],
            ["account_move", "Journal Entry"],
            ["sale_quot", "Quotation"],
            ["sale_order", "Sales Order"],
            ["purch_order", "Purchase Order"],
            ["purchase_request", "Purchase Request"],
            ["prod_order", "Production Order"],
            ["goods_receipt", "Goods Receipt"],
            ["goods_transfer", "Goods Transfer"],
            ["goods_issue", "Goods Issue"],
            ["pay_slip", "Pay Slip"],
            ["tax_detail", "Tax Detail"],
            ["hr_expense", "HR Expense"],
            ["landed_cost","Landed Cost"],
            ["borrow_form", "Borrow Request"],
            ["claim_bill","Claim Bill"],
            ["hotel_ticket","Hotel Ticket"],
            # XXX: Better add by config
            ["account_bill","Bill Issue"],
            ["account_cheque","Cheque"],
            ["account_advance","Advance Payment"],
            ["account_advance_clear","Advance Clearing"],

            ["other", "Other"]], "Template Type", required=True, search=True),

        }
ReportTemplate.register()
