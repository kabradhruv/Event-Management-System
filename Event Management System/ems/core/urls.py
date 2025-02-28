from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views,views_ssp,views_group_event,views_vendor
from django.contrib.auth import views as auth_views

urlpatterns = [

    # Auth URLs
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Reusable views 
    path('get_events/<int:group_id>/', views.get_events, name='get_events'), # Get events for a group


    path('', views.home, name='home'),  # Home page

    # URLs for SSP feature 
    path('add_ssp/', views_ssp.add_ssp, name='add_ssp'), # Add SSP to the database
    path('event/sge_ssp/', views_ssp.sge_ssp, name='sge_ssp'), # select a group and event
    path('event/<int:event_id>/ssps/', views_ssp.event_ssp_list, name='event_ssp_list'), # List of SSPs associated with an event
    path('event/<int:event_id>/link_ssps/', views_ssp.link_ssp_to_event, name='link_ssp_to_event'), # Link SSP to an event
    path('event/<int:event_id>/update_ssp_quantity/<int:item_id>/', views_ssp.update_ssp_quantity, name='update_ssp_quantity'),
    path('event/<int:event_id>/remove_ssp/<int:item_id>/', views_ssp.remove_ssp_from_event, name='remove_ssp_from_event'),
    path('events/', views_group_event.groups_dashboard, name='groups_dashboard'),  # Groups Dashboard also Events Dashboard 
    # Listing All ssp and CRUD operations
    path('all_ssps/', views_ssp.all_ssps, name='all_ssps'), # All SSP of Database
    path('update_all_ssps/', views_ssp.update_all_ssps, name='update_all_ssps'),
    path('remove_ssp/<int:ssp_id>/', views_ssp.remove_ssp, name='remove_ssp'),

    # URLs for Group feature
    path('group/add/', views_group_event.add_group, name='add_group'),  # Add New Group
    path('group/<int:group_id>/edit_group_details/', views_group_event.edit_group_details, name='edit_group_details'),  # Manage Group
    path('group/<int:group_id>/manage/', views_group_event.manage_group, name='manage_group'),

    # Event-related URLs
    path('group/<int:group_id>/add_event/', views_group_event.add_event, name='add_event'),
    path('event/<int:event_id>/edit/', views_group_event.edit_event, name='edit_event'),
    path('event/<int:event_id>/manage/', views_group_event.manage_event, name='manage_event'),

    # Vendor related URLs - 
    path('vendor/add/', views_vendor.add_vendor, name='add_vendor'),
    path('vendor/dashboard/', views_vendor.vendor_dashboard, name='vendor_dashboard'),
    path('vendor/sge_vendor', views_vendor.sge_vendor, name='sge_vendor'),
    path('vendor/assign_vendor/', views_vendor.assign_vendor, name='assign_vendor'),
    path('vendor/<int:vendor_id>/edit_vendor/', views_vendor.edit_vendor, name='edit_vendor'),
    path("vendor/manage_assignment/<int:assignment_id>/", views_vendor.manage_assignment, name="manage_assignment"),
    path("vendor/assignment_detail/<int:vendor_id>/", views_vendor.assignment_detail, name="assignment_detail"),
    path("vendor/record_payment/<int:assignment_id>/", views_vendor.record_payment, name="record_payment"),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)