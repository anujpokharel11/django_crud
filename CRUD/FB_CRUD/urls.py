from django.urls import path
from . import views

urlpatterns = [
    path('',views.add_show,name='add_show'),
    path('delete/<int:id>/',views.delete,name='delete'), # <int:id> => this gives id when delete button press.
    path('edit/<int:id>/', views.edit, name='edit'),  
]