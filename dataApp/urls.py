from django.urls import path
from dataApp import views

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('ticker-list/', views.tickerList, name='tickerList'),
    path('ticker-detail/<str:pk>', views.tickerDetail, name='tickerDetail'),
    path('ticker-create/', views.tickerCreate, name='tickerCreate'),
    path('ticker-update/<str:pk>', views.tickerUpdate, name='tickerUpdate'),
    path('ticker-delete/<str:pk>', views.tickerDelete, name='tickerDelete'),
]
