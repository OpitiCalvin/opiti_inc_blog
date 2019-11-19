from django.urls import path 
from opiti_blog import views

urlpatterns = [
	path('contacts/', views.ListContacts.as_view()),
	path('contacts/<int:pk>/', views.ContactDetail.as_view())
]