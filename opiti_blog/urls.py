from django.urls import path 
from opiti_blog import views

urlpatterns = [
	path('contacts/', views.ListContacts.as_view()),
	path('contacts/<int:pk>/', views.ContactDetail.as_view()),
	# wits acms urls
	path('respondents/', views.ListLocationData.as_view()),
	path('respondents/<int:pk>/', views.LocationDetail.as_view())
]