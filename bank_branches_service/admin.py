from django.contrib import admin
from bank_branches_service.models import Banks, Branches

# Register your models here.
admin.site.register(Banks)
admin.site.register(Branches)