// Copyright (c) 2024, BWH and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Booking", {
	refresh(frm) {
        
	},
    rate(frm){
            //recalculate total
            frm.trigger("update_total_amount");
    },
    update_total_amount(frm){
        distance(frm,cdt,cdn){
            let total_d=0;
            for(let item of frm.doc.items){
                console.log(item.distance)
                total_d+=item.distance;
            }
            const amount=frm.doc.rate*total_d;
            frm.set_value("total_amount",amount);

    }
});

frappe.ui.form.on('Ride Booking Item', {
	refresh(frm) {
		// your code here
	},
    distance(frm,cdt,cdn){
        frm.trigger("update_total_amount");
    }



        // console.log(cdt,cdn);
        // // console.log("child table distance changed!");
        // // console.log(frappe.get_doc(cdt,cdn));
        // my_child=frappe.get_doc(cdt,cdn);
        // frappe.model.set_value(cdt,cdn,"source","Updated Source")

    }
})