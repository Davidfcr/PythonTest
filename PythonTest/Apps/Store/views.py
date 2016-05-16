from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
from Main.serializers import StoreSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer
from rest_framework import status
from .models import stores

# Create your views here.
class store_form(ModelForm):
	class Meta:
		model = stores
		fields = ['name', 'address']

def store_create(request):
	form = store_form(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/crudmenu/store/')
	return render(request, 'crudform.html', {'form':form})

def store_update(request, pk):
	row = get_object_or_404(stores, id=pk)
	form = store_form(request.POST or None, instance=row)
	if form.is_valid():
		form.save()
		return redirect('/crudmenu/store/')
	return render(request, 'crudform.html', {'form':form})

def store_delete(request, pk):
	row = get_object_or_404(stores, id=pk)
	if request.method=='POST':
		row.delete()
		return redirect('/crudmenu/store/')
	return render(request, 'crudconfirmdelete.html', {'object':row})


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def store_collection(request):
    """ API to list all stores """
    try:
        if request.method == 'GET':
            store_list = stores.objects.all()
            store_list_count = store_list.count()
            if store_list_count > 1:
                serializer = StoreSerializer(store_list, many=True)
                response_list = {"stores": serializer.data, "success": "true", "total_elements": store_list_count}
            else:
                serializer = StoreSerializer(store_list, many=False)
                response_list = {"store": serializer.data, "success": "true", "total_elements": store_list_count}
            return Response(response_list, status=status.HTTP_200_OK)

    except ValueError:
        response_list = {'error_code': status.HTTP_400_BAD_REQUEST, 'success': 'false',
                         'error_message': 'Bad Request'}
        return Response(response_list, status=status.HTTP_400_BAD_REQUEST)

    except stores.PermissionDenied:
        response_list = {'error_code': status.HTTP_401_UNAUTHORIZED, 'success': 'false',
                         'error_message': 'Not authorized'}
        return Response(response_list, status=status.HTTP_401_UNAUTHORIZED)

    except stores.DoesNotExist:
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
def store_collection_xml(request):
    """ API to list all stores XML """
    try:
        if request.method == 'GET':
            print("aca vaaaaa")
            store_list = stores.objects.all()
            store_list_count = store_list.count()
            if store_list_count > 1:
                serializer = StoreSerializer(store_list, many=True)
                response_list = {"stores": serializer.data, "success": "true", "total_elements": store_list_count}
            else:
                serializer = StoreSerializer(store_list, many=False)
                response_list = {"store": serializer.data, "success": "true", "total_elements": store_list_count}
            return Response(response_list, status=status.HTTP_200_OK)

    except ValueError:
        response_list = {'error_code': status.HTTP_400_BAD_REQUEST, 'success': 'false',
                         'error_message': 'Bad Request'}
        return Response(response_list, status=status.HTTP_400_BAD_REQUEST)

    except stores.PermissionDenied:
        response_list = {'error_code': status.HTTP_401_UNAUTHORIZED, 'success': 'false',
                         'error_message': 'Not authorized'}
        return Response(response_list, status=status.HTTP_401_UNAUTHORIZED)

    except stores.DoesNotExist:
        response_list = {'error_code': status.HTTP_404_NOT_FOUND, 'success': 'false',
                         'error_message': 'Record not found'}
        return Response(response_list, status=status.HTTP_404_NOT_FOUND)

    except Exception, e:
        response_list = {'error_code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'success': 'false',
                         'error_message': 'Server Error'}
        return Response(response_list, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
