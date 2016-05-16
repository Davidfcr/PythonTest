from django.shortcuts import render
from Article.models import articles
from Store.models import stores


def crudselect_view(request, table=None):
    """
    List of the current SuperZapatos DB tables for CRUD
    """
    table_list = None
    if table is not None:
        try:
            if table == 'article':
                table_list = articles.objects.all()
                template = 'crudarticle.html'
            elif table == 'store':
                table_list = stores.objects.all()
                template = 'crudstore.html'
        except articles.DoesNotExist:
            raise articles.DoesNotExist
        except stores.DoesNotExist:
            raise stores.DoesNotExist

    return render(request, template, {'table_list': table_list})
