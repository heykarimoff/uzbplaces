from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import pagination

from .models import Province, Region
from .serializers import ProvinceSerializer, RegionSerializer


class NoPagination(pagination.PageNumberPagination):
    """
    NoPagination for certain circumstances
    """
    page_size = 0


class ProvinceList(generics.ListAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    pagination_class = NoPagination


class RegionList(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    pagination_class = NoPagination

    def get_queryset(self):
        qs = ()

        province = self.kwargs.get('province', None)

        if province:
            return self.queryset.filter(province=province)
        return qs


class RegionDetail(generics.RetrieveAPIView):
    serializer_class = RegionSerializer

    def get_object(self):
        province = self.kwargs.get('province', None)
        code = self.kwargs.get('code', None)

        if province and code:
            return get_object_or_404(Region, province=province, code=code)
        return None
