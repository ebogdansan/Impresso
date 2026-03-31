from django.contrib import admin
from .models import Membru, Trupa, MembruTrupa

# Register your models here.
@admin.register(Membru)
class MembruAdmin(admin.ModelAdmin):
    list_display = ['idmembru', 'nume', 'prenume', 'cnp', 'adresa']
    search_fields = ['nume', 'prenume', 'cnp']
    list_filter = ['nume']
    
@admin.register(Trupa)
class TrupaAdmin(admin.ModelAdmin):
    list_display = ['numetrupa','genmuzical', 'aninfiintare', 'tara']
    search_fields = ['numetrupa', 'genmuzical']
    list_filter = ['genmuzical', 'tara']

@admin.register(MembruTrupa)
class MembruTrupaAdmin(admin.ModelAdmin):
    list_display = ['membru', 'trupa', 'rol', 'datainscriere', 'activitate']
    search_fields = ['rol', 'activitate', 'trupa']
    list_filter = ['membru__nume', 'membru__prenume', 'trupa__numetrupa']


  			