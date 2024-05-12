from django.shortcuts import render
from my_app.models import Worker   


def index_page(request):

	#  my_dict = {'data1': 'Tru-lu-la-', 'data2': 'La-la-la'} 

	all_workers = Worker.objects.all()   
	print(all_workers)   
	
	return render(request, 'index.html', {'data1': all_workers})
	

def about_page(request):
	return render(request, 'about.html')
