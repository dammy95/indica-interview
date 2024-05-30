from django.contrib import admin
from api.company.models import Company, Measure, KPI, Control


admin.site.register(Company)
admin.site.register(Measure)
admin.site.register(KPI)
admin.site.register(Control)
