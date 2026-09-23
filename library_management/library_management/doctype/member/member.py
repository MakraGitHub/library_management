# Copyright (c) 2026, Faris Ansari and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Member(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		address: DF.Data | None
		attach_image_vkvt: DF.AttachImage | None
		date: DF.Date
		email: DF.Data | None
		name1: DF.Data | None
		phone: DF.Data
	# end: auto-generated types

	_DOCTYPE_NAME = "Member"
