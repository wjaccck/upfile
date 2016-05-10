from django.shortcuts import render
from rest_framework import permissions
# Create your views here.
import django_filters
from rest_framework import viewsets
from rest_framework import filters as source_filter
import rest_framework_filters as filters
from rest_framework_filters.backends import DjangoFilterBackend
from serializers import Up_fileSerializer,StatusSerializer,Azure_keySerializer,Recode_dirsSerializer,DirsSerializer
from models import Up_file,Status,Azure_key,Dirs,Recode_dirs

class DirsFilter(filters.FilterSet):
    name = filters.CharFilter(name="name")
    class Meta:
        model = Dirs
        fields = ['name']

class StatusFilter(filters.FilterSet):
    name = filters.CharFilter(name="alias")
    class Meta:
        model = Status
        fields = ['name']

class UpfileFilter(filters.FilterSet):
    status=filters.RelatedFilter(StatusFilter,name='status')
    start_date = filters.DateFilter(name="created_date", lookup_type='gte')
    end_date=filters.DateFilter(name="created_date", lookup_type='lte')
    name=filters.ModelMultipleChoiceFilter
    # created_date__gte=filters.DateFilter(name='created_date__gte')
    class Meta:
        model = Up_file
        fields = ['blob_name','department','status','created_date','start_date','start_date']

class Recode_dirsFilters(filters.FilterSet):
    base_dir = filters.RelatedFilter(DirsFilter, name='base_dir')
    class Meta:
        model = Recode_dirs
        fields = ['base_dir']


class Up_fileViewSet(viewsets.ModelViewSet):
    queryset = Up_file.objects.all()
    serializer_class = Up_fileSerializer
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (DjangoFilterBackend,source_filter.SearchFilter)
    # filter_fields = ('blob_name',)
    search_fields = ('blob_name',)
    filter_class=UpfileFilter

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (DjangoFilterBackend,source_filter.SearchFilter)
    filter_fields = ('content',)
    search_fields = ('^content',)

class Azure_keyViewSet(viewsets.ModelViewSet):
    queryset = Azure_key.objects.all()
    serializer_class = Azure_keySerializer
    permission_classes = (permissions.DjangoModelPermissions,)

class DirsViewSet(viewsets.ModelViewSet):
    queryset = Dirs.objects.all()
    serializer_class = DirsSerializer
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (DjangoFilterBackend,)
    filter_class=DirsFilter

class Recode_dirsViewSet(viewsets.ModelViewSet):
    queryset = Recode_dirs.objects.all()
    serializer_class = Recode_dirsSerializer
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (DjangoFilterBackend,)
    filter_class=Recode_dirsFilters