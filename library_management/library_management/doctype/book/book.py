# Copyright (c) 2026, Faris Ansari and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document


class Book(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		article: DF.Data
		description: DF.SmallText | None
		naming_series: DF.Literal["PO.####"]
	# end: auto-generated types

	_DOCTYPE_NAME = "Book"

	# -----custom code here--- #
	
	# Custom validation field 
	def validate(self):
		if not self.article:
			frappe.throw("Article is require")
	# makes fuction update
	def on_update(self):
		frappe.publish_realtime(
			event="book_udpated",
			message={"name":self.name, "article" :self.article},
			after_commit=True,
		)
	# makes function delete 
	def on_delete(self):
		frappe.publish_realtime(
			event="book_deteted",
			message={"name":self.name},
			after_commit=True
		)