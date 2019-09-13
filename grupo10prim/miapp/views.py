from django.shortcuts import render

# Create your views here.
def homeCliente(request):
	return render(request, 'homeCliente.html')

def inputs(request):
	return render(request, 'inputs.html')

def contacto(request):
	return render(request, 'contacto.html')

def agenda(request):
	return render(request, 'agenda.html')

def catalogo(request):
	return render(request, 'catalogo.html')

def backoffice(request):
	return render(request, 'backoffice.html')


def recuperar(request):
	diccionario={}

	name1 = request.POST.get("inputComida1")
	if (name1):
		diccionario["Bebestible"] = "Bebestible"

	name2 = request.POST.get("inputComida2")
	if (name2):
		diccionario["Snack"] = "Snack"

	name3 = request.POST.get("inputComida3")
	if (name3):
		diccionario["Cena"] = "Cena"

	
	nombre=request.POST["inputNombre"]
	edad=request.POST["inputEdad"]
	email=request.POST["inputEmail"]
	carrera=request.POST["exampleRadios"]
	tema=request.POST["inputTema"]

	diccionario["Nombre"]=nombre
	diccionario["Edad"]=edad
	diccionario["Email"]=email
	diccionario["Departamento"]=carrera
	diccionario["Tematica"]=tema

	return render(request, "mostrar_resultado.html", diccionario)