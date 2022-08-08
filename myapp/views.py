from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def api(request):
    teste = request.GET["teste"]
    return HttpResponse(f"Buscando algo da URL do parametro teste = {teste}")