from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [

    path('hotel/', views.hotel),
    path('show/', views.show),
    path('edit/', views.edit),
    path('update/', views.update),
    path('delete/', views.destroy),

]
