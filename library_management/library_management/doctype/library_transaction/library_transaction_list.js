frappe.listview_settings['Recommendation Note'] = {
    add_fields: ['transaction_type'],
    has_indicator_for_draft:1,
    get_indicator: function(doc){
        if(doc.transaction_type == "Issue"){
            return [__("Issued"), "green", "status,=,Issued"];
        }
        if(doc.transaction_type == "Return"){
            return [__("Return"), "red", "status,=,Return"];
        }
    }
}