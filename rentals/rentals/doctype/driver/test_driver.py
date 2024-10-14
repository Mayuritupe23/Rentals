# Copyright (c) 2024, BWH and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestDriver(FrappeTestCase):
	def test_full_name_correctly_set(self):
		test_driver = frappe.new_doc("Driver")
		test_driver.first_name="Chitra"
		test_driver.last_name="Bodakhe"
		test_driver.licence_number="DFG45323"
		test_driver.insert()
		test_driver.save()

		self.assertEqual(test_driver.full_name, "Chitra Bodakhe")

	def test_full_name_correctly_set(self):
		test_driver = frappe.new_doc("Driver")
		test_driver.first_name="Chitra"
	
		test_driver.licence_number="DFG45323"
		test_driver.insert()
		test_driver.save()

		self.assertEqual(test_driver.full_name, "Chitra")


