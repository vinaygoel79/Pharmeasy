from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_detail, name='login_detail'),
    path('login/loginRequest', views.login_request, name='login_request'),
    path('logout/', views.logout_detail, name='logout_detail'),
	path('doctor/<int:doctor_id>/', views.doctor_details, name='doctor_details'),
	path('doctor/', views.all_doctor_details, name='all_doctor_details'),
	path('patient/<int:patient_id>/', views.patient_details, name='patient_details'),
	path('patient/<int:patient_id>/RequestMethod', views.patient_details_request, name='patient_details_request'),
	path('patient/<int:patient_id>/Request', views.view_all_permission_requests, name='view_all_permission_requests'),
	path('doctor/<int:doctor_id>/Request', views.view_all_doctor_requests, name='view_all_doctor_requests'),
	path('patient/<int:patient_id>/MH', views.patient_MH_details, name='patient_MH_details'),
	path('patient/<int:patient_id>/Pres', views.patient_Pres_details, name='patient_Pres_details'),
	path('medicine/<int:medicine_id>/', views.medicine_details, name='medicine_details'),
	path('pharmacist/<int:pharmacist_id>/', views.pharmacist_details, name='pharmacist_details'),
	path('prescription/<int:prescription_id>/', views.prescription_details, name='prescription_details'),
]
