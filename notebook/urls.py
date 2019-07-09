from django.urls import path
from notebook import views

urlpatterns = [
    path('', views.history, name='history'),
    path('transaction/', views.transaction, name='transaction')
    # path('<int:pk>/', views.detail, name='detail')
]