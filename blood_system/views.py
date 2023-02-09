from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Register_as_Donor, Request_for_blood, Message, Room,Topic
from .forms import ChatForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout 
from django.contrib import messages
from .forms import RegisterForm





def blog(request):
    return render(request, 'blood_system/blog.html')




def home_page(request):
    return render(request, 'blood_system/home.html')




def about_us(request):
    return render(request, 'blood_system/Who We Are.html')



def contact(request):
    return render(request, 'blood_system/Contact.html')





def chat(request):
    
    rooms = Room.objects.all() 
    topics = Topic.objects.all()
    if request.method=='POST':
        topics== Topic.objects.create(
            name= request.POST.get('name'),
        )
        
    room_count = rooms.count()
    room_messages = Message.objects.all()
    context = {'rooms':rooms,'room_count':room_count,   'topics': topics,  'room_messages' : room_messages}
    return render(request, 'blood_system/Chat.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all()
    topics = Topic.objects.all()
    participants = room.participants.all()
    if request.method == 'POST':
        room_messages = Message.objects.create(

            user = request.user,
            room = room,
            body  = request.POST.get('body')
        )
        
        return redirect('room', pk=room.id)
        
        
    context = {'room':room, 'room_messages':room_messages,  'topics':topics, 'participants':participants}
    return render(request, 'blood_system/room.html', context)



def how_it_works(request):
    return render(request, 'blood_system/How it works.html')





def post_request(request):
    if request.method=='POST':
        title = request.POST['title']
        blood_unit = request.POST['blood_unit']
        patient_name = request.POST['patient_name']
        purpose = request.POST['purpose']
        blood_group = request.POST['blood_group']
        mobile_number = request.POST['mobile_number']
        patient_age = request.POST['patient_age']
        hospital_name = request.POST['hospital_name']
        when_need_blood = request.POST['when_need_blood']
        address = request.POST['address']
        details = request.POST['details']

        patient = Request_for_blood(title=title, blood_unit=blood_unit, patient_name=patient_name, purpose=purpose, blood_group=blood_group, mobile_number=mobile_number, patient_age=patient_age, hospital_name=hospital_name, when_need_blood=when_need_blood, address=address, details=details)
        patient.save()
        return redirect('home')
    return render(request, 'blood_system/Post Request.html')





def register(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        date_of_birth = request.POST['date_of_birth']
        age = request.POST['age']
        gender = request.POST['gender']
        email = request.POST['email'] 
        phone = request.POST['phone']
        address = request.POST['address']
        blood_group = request.POST['blood_group']
        sickness = request.POST['sickness']

        donor = Register_as_Donor(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth, age=age, gender=gender, email=email, phone=phone, address=address, blood_group=blood_group, sickness=sickness)
        
        donor.save()
        return redirect ('home')
    return render(request, 'blood_system/Register as Donor.html' )

@login_required(login_url='login')
def create_talk(request):
        form = ChatForm()
        if request.method== 'POST':
            form = ChatForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('chat')
        context = {'form':form}
        return render(request, 'blood_system/Talk.html', context)

@login_required(login_url='login')
def update_talk(request, pk):
    rooms = Room.objects.get(id=pk)
    form = ChatForm(instance=rooms)

    if request.user != rooms.host:
        return HttpResponse('You are not allowed here')

    if request.method == 'POST':
        form = ChatForm(request.POST, instance=rooms)
        if form.is_valid():
                form.save()
        return redirect('chat')

    context = {'form':form}
    return render(request, 'blood_system/Talk.html', context)

@login_required(login_url='login')
def delete_talk(request, pk):
    talk = Room.objects.get(id=pk)

    if request.user != talk.host:
        return HttpResponse('You are not allowed here')


    if request.method == 'POST':
        talk.delete()
        return redirect('chat')
    context = {'talk':talk}
    return render(request, 'blood_system/delete.html', context)


def register_page(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account Successfully Created for '+ user)
        return redirect('login')
    context = {'form':form}
    return render (request, 'blood_system/register.html', context)



def login_page(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password= request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('chat')
            else:
                messages.info(request, 'username OR password incorrect')
                return render(request, 'blood_system/login.html')
    context = {}        
    return render(request, 'blood_system/login.html', context)



def logout_page(request):
    logout(request)
    return redirect('login')




#def delete_message(request, pk):
  #  obj = Message.objects.get(id=pk)
 #   if request.method == 'POST':
  #      obj.delete()
  #      context= {'obj':obj}
  #  return redirect('room')
    
   # return render(request, 'blood_system/delete_message.html', context)
