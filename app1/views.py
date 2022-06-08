from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def index_view(request):
    return render(request, 'index.html')


def create_company(request):
    if request.method == 'POST':
        cname = request.POST['']
        address = request.POST['']
        country = request.POST['']
        state = request.POST['']
        pincode = request.POST['']
        telephone = request.POST['']
        mobile = request.POST['']
        fax = request.POST['']
        email = request.POST['']
        website = request.POST['']
        currency_symbol = request.POST['']
        currency_formal_name = request.POST['']
        financial_year = request.POST['']
        books_beginning_from = request.POST['']

        mdl = CompanyModel(
            cname = cname,
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


            financial_year=financial_year,
            books_beginning_from=books_beginning_from,
        )

    return render(request, 'create_company.html')
