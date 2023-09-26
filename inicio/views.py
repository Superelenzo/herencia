from django.shortcuts import render
from datetime import datetime
from inicio.models import Curso

# Create your views here.

def inicio(request):
    datos= {
        'fecha': datetime.now()
    }    
    return render(request, r'inicio\inicio.html', datos)
def crear_curso(request,titulo,numero):
    curso = Curso(titulo = titulo, numero=numero)
    curso.save()
    
    return(render(request, r'inicio\curso_creado.html', {}))
 