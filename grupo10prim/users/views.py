from django.shortcuts import render


# Create your views here.
def registrar_usuario(request):
    return render(request, 'registrar_usuario.html')


def recuperar_registro(request):
    def recuperar(request):
        diccionario = {}
        edad = request.POST["inputEdad"]
        email = request.POST["inputEmail"]

        diccionario["Edad"] = edad
        diccionario["email"] = email

        return render(request, "mostrar_resultado.html", diccionario)
