from django.core.urlresolvers import reverse
from rest_framework import serializers

from .models import Province, Region


class ProvinceSerializer(serializers.ModelSerializer):
    regions = serializers.SerializerMethodField(method_name='get_regions_url')

    class Meta:
        model = Province

        fields = (
            'name',
            'name_en',
            'name_ru',
            'name_uz',
            'regions',
            'code',
        )

    def get_regions_url(self, obj):
        return self.context['request'].build_absolute_uri(
            reverse('address-api:province_regions', kwargs={'province': obj.code}))


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region

        fields = (
            'name',
            'name_en',
            'name_ru',
            'name_uz',
            'code',
        )

