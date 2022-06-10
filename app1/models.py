import email
from locale import currency
from django.db import models

# Create your models here.


class CompanyModel(models.Model):
    cname = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    country = models.CharField(max_length=225)
    state = models.CharField(max_length=225)
    pincode = models.CharField(max_length=225)
    telephone = models.CharField(max_length=225)
    mobile = models.CharField(max_length=225)
    fax = models.CharField(max_length=225)
    email = models.EmailField()
    website = models.CharField(max_length=225)
    is_status = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    #
    currency_symbol = models.CharField(max_length=225, default='₹')
    currency_formal_name = models.CharField(max_length=225, default='INR')
    #
    financial_year = models.DateField()
    books_beginning_from = models.DateField()


class Company_Feature(models.Model):
    cid = models.ForeignKey(
        CompanyModel, on_delete=models.CASCADE, null=True, blank=True)
    # accounting
    maintain_accounts = models.BooleanField(default=True)
    enable_bill_wise_entry = models.BooleanField(default=True)
    # Inventory
    maintain_inventory = models.BooleanField(default=True)
    integrate_accounts_with_inventory = models.BooleanField(default=True)
    # taxation
    enable_gst = models.BooleanField(default=True)
    enable_tds = models.BooleanField(default=False)


class GST(models.Model):
    # gst registraion details
    cid = models.ForeignKey(
        CompanyModel, on_delete=models.CASCADE, null=True, blank=True)
    state = models.CharField(max_length=225)
    registration_type = models.CharField(max_length=225)
    gst_applicable_from = models.DateField()
    gst_uin = models.CharField(max_length=225)
    periodicity_of_gst = models.CharField(max_length=225)
    # additional_features
    alter_gst_rate_dtls = models.BooleanField(default=False)
    tax_liabilty_on_advanced_recipts = models.BooleanField(default=False)
    tax_liabilty_on_reverse_charge = models.BooleanField(default=False)
    gst_classification = models.BooleanField(default=False)
    # provide LUT-Bond details(field)
    lut_bond_dtls = models.BooleanField(default=False)
    # invoice_fetures
    bill_applicable = models.BooleanField(default=True)  # e-way bill
    applicable_from = models.DateField()
    threshold_limt_includes = models.CharField(max_length=225)  # drop down

    applicable_for_intrastate = models.BooleanField(default=True)
    threshold_limit = models.CharField(max_length=225, default='50,000')
    print_e_bill_with_invoice = models.BooleanField(default=False)
    e_invoicing_applicable = models.BooleanField(default=False)


class gateway(models.Model):
    cid = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, null=True, blank=True)
