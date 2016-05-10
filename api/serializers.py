from rest_framework import serializers
from api.models import Up_file,Status,Azure_key,Dirs,Recode_dirs

class Up_fileSerializer(serializers.ModelSerializer):
    status = serializers.SlugRelatedField(queryset=Status.objects.all(), slug_field='alias')
    base_dir = serializers.SlugRelatedField(queryset=Dirs.objects.all(), slug_field='name')
    class Meta:
        model = Up_file
        fields = ('url', 'id', 'base_dir','blob_name', 'blob_url','file_name', 'file_md5', 'file_location',
                  'department','status', 'modified_date', 'created_date')


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status

class Azure_keySerializer(serializers.ModelSerializer):
    class Meta:
        model = Azure_key

class DirsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dirs


class Recode_dirsSerializer(serializers.ModelSerializer):
    base_dir=serializers.SlugRelatedField(queryset=Dirs.objects.all(), slug_field='name')
    sub_dir = serializers.SlugRelatedField(queryset=Dirs.objects.all(), slug_field='name',many=True)
    sub_files=serializers.SerializerMethodField()
    class Meta:
        model = Recode_dirs
        fields = ('url', 'id', 'base_dir', 'sub_dir', 'sub_files')
    def get_sub_files(self,obj):
        base_dir=obj.base_dir
        result=[]
        for m in Up_file.objects.filter(base_dir=base_dir):
            status = m.status.alias
            if status == 'upload':
                sig = Azure_key.objects.get(name='azure').sig
                url = m.blob_url + '?' + sig
            else:
                url = ''
            data = {}
            data['status'] = status
            data['file'] = m.file_name
            data['url'] = url
            data['created_date']=m.created_date
            data['department']=m.department
            result.append(data)
        total={"total":len(result)}
        result.append(total)
        return result
