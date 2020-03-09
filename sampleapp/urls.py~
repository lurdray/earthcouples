from django.conf.urls import url
from django.urls import path
from . import views

app_name = "sampleapp"

urlpatterns = [
	path("", views.indexView, name='index'),
	path("register/", views.enquire, name='enquire'),
	path("verify/", views.verify, name='verify'),
	path("about/", views.about, name='about'),
	
	#url(r'^(?P<enquiry_id>[0-9]+)/$', views.detail, name='detail'),
	#url(r'^(?P<enquiry_id>[0-9]+)/respond/$', views.respond, name='respond'),
	#path("dashboard", views.dashboard, name='dashboard'),
	

]

