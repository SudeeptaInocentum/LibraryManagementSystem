from django.urls import path
from .views import *

urlpatterns = [
    path('building/', BuildingList.as_view()),
    path('building/<int:id>/', BuildingDetails.as_view()),

    path('department/', DepartmentList.as_view()),
    path('department/<int:id>/', DepartmentDetails.as_view()),

    path('section/', SectionList.as_view()),
    path('section/<int:id>/', SectionDetails.as_view()),

    path('books/', BookList.as_view()),
    path('books/<int:id>/', BookDetails.as_view()),

    path('libadmin/', AdminList.as_view()),
    path('libadmin/<int:id>/', AdminDetails.as_view()),

    path('user/', UserList.as_view()),
    path('user/<int:id>/', UserDetails.as_view()),

    path('status/', IssuenceList.as_view()),
    path('status/<int:id>/', IssuenceDetails.as_view()),
]