from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Animal

@csrf_exempt
def mensaje(request):
    return HttpResponse("Aquí encontrarás una lista de animales los cuales te pueden gustar. (ojala en el salon esto si me funcione, aaaa)")

@csrf_exempt
def lista_animal(request):
    if request.method == 'GET':
        animales = Animal.objects.all()
        animales_data = [
            {
                'id': animal.id,
                'nombre': animal.nombre,
                'especie': animal.especie,
                'edad': animal.edad,
                'habitat': animal.habitat,
                'descripcion': animal.descripcion
            }
            for animal in animales
        ]
        return JsonResponse(animales_data, safe=False, status=200)
    return HttpResponseNotAllowed(['GET'])

@csrf_exempt
def animal(request, id):
    if request.method == 'GET':
        animal = Animal.objects.filter(id=id).first()
        if not animal:
            return JsonResponse({'error': 'Animal no encontrado'}, status=404)
        return JsonResponse({
            'id': animal.id,
            'nombre': animal.nombre,
            'especie': animal.especie,
            'edad': animal.edad,
            'habitat': animal.habitat,
            'descripcion': animal.descripcion
        }, status=200)
    return HttpResponseNotAllowed(['GET'])

@csrf_exempt
def crear(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nuevo_animal = Animal(**{k: data.get(k) for k in ['nombre', 'especie', 'edad', 'habitat', 'descripcion']})
        nuevo_animal.save()
        return JsonResponse({'mensaje':'Se creo un nuevo animal'}, status=201)
    return HttpResponseNotAllowed(['POST'])

@csrf_exempt
def actualizar(request, id):
    if request.method == 'PUT':
        animal = Animal.objects.filter(id=id).first()
        if not animal:
            return JsonResponse({'error': 'Animal no encontrado'}, status=404)
        data = json.loads(request.body)
        for field in ['nombre', 'especie', 'edad', 'habitat', 'descripcion']:
            if field in data:
                setattr(animal, field, data[field])
        animal.save()
        return JsonResponse({'mensaje': 'Se actualizo un animal'}, status=200)
    return HttpResponseNotAllowed(['PUT'])

@csrf_exempt
def eliminar(request, id):
    if request.method == 'DELETE':
        animal = Animal.objects.filter(id=id).first()
        if not animal:
            return JsonResponse({'error': 'Animal no encontrado'}, status=404)
        animal.delete()
        return JsonResponse({'mensaje': 'Se elimino un animal'}, status=200)
    return HttpResponseNotAllowed(['DELETE'])
