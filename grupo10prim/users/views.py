from django.shortcuts import render


# Create your views here.
def registrar_usuario(request):
    print("Jola")
    return render(request, 'registrar_usuario.html')


def recuperar_registro(request):
    print("test")
    name = request.POST["input_name"]
    last_name = request.POST["input_last_name"]
    rut = request.POST["input_rut"]
    email = request.POST["input_mail"]
    diccionario = {"nombre": name, "apellido": last_name, "rut": rut, "email": email}
    print("ayuda")
    print(diccionario)
    return render(request, 'mostrar_resultado.html', diccionario)
