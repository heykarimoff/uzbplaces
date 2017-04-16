from django.conf import settings
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Province, Region


class TabbedTranslationAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = ['name_en', 'name_ru', 'name_uz', 'code',]

    class Media:
        js = settings.MODELTRANSLATION_ADMIN_SCRIPTS
        css = settings.MODELTRANSLATION_ADMIN_STYLE


class ProvinceAdmin(TabbedTranslationAdmin):
    pass

class RegionAdmin(TabbedTranslationAdmin):
    list_display = TabbedTranslationAdmin.list_display + ['province']


admin.site.register(Province, ProvinceAdmin)
admin.site.register(Region, RegionAdmin)
