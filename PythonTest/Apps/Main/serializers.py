"""
Serializers file for Django Rest framework - API
"""
from Article.models import articles
from Store.models import stores
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.views import APIView
from django.contrib.auth import login
from rest_framework.response import Response

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = articles
        fields = ('name', 'description', 'price', 'total_in_shelf', 'total_in_vault', 'store_id')


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = stores
        fields = ('name', 'address')

"""
class MyBasicAuthentication(BasicAuthentication):

    def authenticate(self, request):
        user, _ = super(MyBasicAuthentication, self).authenticate(request)
        login(request, user)
        return user, _


class AuthView(APIView):
    authentication_classes = (MyBasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),
            'auth': unicode(request.auth),
        }
        return Response(content)
"""