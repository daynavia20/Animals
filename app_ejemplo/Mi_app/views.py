from django.http import HttpResponse,JsonResponse,HttpResponseBadRequest
from .models import Ejemplo
import json
from django.views.decorators.csrf import csrf_exempt

def mi_vista(request):
    return HttpResponse("Hola, soy dayana y este es un mensaje para verlo por medio de una url, gracias")

def ver_mensajes(request):
    mensajes = Ejemplo.objects.all() #tiene los mensajes anteriores
    mensajes_data = [{'id': mensaje.id, 'texto': mensaje.texto} for mensaje in mensajes]
    return JsonResponse(mensajes_data, safe=False, status=200)

def mensaje_actualizado(request):
    ultimo_mensaje = Ejemplo.objects.last()# tienes los datos de la base de datos
    if ultimo_mensaje:
        return JsonResponse({'texto': ultimo_mensaje.texto}, status=200)
    return JsonResponse({'error': 'No hay mensajes.'}, status=404)

@csrf_exempt
def crear_mensaje(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        texto = data.get('texto')
        if not texto:
            return HttpResponseBadRequest("El mensaje no puede estar vacío.")
        Ejemplo.objects.create(texto=texto)  
        return JsonResponse({'mensaje':'Se creo un nuevo mensaje'}, status=201)
    return HttpResponseBadRequest("Método no permitido")
