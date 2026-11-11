frappe.listview_settings["Book"] = {
	onload(listview) {
		frappe.realtime.off("book_updated");
		frappe.realtime.on("book_updated", () => listview.refresh());
	},
};

# Please help customize and any update.
