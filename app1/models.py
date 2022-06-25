
from ast import alias
import email
from locale import currency
from operator import mod
from pyexpat import model
from unicodedata import name
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

    def __str__(self):
        return self.cname


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


class Selected_Companies_Model(models.Model):
    cid = models.ForeignKey(
        CompanyModel, on_delete=models.CASCADE, null=True, blank=True)


class GroupModel(models.Model):
    name = models.CharField(max_length=225)
    alias = models.CharField(max_length=225, null=True)
    under = models.CharField(max_length=225)
    gp_behaves_like_sub_ledger = models.BooleanField(default=False)
    nett_debit_credit_bal_reporting = models.BooleanField(default=False)
    used_for_calculation = models.BooleanField(default=False)
    method_to_allocate_usd_purchase = models.CharField(
        max_length=225, null=True, blank=True)

    def __str__(self):
        return self.name


class LedgerModel(models.Model):
    cid = models.ForeignKey(
        CompanyModel, on_delete=models.CASCADE, null=True, blank=True)
    ledger_name = models.CharField(max_length=225)
    ledger_alias = models.CharField(max_length=225)

    group = models.ForeignKey(
        GroupModel, on_delete=models.CASCADE, null=True, blank=True)
    ledger_opening_bal = models.CharField(max_length=225)
    ledger_type = models.CharField(max_length=225)
    type_of_duty = models.CharField(max_length=225)
    percent_of_calculation = models.CharField(max_length=225)
    maintain_bal_bill = models.CharField(max_length=225)
    credit_days_during_voucher_entry = models.CharField(max_length=225)
    default_cr_peroid = models.CharField(max_length=225)
    provide_banking_details = models.BooleanField()

    def __str__(self):
        return self.ledger_name


class BankingDetails(models.Model):
    cid = models.ForeignKey(
        CompanyModel, on_delete=models.CASCADE, null=True, blank=True)
    ledger_id = models.ForeignKey(
        LedgerModel, on_delete=models.CASCADE, null=True, blank=True)
    od_limit = models.CharField(max_length=225)
    holder_name = models.CharField(max_length=225)
    ac_number = models.CharField(max_length=225)
    ifsc = models.CharField(max_length=225)
    swift_code = models.CharField(max_length=225)
    bank_name = models.CharField(max_length=225)
    branch_name = models.CharField(max_length=225)
    alter_chk_bks = models.BooleanField()
    enbl_chk_printing = models.BooleanField()


class MailingAddressModel(models.Model):
    cid = models.ForeignKey(
        CompanyModel, on_delete=models.CASCADE, null=True, blank=True)
    ledger_id = models.ForeignKey(
        LedgerModel, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    state = models.CharField(max_length=225)
    country = models.CharField(max_length=225)
    pincode = models.CharField(max_length=225)


class TaxRegisterModel(models.Model):
    cid = models.ForeignKey(
        CompanyModel, on_delete=models.CASCADE, null=True, blank=True)
    ledger_id = models.ForeignKey(
        LedgerModel, on_delete=models.CASCADE, null=True, blank=True)
    gst_uin = models.CharField(max_length=225)
    register_type = models.CharField(max_length=225)
    pan_no = models.CharField(max_length=225)
    alter_gst_details = models.BooleanField()


class LedgerSatutoryModel(models.Model):
    cid = models.ForeignKey(
        CompanyModel, on_delete=models.CASCADE, null=True, blank=True)
    ledger_id = models.ForeignKey(
        LedgerModel, on_delete=models.CASCADE, null=True, blank=True)
    assessable_calculation = models.CharField(max_length=225)
    gst_applicable = models.CharField(max_length=225)
    type_of_supply = models.CharField(max_length=225)


class VoucherModel(models.Model):
    voucher_name = models.CharField(max_length=225)
    alias = models.CharField(max_length=225)
    voucher_type = models.CharField(max_length=225)
    abbreviation = models.CharField(max_length=225)
    active_this_voucher_type = models.BooleanField()
    method_voucher_numbering = models.CharField(max_length=225)
    use_effective_date = models.BooleanField()
    allow_zero_value_trns = models.BooleanField()
    allow_naration_in_voucher = models.BooleanField()
    enable_default_ac_allocation = models.BooleanField()
    track_additional_cost_purchase = models.BooleanField()
    use_as_manf_journal = models.BooleanField()
    print_voucher_af_save = models.BooleanField()
    print_formal_recept = models.BooleanField()
    default_juridiction = models.CharField(max_length=225)
    default_title = models.CharField(max_length=225)
    alter_decalaration = models.BooleanField()


class CurrencyModel(models.Model):
    symbol = models.CharField(max_length=225)
    fname = models.CharField(max_length=225)
    iso_code = models.CharField(max_length=225)
    n_deci_placs = models.CharField(max_length=225)
    smt_millon = models.BooleanField()
    symbol_to_amount = models.BooleanField()
    space_bt_sy = models.BooleanField()
    amount_after_decimal = models.CharField(max_length=225)
    amount_in_words = models.CharField(max_length=225)


class StockGroupModel(models.Model):
    name = models.CharField(max_length=225)
    alias = models.CharField(max_length=225)
    under = models.CharField(max_length=225)
    item_be_added = models.BooleanField()
    alter = models.BooleanField()

    def __str__(self):
        return self.name


class StockCategoryModel(models.Model):
    scat_name = models.CharField(max_length=225)
    scat_alias = models.CharField(max_length=225)
    scat_under = models.CharField(max_length=225)


class StockItemCreation(models.Model):
    cid = models.ForeignKey(
        CompanyModel, on_delete=models.CASCADE, null=True, blank=True)
    sname = models.CharField(max_length=225)
    salias = models.CharField(max_length=225)
    sunder = models.ForeignKey(
        StockGroupModel, on_delete=models.CASCADE, null=True, blank=True)
    sname = models.CharField(max_length=225)
    units = models.CharField(max_length=225)
    gst_applicable = models.CharField(max_length=225)
    alter_gst_details = models.BooleanField()
    typ_supply = models.CharField(max_length=225)
    rate_duty = models.CharField(max_length=225)
    opening_bal = models.CharField(max_length=225)


class UnitCreation(models.Model):
    cid = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=225)
    symbol = models.CharField(max_length=225)
    formal_name = models.CharField(max_length=225)
    quc = models.CharField(max_length=225)
    num_decimal_plce= models.CharField(max_length=225)

class InventeryLocation(models.Model):
    cid = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    

class EmployeeGroup(models.Model):
    cid= models.ForeignKey(CompanyModel, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    

