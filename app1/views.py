from multiprocessing import context
from django.shortcuts import render, redirect

from .models import *
from datetime import datetime, date, timedelta
from django.contrib.auth.models import User, auth
# Create your views here.


def index_view(request):
    return render(request, 'index.html')


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
        
        return redirect('Company_Features')



def Gst_Details(request):



    # cid=models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    # state=models.CharField(max_length=225)
    # registration_type=models.CharField(max_length=225)
    # gst_applicable_from=models.DateField()
    # gst_uin=models.CharField(max_length=225)
    # periodicity_of_gst=models.CharField(max_length=225)
    # #additional_features      
    # alter_gst_rate_dtls=models.BooleanField(default=False)   
    # tax_liabilty_on_advanced_recipts=models.BooleanField(default=False)
    # tax_liabilty_on_reverse_charge=models.BooleanField(default=False)
    # gst_classification=models.BooleanField(default=False)
    # lut_bond_dtls=models.BooleanField(default=False) #provide LUT-Bond details(field)
    # #invoice_fetures
    # bill_applicable=models.BooleanField(default=True)#e-way bill
    # applicable_from=models.DateField()
    # threshold_limt_includes=models.CharField(max_length=225)#drop down
    # threshold=models.CharField(max_length=225,default='50,000')
    # applicable_for_intrastate=models.BooleanField(default=True)
    # threshold_limit=models.CharField(max_length=225,default='50,000')
    # print_e_bill_with_invoice=models.BooleanField(default=False)
    # e_invoicing_applicable=models.BooleanField(default=False)
    
    return render(request,'create_gst_details.html')
