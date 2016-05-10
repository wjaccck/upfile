# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from django.dispatch import receiver
from api.models import Up_file,Dirs,Recode_dirs
import re


def _create_dir(dir_name):
    if len(Dirs.objects.filter(name=dir_name))==0:
        m_dir=Dirs.objects.create(name=dir_name)
    else:
        m_dir=Dirs.objects.get(name=dir_name)
    if len(Recode_dirs.objects.filter(base_dir=m_dir))==0:
        Recode_dirs.objects.create(base_dir=m_dir)
    return m_dir

def _add_dir(base_dir,sub_dir):
    sub_dir_info = Recode_dirs.objects.get(base_dir=base_dir)
    sub_dir_names = [x.name for x in sub_dir_info.sub_dir.all()]
    if sub_dir.name in sub_dir_names:
        pass
    else:
        sub_dir_info.sub_dir.add(sub_dir)

def check_dir(dir_name):
    if re.match('^D:\\.*', dir_name):
        split_str='\\'
        end_dir='D:\\work'
    else:
        split_str='/'
        end_dir='/opt'
    sub_dir=_create_dir(dir_name)
    b=dir_name.split(split_str)
    b.pop()
    base_dir_name = split_str.join(b)
    base_dir=_create_dir(base_dir_name)
    _add_dir(base_dir,sub_dir)
    print dir_name
    if dir_name==end_dir:
        pass
    else:
        check_dir(base_dir_name)




@receiver(post_save, sender=Up_file)
def add_dirs(**kwargs):
    if kwargs['created']:
        instance=kwargs['instance']
        dir_name=instance.base_dir.name
        return check_dir(dir_name)


