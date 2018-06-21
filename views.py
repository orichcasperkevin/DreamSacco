from django.shortcuts import render, redirect
from django.contrib import messages
#from .forms import ContactForm



from .models import Contact


def index(request):
     return render(request, 'home/index.html')


def index3(request):
     return render(request, 'home/index3.html')


def about(request):
     return render(request,'home/about.html')


def portfolio(request):
     return render(request, 'home/portfolio.html')


def pricing(request):
     return render(request, 'home/pricing.html')


def services(request):
     return render(request, 'home/services.html')


def contact(request):

     if request.method == 'post':
          if request.POST.get('name') and request.POST.get('email') and request.POST.get('message'):
               post = Contact()
               post.name = request.POST.get('name')
               post.email = request.POST.get('email')
               post.message = request.POST.get('message')
               post.save()
               messages.success(request, "Thanks for your message, we'll get intouch")
               return render(request, 'home/contact.html')

     else:
         # form = ContactForm()
          #args = {'form': form}
          return render(request, 'home/contact.html')