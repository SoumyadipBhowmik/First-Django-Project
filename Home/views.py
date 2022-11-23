from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
def menu(request):
    return render(request, 'menu.html')
def takeaway(request):
    return render(request, 'takeaway.html')
def book(request):
    return render(request, 'book.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        review = request.POST.get('desc')
        contact = Contact(name = name, email = email, review = review, date = datetime.today())
        contact.save()
        messages.success(request, 'Profile details updated.')
    return render(request, 'contact.html')