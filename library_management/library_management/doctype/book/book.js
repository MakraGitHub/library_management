// Copyright (c) 2026, Faris Ansari and contributors
// For license information, please see license.txt

frappe.ui.form.on("Book", {
    article(frm){
        frappe.show_alert('Please save form before you updated.')
    }
});
