from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Couple
from datetime import date
from django.core.mail import send_mail

# Create your views here.

def indexView(request):
	return render(request, "sampleapp/index.html")

def service(request):
	return render(request, "sampleapp/index.html")

def about(request):
	return render(request, "sampleapp/index.html")
 

def enquire(request):
	if request.method == "POST":
		#get the details of enquiry
		name1 = request.POST["name1"]
		name2 = request.POST["name2"]
		email = request.POST["email"]
		comment = request.POST["comment"]
		phone = request.POST["phone"]
		#subject = request.POST["subject"]
		date_today = date.today()

		#create the enquiry
		#enquirer = Enquirer.objects.create(name=name, email=email, phone=phone)
		couple = Couple.objects.create(hus_name=name1, wife_name=name2, email=email, phone=phone, comment=comment, pub_date=date_today)
		couple.save()
		
		#couple_id = Couple.objects.get(i)
		#couple_id = Couple.objects.order_by("-pub_date")[0]
		msg = "Please note down your union id: %s" % (couple.id)
		return HttpResponse(msg)
		return HttpResponseRedirect(reverse("sampleapp:index"))

	else:
		#load the enquiry page
		return render(request, "sampleapp/register.html")
		
		
def verify(request):
	union_id = request.POST["union_id"]
	
	try:
		couple = Couple.objects.get(id=union_id)
		#return HttpResponse(couple)
		context = {"couple":couple}
		return render(request, "sampleapp/verify.html", context)
		
	except:
		return HttpResponse("union id not found")
	
	
	
	
	
		

def dashboard(request):
	enquiry = Enquiry.objects.order_by("-pub_date")
	context = {"enquiry": enquiry}
		
	return render(request, "sampleapp/dashboard.html", context)

def detail(request, enquiry_id):
	enquiry = Enquiry.objects.get(pk=enquiry_id)
	context = {"enquiry": enquiry}
		
	return render(request, "sampleapp/detail.html", context)

def respond(request, enquiry_id):
	response = request.POST["response"]
	enquiry = Enquiry.objects.get(pk=enquiry_id)
	enquirer_email = (enquiry.enquirer.email)
	email_list = []
	email_list.append(enquirer_email)
	
	Response.objects.create(enquiry=enquiry, response=response)
	subject = "Response to you enquiry"
	app_email = "app@email.com"
	
	send_mail(
		subject,
		response,
		app_email,
		email_list,
		fail_silently=False,
		)

	return HttpResponseRedirect(reverse("sampleapp:dashboard"))
	
