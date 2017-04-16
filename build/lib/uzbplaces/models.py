from django.db import models
from django.utils.translation import ugettext_lazy as _
from geoposition.fields import GeopositionField


class Province(models.Model):
    name = models.CharField(_("Province name"), max_length=255)
    code = models.IntegerField(_("Province code"), unique=True)
    weight = models.IntegerField(default=0)
    location = GeopositionField(null=True, blank=True, verbose_name=_("Location"))

    class Meta:
        ordering = ('weight', 'code')
        verbose_name = _("Province")
        verbose_name_plural = _("Provinces")

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(_("Region name"), max_length=255)
    code = models.IntegerField(_("Region code"), unique=True)
    province = models.ForeignKey(to=Province, related_name='regions', verbose_name=_("In which Province?"))
    weight = models.IntegerField(default=0)
    location = GeopositionField(null=True, blank=True, verbose_name=_("Location"))

    class Meta:
        ordering = ('weight', 'code')
        verbose_name = _('Region')
        verbose_name_plural = _('Regions')

    def __str__(self):
        return self.name
