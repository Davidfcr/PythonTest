from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
from Main.serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import renderer_classes
from rest_framework.decorators import parser_classes
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer
from rest_framework import status
from .models import articles


class article_form(ModelForm):
    class Meta:
        model = articles
        fields = ['name', 'description', 'price', 'total_in_shelf', 'total_in_vault', 'store_id']

def article_create(request):
    form = article_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/crudmenu/article/')
    return render(request, 'crudform.html', {'form':form})

def article_update(request, pk):
    row = get_object_or_404(articles, id=pk)
    form = article_form(request.POST or None, instance=row)
    if form.is_valid():
        form.save()
        return redirect('/crudmenu/article/')
    return render(request, 'crudform.html', {'form':form})

def article_delete(request, pk):
    row = get_object_or_404(articles, id=pk)
    if request.method=='POST':
        row.delete()
        return redirect('/crudmenu/article/')
    return render(request, 'crudconfirmdelete.html', {'object':row})


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def article_collection(request):
    """ API to list or create articles JSON"""
    try:
        if request.method == 'GET':
            article_list = articles.objects.all()
            article_list_count = article_list.count()
            if article_list_count > 1:
                serializer = ArticleSerializer(article_list, many=True)
                response_list = {"articles": serializer.data, "success": "true", "total_elements": article_list_count}
            else:
                serializer = ArticleSerializer(article_list, many=False)
                response_list = {"article": serializer.data, "success": "true", "total_elements": article_list_count}
            return Response(response_list, status=status.HTTP_200_OK)

    except ValueError:
        response_list = {'error_code': status.HTTP_400_BAD_REQUEST, 'success': 'false',
                         'error_message': 'Bad Request'}
        return Response(response_list, status=status.HTTP_400_BAD_REQUEST)

    except articles.PermissionDenied:
        response_list = {'error_code': status.HTTP_401_UNAUTHORIZED, 'success': 'false',
                         'error_message': 'Not authorized'}
        return Response(response_list, status=status.HTTP_401_UNAUTHORIZED)

    except articles.DoesNotExist:
        response_list = {'error_code': status.HTTP_404_NOT_FOUND, 'success': 'false',
                         'error_message': 'Record not found'}
        return Response(response_list, status=status.HTTP_404_NOT_FOUND)

    except Exception, e:
        response_list = {'error_code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'success': 'false',
                         'error_message': 'Server Error'}
        return Response(response_list, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def article_by_store_element(request, key):
    """ API to list all articles by store JSON """
    try:
        if request.method == 'GET':
            article_list = articles.objects.filter(store_id=key)
            article_list_count = article_list.count()
            if article_list_count > 1:
                serializer = ArticleSerializer(article_list, many=True)
                response_list = {"articles": serializer.data, "success": "true", "total_elements": article_list_count}
            else:
                serializer = ArticleSerializer(article_list, many=True)
                response_list = {"article": serializer.data, "success": "true", "total_elements": article_list_count}
            return Response(response_list, status=status.HTTP_200_OK)

    except ValueError:
        response_list = {'error_code': status.HTTP_400_BAD_REQUEST, 'success': 'false',
                         'error_message': 'Bad Request'}
        return Response(response_list, status=status.HTTP_400_BAD_REQUEST)

    except articles.PermissionDenied:
        response_list = {'error_code': status.HTTP_401_UNAUTHORIZED, 'success': 'false',
                         'error_message': 'Not authorized'}
        return Response(response_list, status=status.HTTP_401_UNAUTHORIZED)

    except articles.DoesNotExist:
        response_list = {'error_code': status.HTTP_404_NOT_FOUND, 'success': 'false',
                         'error_message': 'Record not found'}
        return Response(response_list, status=status.HTTP_404_NOT_FOUND)

    except Exception, e:
        response_list = {'error_code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'success': 'false',
                         'error_message': 'Server Error'}
        return Response(response_list, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@parser_classes((XMLParser,))
@renderer_classes((XMLRenderer,))
def article_collection_xml(request):
    """ API to list or create articles in XML"""
    try:
        if request.method == 'GET':
            article_list = articles.objects.all()
            article_list_count = article_list.count()
            if article_list_count > 1:
                serializer = ArticleSerializer(article_list, many=True)
                response_list = {"articles": serializer.data, "success": "true", "total_elements": article_list_count}
            else:
                serializer = ArticleSerializer(article_list, many=False)
                response_list = {"article": serializer.data, "success": "true", "total_elements": article_list_count}
            return Response(response_list, status=status.HTTP_200_OK)

    except ValueError:
        response_list = {'error_code': status.HTTP_400_BAD_REQUEST, 'success': 'false',
                         'error_message': 'Bad Request'}
        return Response(response_list, status=status.HTTP_400_BAD_REQUEST)

    except articles.PermissionDenied:
        response_list = {'error_code': status.HTTP_401_UNAUTHORIZED, 'success': 'false',
                         'error_message': 'Not authorized'}
        return Response(response_list, status=status.HTTP_401_UNAUTHORIZED)

    except articles.DoesNotExist:
        response_list = {'error_code': status.HTTP_404_NOT_FOUND, 'success': 'false',
                         'error_message': 'Record not found'}
        return Response(response_list, status=status.HTTP_404_NOT_FOUND)

    except Exception, e:
        response_list = {'error_code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'success': 'false',
                         'error_message': 'Server Error'}
        return Response(response_list, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@parser_classes((XMLParser,))
@renderer_classes((XMLRenderer,))
def article_by_store_element_xml(request, key):
    """ API to list all articles by store XML """
    try:
        if request.method == 'GET':
            article_list = articles.objects.filter(store_id=key)
            article_list_count = article_list.count()
            if article_list_count > 1:
                serializer = ArticleSerializer(article_list, many=True)
                response_list = {"articles": serializer.data, "success": "true", "total_elements": article_list_count}
            else:
                serializer = ArticleSerializer(article_list, many=True)
                response_list = {"article": serializer.data, "success": "true", "total_elements": article_list_count}
            return Response(response_list, status=status.HTTP_200_OK)

    except ValueError:
        response_list = {'error_code': status.HTTP_400_BAD_REQUEST, 'success': 'false',
                         'error_message': 'Bad Request'}
        return Response(response_list, status=status.HTTP_400_BAD_REQUEST)

    except articles.PermissionDenied:
        response_list = {'error_code': status.HTTP_401_UNAUTHORIZED, 'success': 'false',
                         'error_message': 'Not authorized'}
        return Response(response_list, status=status.HTTP_401_UNAUTHORIZED)

    except articles.DoesNotExist:
        response_list = {'error_code': status.HTTP_404_NOT_FOUND, 'success': 'false',
                         'error_message': 'Record not found'}
        return Response(response_list, status=status.HTTP_404_NOT_FOUND)

    except Exception, e:
        response_list = {'error_code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'success': 'false',
                         'error_message': 'Server Error'}
        return Response(response_list, status=status.HTTP_500_INTERNAL_SERVER_ERROR)