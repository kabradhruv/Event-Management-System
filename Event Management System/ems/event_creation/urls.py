from django.urls import path
from . import views

app_name = 'event_creation'

urlpatterns = [
    path('dashboard/<int:event_id>/', views.dashboard_ec, name='dashboard_ec'),
    path('start_flow/<int:event_id>/', views.start_flow, name='start_flow'),
    path('category_flow/<int:event_id>/<str:category_name>/', views.category_flow, name='category_flow'),
    path('summary/<int:event_id>/', views.summary, name='summary'),
    path('quotation/<int:event_id>/', views.quotation, name='quotation'),
    path('generate_ppt/<int:event_id>/', views.generate_ppt, name='generate_ppt'),
]