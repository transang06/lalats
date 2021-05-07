from django.contrib import admin
from home.models import Wallet, Category, Spending, DetailSpending


# Register your models here.

class WalletAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "credit"]
    list_display_links = ["user"]


class SpendingAdmin(admin.ModelAdmin):
    list_display = ["user", "time"]


class DetailSpendingAdmin(admin.ModelAdmin):
    list_display = ["spending", "wallet", "category"]


admin.site.register(Wallet, WalletAdmin)

admin.site.register(Category)
admin.site.register(Spending, SpendingAdmin)
admin.site.register(DetailSpending, DetailSpendingAdmin)
