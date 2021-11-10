from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Books

def pagination(request):
    books=Books.objects.all()
    book_paginator=Paginator(books,2)
    page_num=request.GET.get('page')
    page=book_paginator.get_page(page_num)
    context={'count':book_paginator.count,
             'page':page}
    template_name='fapp/index.html'
    return render(request,template_name,context)

