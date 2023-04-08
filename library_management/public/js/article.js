frappe.ui.form.on('Article', {
    refresh(frm) {
        frm.add_custom_button("Stock UP", () => {
            var d = new frappe.ui.Dialog({
                title: __("Stock UP"),
                fields: [
                    {
                        "label" : "Stock UP Quantity",
                        "fieldname" : "stock_qty",
                        "fieldtype" : "Int",
                        "reqd" : 1
                    }
                ],
                primary_action() {
                    var data = d.get_values();
                    frm.set_value("quantity", frm.doc.quantity + data.stock_qty);
                    frm.refresh_field("quantity");
                    frm.save();
                    d.hide();
                },
                primary_action_label: __("Update")
            });
            d.show();
        })

        frm.add_custom_button("Stock DOWN", () => {
            var d = new frappe.ui.Dialog({
                title: __("Stock DOWN"),
                fields: [
                    {
                        "label" : "Stock DOWN Quantity",
                        "fieldname" : "stock_qty",
                        "fieldtype" : "Int",
                        "reqd" : 1
                    }
                ],
                primary_action() {
                    var data = d.get_values();
                    frm.set_value("quantity", frm.doc.quantity - data.stock_qty);
                    frm.refresh_field("quantity");
                    frm.save();
                    d.hide();
                },
                primary_action_label: __("Update")
            });
            d.show();
        })
    }
})