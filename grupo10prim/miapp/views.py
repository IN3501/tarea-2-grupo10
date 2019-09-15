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


def homeEmpresa(request):
    return render(request, 'homeEmpresa.html')


def fichaClinica(request):
    return render(request, 'fichaClinica.html')


def estadisticas(request):
    return render(request, 'estadisticas.html')


def inventario(request):
    return render(request, 'inventario.html')


def comprarObjeto(request):
    return render(request, 'comprarObjeto.html')

def agendaReg(request):
    return render(request, 'agendaReg.html')

def recuperar(request):
    diccionario = {}

    name1 = request.POST.get("inputComida1")
    if (name1):
        diccionario["Bebestible"] = "Bebestible"

    name2 = request.POST.get("inputComida2")
    if (name2):
        diccionario["Snack"] = "Snack"

    name3 = request.POST.get("inputComida3")
    if (name3):
        diccionario["Cena"] = "Cena"

    return render(request, "mostrar_resultado.html", diccionario)
