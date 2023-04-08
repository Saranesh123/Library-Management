frappe.listview_settings['Library Transaction'] = {
    add_fields: ['status'],
    has_indicator_for_draft:1,
    get_indicator: function(doc){
        if(doc.docstatus == 0) {
            return [__("Draft"), "red", "status,=,Issued"]
        }
        if(doc.status == "Issue") {
            return [__("Issued"), "green", "status,=,Issued"];
        }
        if(doc.status == "Return") {
            return [__("Return"), "red", "status,=,Return"];
        }
    }
}