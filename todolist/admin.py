from django.contrib import admin
from .models import Task, ValorIntroducido, Resultados, Bitcoinpriceves,Bitcoinpriceuk

# Register your models here.
admin.site.register(Task)
admin.site.register(ValorIntroducido)
admin.site.register(Resultados)
admin.site.register(Bitcoinpriceves)
admin.site.register(Bitcoinpriceuk)
