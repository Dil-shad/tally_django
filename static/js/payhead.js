$(function () {
    $('#name_in_payslip').hide()

})
function on_run() {
    n = $('#affect_sal').val()
    if (n == 'Yes') {
        $('#name_in_payslip').show()

    }
    else {
        $('#name_in_payslip').hide()

    }

}
function hide_divs() {
    $('#undr').hide()
    $('#income_typ').hide()
    $('#comput_tb').hide()
    $('#affect_net_salary').hide()
}
function pay_head_typ() {
    var x = $('#ph_typ').val()
    console.log(x)
    on_run()
    if (x == 'Deduction From Employees') {
        $('#undr').show()
        $('#affect_net_salary').show()
    }
    else if (x == 'Earnings for Employees') {
        $('#undr').show()
        $('#income_typ').show()
        $('#affect_net_salary').show()
    }
    else if (x == 'Not Applicable') {
        $('#undr').show()
        $('#affect_net_salary').show()

    }
    else if (x == "Employee's Statutory Deductions") {
        $('#undr').show()
        $('#comput_tb').show()
        $('#affect_net_salary').show()

    }
    else if (x == "Loans and Advances") {
        $('#undr').show()
        $('#affect_net_salary').show()
    }
    else if (x == "Reimbursements to Employees") {
        $('#undr').show()
        $('#income_typ').show()
        $('#affect_net_salary').show()
    }
    else if (x == "Employer's Statutory Contributions") {
        $('#undr').show()
        $('#comput_tb').show()
        $('#affect_net_salary').show()

    }
}

function create_payhead() {
    console.log('create button clicked')
    let phname = $('#phname').val()
    let phalias = $('#phalias').val()
    let phtyp = $('#ph_typ').val()
    let phunder=$('#ph_under').val()
    let inco_typ=$('#inc_typ').val()
    let affect_sal=$('#affect_sal').val()
    let name_npayslip=$('#name_payslip').val()
    let calculation_typ=$('#calculation_typ').val()
    //compute info
    let compute=$('#compute').val()
    let effectivefrm=$('#cefrm').val()
    let amt_gtrthn=$('#amt_gtrthn').val()
    let amt_upto=$('#amt_upto').val()
    let slb_typ=$('#slb_typ').val()
    let cvalue=$('#cvalue').val()

    //gratuity
    let gdofmonths=$('#gdofmonths').val()
    let fdate1=$('#fdate1').val()





    console.log(inco_typ,'df')

}