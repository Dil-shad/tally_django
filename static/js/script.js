

function undertaker(a, b) {
    $('#all').show()
    var val = a;
    var vin = b;
    console.log(val, vin)
    showforms(vin);
    function showforms(vin) {
        if (vin == 'Bank Accounts' | vin == 'Bank OD A/c' | vin == 'Bank OCC A/c') {
            $('#tax_uin').show()
            $('#tax_reg_typ').hide()
            $('#tax_pan').hide()
            $('#tax_alter_gst').hide()
            $('#provide_banking').hide()
            $('#mail_state').show()
            $('#mail_country').show()
            $('#mail_pincode').show()
            if (vin == 'Bank OD A/c' | vin == 'Bank OCC A/c') {
                $('#OD').show()
                $('#tax_uin').show()
                $('#bank_ac_details').show()
                $('#provide_banking').hide()
                $('#mail_state').show()
                $('#mail_country').show()
                $('#mail_pincode').show()

            }
            else {
                $('#OD').hide()
                $('#bank_ac_details').show()

            }

        } else if (vin == 'Branch/Division') {
            $('#bank_ac_details').hide()
            $('#tax_uin').show()
            $('#tax_reg_typ').show()
            $('#tax_pan').show()
            $('#tax_alter_gst').show()
            $('#OD').hide()
            $('#provide_banking').show()
            $('#mail_state').show()
            $('#mail_country').show()
            $('#mail_pincode').show()





        } else if (vin == 'Capital Accounts') {
            $('#bank_ac_details').hide()
            $('#tax_uin').show()
            $('#tax_reg_typ').show()
            $('#tax_pan').show()
            $('#tax_alter_gst').show()
            $('#OD').hide()
            $('#provide_banking').show()
            $('#mail_state').show()
            $('#mail_country').show()
            $('#mail_pincode').show()
            $('#mail_name').show()
            $('#mail_address').show()

        }
        else if (vin == 'Cash-in-Hand') {
            $('#provide_banking').show()
            $('#mail_address').show()
            $('#tax_uin').hide()
            $('#tax_reg_typ').hide()
            $('#tax_pan').show()
            $('#tax_alter_gst').hide()
            $('#mail_state').hide()
            $('#mail_name').show()
            $('#mail_country').hide()
            $('#mail_pincode').hide()
        } else if (vin == 'Current Assets') {
            $('#mail_name').show()
            $('#mail_address').show()
            $('#mail_state').show()
            $('#mail_country').show()
            $('#mail_pincode').show()
            $('#provide_banking').show()
            $('#bank_ac_details').hide()
            $('#tax_uin').show()
            $('#tax_reg_typ').show()
            $('#tax_pan').show()
            $('#tax_alter_gst').show()
            $('#Satutory_details').show()

        }
        else {
            $('#all').hide()
            


        }
    }
    showunder(val);
    function showunder(val) {
        if (val == 'primary') {
            under;
            document.getElementById('und').innerHTML = ''
        }
        else {
            let under = val
            document.getElementById('und').innerHTML = '(' + under + ')'
        }
    }
}