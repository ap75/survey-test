from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from .models import SurveyRes


class SurveyResource(ModelResource):
    #timestamp = fields.DateTimeField(readonly=True)

    class Meta:
        queryset = SurveyRes.objects.all()
        resource_name = 'survey'
        authorization = Authorization()
