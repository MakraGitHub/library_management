// Copyright (c) 2026, Faris Ansari and contributors
// For license information, please see license.txt

frappe.ui.form.on("Book", {
    onload(frm){
        frappe.realtime.off("book-updated");
        frappe.realtime.on("book_updated", (data) =>{
            if(data.name === frm.doc.name){
                frappe.show_alert({
                    message:__("Book {0} was updated", [data.article]),
                });
                frm.relaod.doc();
            }
        });
    },
    refresh(frm){
        frm.add_custom_button(__('Have a good day!'), ()=>{
            frappe.msgprint('Book',+ frm.doc.article);
;        })
    }
});
