from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Category, Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage

def index(request):
    var = "This is a test line"
    return HttpResponse(var)

def allProdCat(request,browser_slug=None):
    any_var = None
    products_list = None
    if browser_slug!=None:
        any_var = get_object_or_404(Category, slug=browser_slug)
        #We are searching the object in Category model with slug value that is passed in the function argument.
        products_list = Product.objects.filter(category=any_var,availability=True)
    else:
        products_list = Product.objects.all().filter(availability=True)
        #This will be shown if no slug is passed(eg: http://127.0.0.1:8000/shop )

        '''paginator code lines'''
    paginator = Paginator(products_list, 6)
    page_no = request.GET.get('raj', '1') #if 1 is not used it will stay in the same page.
    #This line is used as if invalid format is passed in url it will give page 1.
    #value of raj will come from the category.html page.
    try:
        products = paginator.page(page_no)
    except(EmptyPage,InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request,'shop/category.html',{'category':any_var,'products':products})


def ProdCatDetail(request,browser_slug,Prod_slug):
    try:
        product=Product.objects.get(category__slug=browser_slug,slug=Prod_slug)
    except Exception as e:
        raise e
    return render(request,'shop/product.html',{'product':product})