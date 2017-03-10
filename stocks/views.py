# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import render
from .models import Stock

def list(request ):
	latest_stock_list = Stock.objects.order_by('-create_date')[:5]
	context = {
    	'latest_stock_list' : latest_stock_list,
    }
	return render(request,'stocks/index.html',context)

def detail(request, stock_id):
	try:
		stock = Stock.objects.get(number=stock_id)
	except Stock.DoesNotExist:
		raise Http404("Stock does not exist")
	return render(request, 'stocks/detail.html', {'stock_name': stock.name})