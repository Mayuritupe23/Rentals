# Copyright (c) 2024, BWH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Voting(Document):
	def validate(self):
		if self.age<=18:
			frappe.throw("not eligible")




	 