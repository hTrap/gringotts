from tastypie.resources import ModelResource
from gringotts.models import API


class APIResource(ModelResource):
    class Meta:
        queryset = API.objects.all()
        resource_name = 'capi'
