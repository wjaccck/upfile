from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Azure_key(models.Model):
    sig=models.CharField(max_length=300)
    name=models.CharField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

class Status(models.Model):
    content=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.alias

class Dirs(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __unicode__(self):
        return self.name

class Recode_dirs(models.Model):
    base_dir=models.ForeignKey(Dirs,related_name='base_dir')
    sub_dir=models.ManyToManyField(Dirs,related_name='sub_dir')
    def __unicode__(self):
        return self.base_dir.name

class Up_file(models.Model):
    base_dir=models.ForeignKey(Dirs,related_name='base_file_dir')
    blob_name=models.CharField(max_length=100,db_index=True)
    blob_url=models.URLField(blank=True)
    file_name=models.CharField(max_length=100,db_index=True)
    file_md5=models.CharField(max_length=100,blank=True,default='')
    file_location=models.CharField(max_length=300)
    department=models.CharField(max_length=100,default='emoney',db_index=True)
    status=models.ForeignKey(Status)
    desc=models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True,db_index=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
      return self.blob_name

    class Meta:
        ordering=['-created_date']





