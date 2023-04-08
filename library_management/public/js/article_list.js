frappe.listview_settings['Article'] = {
    add_fields: ['status'],
    has_indicator_for_draft:1,
    get_indicator: function(doc){
        if(doc.status == "Active") {
            return [__("Active"), "green", "status,=,Active"];
        }
        if(doc.status == "Inactive") {
            return [__("Inactive"), "red", "status,=,Inactive"];
        }
    }
}
