from __future__ import unicode_literals
from django.contrib import admin
from import_export import resources,fields
from import_export.admin import ImportExportMixin
from models import *
from import_export.widgets import ForeignKeyWidget

class StatusResource(resources.ModelResource):
    class Meta:
        model = Status
        skip_unchanged = True
        fields = ('id','content','alias','created_date')

class Up_fileResource(resources.ModelResource):
    status = fields.Field(column_name='status', attribute='status',
                   widget=ForeignKeyWidget(Status, 'alias'))
    class Meta:
        model = Up_file
        skip_unchanged = True
        fields = ('id','blob_name','blob_url','file_name','department','status','desc')

class Up_fileAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = Up_fileResource
    list_display=('id','blob_name','blob_url','file_name','department','status','desc','created_date')
    search_fields=('blob_name','department')
    list_filter = ('blob_name','created_date')
    list_per_page = 10
    ordering = ('id','blob_name','department','created_date')

class StatusAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = StatusResource
    list_display=('id','content','alias','created_date')
    search_fields=('content',)
    list_filter = ('content','created_date')
    list_per_page = 10
    ordering = ('id','content','created_date')

admin.site.register(Up_file,Up_fileAdmin)
admin.site.register(Status,StatusAdmin)