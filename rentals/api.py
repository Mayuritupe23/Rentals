import frappe
@frappe.whitelist(allow_guest=True)
def get_emoji():
    return "🤭"

def throw_emoji(doc,event):
    frappe.throw("🥳")

def send_payment_remainders():
    frappe.throw("Hello")

def get_query_conditions_for_vehicle(user):
    # frappe.throw(user)
    return "name=9"