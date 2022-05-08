
from django.contrib import admin
from django.urls import path
from event import views
from django.contrib.auth.views import LogoutView,LoginView
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),


    path('customer/',include('customer.urls')),
    path('',views.home_view,name=''),
    path('logout', LogoutView.as_view(template_name='event/logout.html'),name='logout'),
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),

    
    path('adminlogin', LoginView.as_view(template_name='event/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('admin-view-customer', views.admin_view_customer_view,name='admin-view-customer'),
    path('update-customer/<int:pk>', views.update_customer_view,name='update-customer'),
    path('delete-customer/<int:pk>', views.delete_customer_view,name='delete-customer'),

    path('admin-category', views.admin_category_view,name='admin-category'),
    path('admin-view-category', views.admin_view_category_view,name='admin-view-category'),
    path('admin-update-category', views.admin_update_category_view,name='admin-update-category'),
    path('update-category/<int:pk>', views.update_category_view,name='update-category'),
    path('admin-add-category', views.admin_add_category_view,name='admin-add-category'),
    path('admin-delete-category', views.admin_delete_category_view,name='admin-delete-category'),
    path('delete-category/<int:pk>', views.delete_category_view,name='delete-category'),


    path('admin-event', views.admin_event_view,name='admin-event'),
    path('admin-add-event', views.admin_add_event_view,name='admin-add-event'),
    path('admin-view-event', views.admin_view_event_view,name='admin-view-event'),
    path('admin-update-event', views.admin_update_event_view,name='admin-update-event'),
    path('update-event/<int:pk>', views.update_event_view,name='update-event'),
    path('admin-delete-event', views.admin_delete_event_view,name='admin-delete-event'),
    path('delete-event/<int:pk>', views.delete_event_view,name='delete-event'),

    path('admin-view-event-holder', views.admin_view_event_holder_view,name='admin-view-event-holder'),
    path('admin-view-approved-event-holder', views.admin_view_approved_event_holder_view,name='admin-view-approved-event-holder'),
    path('admin-view-disapproved-event-holder', views.admin_view_disapproved_event_holder_view,name='admin-view-disapproved-event-holder'),
    path('admin-view-waiting-event-holder', views.admin_view_waiting_event_holder_view,name='admin-view-waiting-event-holder'),
    path('approve-request/<int:pk>', views.approve_request_view,name='approve-request'),
    path('reject-request/<int:pk>', views.disapprove_request_view,name='reject-request'),

    path('admin-question', views.admin_question_view,name='admin-question'),
    path('update-question/<int:pk>', views.update_question_view,name='update-question'),

]
