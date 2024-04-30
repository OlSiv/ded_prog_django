from django.shortcuts import render
from my_app.models import Worker   


def index_page(request):
	all_workers = Worker.objects.all()   
	print(all_workers)   

	workers_filtered = Worker.objects.filter(salary=5000)   ### new
	print(workers_filtered)   ### new
	
	return render(request, 'index.html')
	
	
def about_page(request):
	return render(request, 'about.html')

