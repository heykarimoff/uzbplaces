from modeltranslation.translator import translator, TranslationOptions

from .models import Province, Region


class ProvinceTranslationOptions(TranslationOptions):
    fields = ('name', )


class RegionTranslationOptions(TranslationOptions):
    fields = ('name', )


translator.register(Province, ProvinceTranslationOptions)
translator.register(Region, RegionTranslationOptions)
