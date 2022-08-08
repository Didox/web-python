from django.http import HttpResponse
from django.http import JsonResponse
import json

def index(request):
    try:
        teste = request.GET["teste"]
    except:
        teste = "vazio"

    headers = request.headers
    cookie = request.headers['Cookie']
    
    print("===================")
    print(headers)
    print("===================")
    print(cookie)
    print("===================")

    return HttpResponse(f"Buscando algo da URL do parametro teste = {teste}")

def api(request):
    response_data = {}
    response_data["nome"] = "Danilo"
    response_data["sobrenome"] = "Aparecido"
    response_data["site"] = "https://www.torneseumprogramador.com.br"

    return HttpResponse(json.dumps(response_data), content_type="application/json")

def api2(request):
    response_data = {}
    response_data["nome"] = "Danilo"
    response_data["sobrenome"] = "Aparecido"
    response_data["site"] = "https://www.torneseumprogramador.com.br"

    return JsonResponse(response_data)