from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Room, Program, AddIcon, SelectIcon, Bdcpf 
import json

from allauth.account.views import SignupView, PasswordResetDoneView


#not in use at the moment

lista_bd = Bdcpf.objects.all()
lista_cpf = []
for item in lista_bd:
    lista_cpf.append(item.cpfbd)


def menuView(request): 
    if not request.user.is_authenticated:
        return redirect('/') 

    if request.user.last_name not in lista_cpf: 

        if request.user.is_superuser:
            pass
        else:
            user_data = [request.user.username, request.user.last_name] 
            request.user.delete()
            return redirect('/cpf-invalido/')
    

    event = Event.objects.all()[0]
    event_name = event.slug
    
    #dar uma olhada na linha abaixo depois (apenas rooms da sapiens)
    rooms = Room.objects.all()
    
    return render(request, 'hall.html', {'event':event, 'rooms':rooms, 'slug':event_name})


    #slug2 é o slug da sala
def daysView(request, slug1, slug2):

    if not request.user.is_authenticated:
        return redirect('/')

    event = Event.objects.all()[0]

    #sala específica que a pessoa entrou
    sala = get_object_or_404(Room, slug=slug2) 

    
    rooms = Room.objects.all()
    
    sala_days= [x for x in range(1, event.days+1)]

    if sala.days == 1:
        return redirect(roomsGenericView, slug1, slug2, 'unico')

    return render(request, 'days.html', { "sala_days":sala_days, "room":sala, 'event':event, 'rooms':rooms})

#slug3 é o dia
def roomsGenericView(request, slug1, slug2, slug3):

    if not request.user.is_authenticated:
        return redirect('/')


    event = Event.objects.all()[0]

    sala = get_object_or_404(Room, slug=slug2)

    #Apenas programas da sala específica
    #Se não for dia único ele pega os programas específicos por dia
    #Se for dia único, ele pega apenas o programa daquela sala
    if slug3 == 'unico':
        room_programs = Program.objects.filter(room=sala.id)
    else:
        room_programs = Program.objects.filter(room=sala.id, day =slug3)
    


    #dar uma olhada na linha abaixo depois (apenas rooms da sapiens)
    rooms = Room.objects.all()

    return render(request, 'rooms.html', { 'event':event, 'programs': room_programs, 'room':sala, 'rooms':rooms})

#slug1 is the event
def padletView(request, slug1):
    if not request.user.is_authenticated:
        return redirect('/')

    rooms = Room.objects.all()
    event = Event.objects.all()[0] 


    return render(request, 'padlet.html', {'event':event, 'rooms':rooms, 'slug1':slug1})


def desopilarView(request, slug1):
    if not request.user.is_authenticated:
        return redirect('/')

    event = Event.objects.all()[0]
    rooms = Room.objects.all()  

    return render(request, 'desopilar.html', {'event': event, 'rooms':rooms, 'slug1':slug1})

def programacaoView(request, slug1):
    if not request.user.is_authenticated:
        return redirect('/')

    event = Event.objects.all()[0]
    rooms = Room.objects.all()  

    return render(request, 'programacao.html', {'event': event, 'rooms':rooms, 'slug1':slug1})


def cpfinvalido(request):

    return render(request, 'cpf_invalido.html', {})


"""def passwordSent(request):

    return redirect("/")"""



