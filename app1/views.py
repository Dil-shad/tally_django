
from multiprocessing import context
from django.shortcuts import render, redirect
from pymysql import NULL

from .models import *
from datetime import datetime, date, timedelta
from django.contrib.auth.models import User, auth
# Create your views here.


def index_view(request):
    obj = CompanyModel.objects.all()
    sel = Selected_Companies_Model.objects.all()
    sec = Selected_Companies_Model.objects.get(id=request.session["scid"])
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
        n = request.session["scid"]
        print(n)
        return redirect('index_view')
    except:
        var = CompanyModel.objects.get(id=pk)

        mdl = Selected_Companies_Model(
            cid=var

        )
        mdl.save()
        request.session["scid"] = mdl.id
        n = request.session["scid"]
        print(n)
        print('saved')
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


def create_group(request):
    if request.method == 'POST':
        gname = request.POST['gname']
        alia = request.POST['alia']
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
        return redirect('index_view')
