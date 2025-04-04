from . import  views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('club/<int:club_id>/', views.club_detail, name='club_detail'),
    path('news/<int:id>', views.news,name='news'),
    path('accreditation/', views.accreditation, name='accreditation'),   

   
]
