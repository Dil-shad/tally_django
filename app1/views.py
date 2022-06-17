from multiprocessing import context
from unicodedata import name
from django.http import JsonResponse
from django.shortcuts import render, redirect
from pymysql import NULL
from .models import *
from datetime import datetime, date, timedelta
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index_view(request):
    obj = CompanyModel.objects.all()
    sel = Selected_Companies_Model.objects.all()
    sec = CompanyModel.objects.get(id=request.session["scid"])
    print(sec)
    grp_under_lst = GroupModel.objects.all().order_by('name')

    context = {
        'obj': obj,
        'sc': sel,
        's': sec,
        "grp": grp_under_lst,
    }
    return render(request, 'index.html', context)


def create_company(request):
    if request.method == 'POST':
        toda = date.today()
        tod = toda.strftime("%Y-04-01")

        cname = request.POST['cname']
        address = request.POST['addr']
        country = request.POST['country']
        state = request.POST['state']
        pincode = request.POST['pinco']
        telephone = request.POST['tele']
        mobile = request.POST['mob']
        fax = request.POST['fax']
        email = request.POST['mail']
        website = request.POST['web']
        currency_symbol = request.POST['symbol']
        currency_formal_name = request.POST['cny_name']
        fin_year = request.POST['fy_date']
        books_from = request.POST['bb_date']

        if len(currency_symbol) == 0:
            currency_symbol = '₹'
        if len(currency_formal_name) == 0:
            currency_formal_name = 'INR'

        if len(fin_year) <= 0:
            fin_year = toda.strftime("%Y-04-01")

        if len(books_from) <= 0:
            books_from = toda.strftime("%Y-04-01")

        mdl = CompanyModel(
            cname=cname,
            address=address,
            country=country,
            state=state,
            pincode=pincode,
            telephone=telephone,
            mobile=mobile,
            fax=fax,
            email=email,
            website=website,

            currency_symbol=currency_symbol,
            currency_formal_name=currency_formal_name,

            financial_year=fin_year,
            books_beginning_from=books_from,
        )
        mdl.save()
        request.session["cid"] = mdl.id
        return redirect('Company_Features')
    return render(request, 'create_company.html')


def Company_Features(request):

    var = request.session["cid"]
    var1 = CompanyModel.objects.get(id=var)
    context = {
        'cm': var1
    }

    return render(request, 'company_feature_form.html', context)


def Company_Features_Save(request, pk):

    if request.method == 'POST':
        ciid = CompanyModel.objects.get(id=pk)
        maintain_accounts = request.POST['MA']
        enable_bill_wise_entry = request.POST['wise_en']
        maintain_inventory = request.POST['MI']
        integrate_accounts_with_inventory = request.POST['IAWI']
        enable_gst = request.POST['gst']
        enable_tds = request.POST['tds']

        print(ciid)
        md = Company_Feature(
            cid=ciid,
            maintain_accounts=maintain_accounts,
            enable_bill_wise_entry=enable_bill_wise_entry,
            maintain_inventory=maintain_inventory,
            integrate_accounts_with_inventory=integrate_accounts_with_inventory,
            enable_gst=enable_gst,
            enable_tds=enable_tds,
        )
        md.save()
        if enable_gst == 'True':
            return redirect('gst_details')
        else:
            pass

        return redirect('Company_Features')


def gst_details(request):

    if request.method == 'POST':
        toda = date.today()
        tod = toda.strftime("%Y-04-01")

        pk = request.session["cid"]
        ciid = CompanyModel.objects.get(id=pk)

        state = request.POST['ste']
        reg_typ = request.POST['reg_tp']
        gst_af = request.POST['gpf']
        uin = request.POST['uin']
        peroidici = request.POST['priod']
        #
        alter_gst = request.POST['alt_gst']
        liabi_adv_rece = request.POST['tax_liab']
        liabi_reverse_chrg = request.POST['liab_reve']
        gst_clasific = request.POST['gst_clasif']
        bond_dtls = request.POST['bond']
        #
        e_bil_applicable = request.POST['e_bill']
        gst_applicable_from = request.POST['gap_date']
        thres_limit_inc = request.POST['thre_limit_include']
        threshold_lmt = request.POST['threshold_limit_amt']
        applicable_intrstate = request.POST['intrestate']
        e_bil_wit_invo = request.POST['bil_invoi']
        e_invo_applic = request.POST['e_invo_applicable']

        mdl = GST(

            cid=ciid,
            state=state,
            registration_type=reg_typ,
            gst_applicable_from=gst_af,
            gst_uin=uin,
            periodicity_of_gst=peroidici,
            alter_gst_rate_dtls=alter_gst,
            tax_liabilty_on_advanced_recipts=liabi_adv_rece,
            tax_liabilty_on_reverse_charge=liabi_reverse_chrg,
            gst_classification=gst_clasific,
            lut_bond_dtls=bond_dtls,
            bill_applicable=e_bil_applicable,
            applicable_from=gst_applicable_from,
            threshold_limt_includes=thres_limit_inc,
            applicable_for_intrastate=applicable_intrstate,
            threshold_limit=threshold_lmt,
            print_e_bill_with_invoice=e_bil_wit_invo,
            e_invoicing_applicable=e_invo_applic,

        )

        mdl.save()
        request.session["cid"] = ''

        return redirect('index_view')

    return render(request, 'create_gst_details.html')


def selected_companies(request, pk):
    try:
        chk = Selected_Companies_Model.objects.get(cid=pk)
        print('already exist')

        return redirect('index_view')
    except:
        var = CompanyModel.objects.get(id=pk)

        mdl = Selected_Companies_Model(
            cid=var

        )
        mdl.save()

        print('saved')
        return redirect('index_view')


def log_company(request, pk):
    var = CompanyModel.objects.get(id=pk)
    request.session["scid"] = var.id
    k = request.session["scid"]
    print(k)

    return redirect('index_view')


def shut_company(request, pk):

    mdl = Selected_Companies_Model.objects.get(id=pk)
    mdl.delete()
    return redirect('index_view')


def alter_company(request, pk):
    if request.method == 'POST':
        try:
            e = CompanyModel.objects.get(id=pk)
            e.cname = request.POST.get('cname')
            e.address = request.POST.get('addr')
            e.country = request.POST.get('country')
            e.state = request.POST.get('state')
            e.pincode = request.POST.get('pinco')
            e.telephone = request.POST.get('tele')
            e.mobile = request.POST.get('mob')
            e.fax = request.POST.get('fax')
            e.email = request.POST.get('mail')
            e.website = request.POST.get('web')
            e.currency_symbol = request.POST.get('symbol')
            e.currency_formal_name = request.POST.get('cny_name')
            e.financial_year = request.POST.get('fy_date')
            e.books_beginning_from = request.POST.get('bb_date')
            e.save()
            return redirect('index_view')
        except:
            pass

    var = Selected_Companies_Model.objects.get(id=pk)

    mdl = CompanyModel.objects.get(id=var.cid.id)
    context = {
        'obj': mdl
    }

    return render(request, 'alter_company.html', context)


@csrf_exempt
def create_group(request):
    if request.method == 'POST':
        gname = request.POST['gname']
        alia = request.POST['alia']
        if len(gname) <= 0:
            return JsonResponse({
                'status': 00
            })

        if len(alia) <= 0:
            alia = None
        else:
            pass

        under = request.POST['und']
        gp = request.POST['subled']
        nett = request.POST['nee']
        calc = request.POST['cal']
        meth = request.POST['meth']

        mdl = GroupModel(
            name=gname,
            alias=alia,
            under=under,
            gp_behaves_like_sub_ledger=gp,
            nett_debit_credit_bal_reporting=nett,
            used_for_calculation=calc,
            method_to_allocate_usd_purchase=meth,
        )
        mdl.save()
        # return redirect('index_view')
        return JsonResponse({
            'status': 1
        })


def create_ledger(request):
    if request.method == 'POST':

        # Ledger Basic
        Lname = request.POST['Lname']
        Lalias = request.POST['Lalias']
        Lunder = request.POST['Lund']
        try:
            mdl = GroupModel.objects.get(name=Lunder)

            fl = mdl
            print('IN name')
        except:

            try:
                mdl = GroupModel.objects.get(alias=Lunder)
                print('in ALIAS')
                fl = mdl
            except:
                print("NOT found")

        Lopening_bal = request.POST['Lopening']
        typ_of_ledg = request.POST['typ_of_ledg']
        typ_of_duty = request.POST['typ_of_duty']
        percet_of_calc = request.POST['percet_of_calc']
        main_balance_bill_ = request.POST['main_balance_bill_']  # bool
        chk_credit_days = request.POST['chk_credit_days']  # bool
        def_cr_period = request.POST['def_cr_period']
        # Provide Banking Details
        provide_banking = request.POST['provide_banking']  # bool

        # Banking_details
        B_od_limit = request.POST['B_od_limit']
        B_ac_holder_name = request.POST['B_ac_name']
        B_ac_no = request.POST['B_ac_no']
        B_ifsc = request.POST['B_ac_ifsc']
        B_swift_code = request.POST['B_ac_swift']
        B_name = request.POST['B_name']
        B_branch = request.POST['B_branch']
        '''bank Configuration'''
        B_alter_chq_bks = request.POST['B_alter_chq_bks']  # bool
        B_name_enbl_chq_prtg = request.POST['B_name_enbl_chq_prtg']  # bool

        # Mailing_details
        Mname = request.POST['Mname']
        Maddress = request.POST['Maddress']
        Mstate = request.POST['Mstate']
        Mcountry = request.POST['Mcountry']
        Mpincode = request.POST['Mpincode']

        # Tax_Registration_Details
        Tgst_uin = request.POST['Tgst_uin']
        Treg_typ = request.POST['Treg_typ']
        Tpan_no = request.POST['Tpan_no']
        T_alter_gst = request.POST['T_alter_gst']

        # Satutory Details
        assemble_calc = request.POST['assemble_value']
        is_gst_applicable = request.POST['is_gst_applicable']
        typ_of_supply = request.POST['typ_of_supply']

        # -------------------------#
        sec = CompanyModel.objects.get(id=request.session["scid"])
        Lmdl = LedgerModel(
            cid=sec,
            ledger_name=Lname,
            ledger_alias=Lalias,
            group=fl,
            ledger_opening_bal=Lopening_bal,
            ledger_type=typ_of_ledg,
            type_of_duty=typ_of_duty,
            percent_of_calculation=percet_of_calc,
            maintain_bal_bill=main_balance_bill_,
            credit_days_during_voucher_entry=chk_credit_days,
            default_cr_peroid=def_cr_period,
            provide_banking_details=provide_banking,
        )
        Lmdl.save()
        idd = Lmdl
        Bmdl = BankingDetails(
            cid=sec,
            ledger_id=idd,
            od_limit=B_od_limit,
            holder_name=B_ac_holder_name,
            ac_number=B_ac_no,
            ifsc=B_ifsc,
            swift_code=B_swift_code,
            bank_name=B_name,
            branch_name=B_branch,
            alter_chk_bks=B_alter_chq_bks,
            enbl_chk_printing=B_name_enbl_chq_prtg,
        )
        Bmdl.save()
        M_mdl = MailingAddressModel(
            cid=sec,
            ledger_id=idd,
            name=Mname,
            address=Maddress,
            state=Mstate,
            country=Mcountry,
            pincode=Mpincode,
        )
        M_mdl.save()
        T_mdl = TaxRegisterModel(
            cid=sec,
            ledger_id=idd,
            gst_uin=Tgst_uin,
            register_type=Treg_typ,
            pan_no=Tpan_no,
            alter_gst_details=T_alter_gst,

        )
        T_mdl.save()
        LS_mdl = LedgerSatutoryModel(
            cid=sec,
            ledger_id=idd,
            assessable_calculation=assemble_calc,
            gst_applicable=is_gst_applicable,
            type_of_supply=typ_of_supply,


        )
        LS_mdl.save()
        return redirect('index_view')

    grp_under_lst = GroupModel.objects.all().order_by('name')
    sec = CompanyModel.objects.get(id=request.session["scid"])
    context = {
        'grp': grp_under_lst,
        's': sec,
    }
    return render(request, 'create_ledger.html', context)


def create_voucher(request):
    if request.method == 'POST':
        Vname = request.POST['nam']
        alias = request.POST['alias']
        vtype = request.POST['vtype']
        abbre = request.POST['abbre']
        activ_vou_typ = request.POST['avtyp']  # bool
        meth_vou_num = request.POST['meth_vou_num']
        use_effct_date = request.POST['uefftdate']  # bool
        allow_zero_trans = request.POST['allow_zero_trans']  # bool
        allow_naration_in_vou = request.POST['allow_naration_in_vou']  # bool
        enbl_def_accout_alloc = request.POST['enbl_def_accout_alloc']  # bool
        track_addi_coast = request.POST['track_addi_coast']  # bool
        # bool
        use_as_manfacturing_journal = request.POST['use_as_manfacturing_journal']
        #
        print_vou_aft_save = request.POST['print_vou_aft_save']  # b
        print_formal_recept = request.POST['print_formal_recept']  # b
        def_juri = request.POST['def_juri']
        default_title = request.POST['default_title']
        alte_declaration = request.POST['alte_declaration']  # b

        mdl = VoucherModel(
            voucher_name=Vname,
            alias=alias,
            voucher_type=vtype,
            abbreviation=abbre,
            active_this_voucher_type=activ_vou_typ,
            method_voucher_numbering=meth_vou_num,
            use_effective_date=use_effct_date,
            allow_zero_value_trns=allow_zero_trans,
            allow_naration_in_voucher=allow_naration_in_vou,
            enable_default_ac_allocation=enbl_def_accout_alloc,
            track_additional_cost_purchase=track_addi_coast,
            use_as_manf_journal=use_as_manfacturing_journal,
            print_voucher_af_save=print_vou_aft_save,
            print_formal_recept=print_formal_recept,
            default_juridiction=def_juri,
            default_title=default_title,
            alter_decalaration=alte_declaration,

        )
        mdl.save()
        return redirect('index_view')

    context = {

    }
    return render(request, 'create_voucher.html', context)
