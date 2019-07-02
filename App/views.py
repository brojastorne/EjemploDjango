from django.shortcuts import render
from django.http import HttpResponse
from .models import Person


# Create your views here.

def index(request):
	context = {}
	return render(request, 'plantillas/home.html', context)

def listado(request):
	datos = Person.objects.all()
	context = {'datos': datos}
	return render(request, 'plantillas/listado.html', context)

def contacto(request):
	if request.method == 'POST':
		nom = request.POST.get('nombre')
		ape = request.POST.get('apellido')
		persona = Person()
		persona.first_name = nom
		persona.last_name = ape
		persona.save()

		return HttpResponse("datos: {nom}, {ape}".format(nom = nom, ape = ape))

	return HttpResponse("Te estoy vigilando")

def clinicas(request):
	return HttpResponse("Terrible de clinicas veteras Web's")
