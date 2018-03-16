from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import *

# Create your views here.
login=10

def login_detail(request):
	return render(request, 'website/login.html')

def login_request(request):
	return HttpResponse('Successful')

def logout_detail(request):
	return redirect('login_detail')

def all_doctor_details(request):
    doctor_list = Doctor.objects.all()[:5]
    context = {'doctor_list': doctor_list}
    print(context)
    return render(request, 'website/all_doctor_details.html', context)


def doctor_details(request, doctor_id):
    try:
        doctor = Doctor.objects.get(pk=doctor_id)
    except Doctor.DoesNotExist:
        raise Http404("Couldn't find the doctor")
    return render(request, 'website/doctor_details.html', {'doctor': doctor})


def index(request):
    return HttpResponse('Hello World!')


def patient_details(request, patient_id):
    try:
        patient = Patient.objects.get(pk=patient_id)
    except Patient.DoesNotExist:
        raise Http404("Couldn't find the doctor")
    return render(request, 'website/patient_details.html', {'patient': patient})

def patient_details_request(request, patient_id):
    permission_id = request.POST['permission_id']
    if request.method == 'POST':
        if request.POST.__contains__('Approve'):
            Permission.objects.filter(pk=permission_id).update(pending=False, approved=True)
        elif request.POST.__contains__('Decline'):
            Permission.objects.filter(pk=permission_id).update(pending=False)   
    return redirect('patient_details',patient_id=patient_id)

def patient_MH_details(request, patient_id):
    try:
        history = MedicalHistory.objects.filter(patient__pk=patient_id)
    except MedicalHistory.DoesNotExist:
        raise Http404("Couldn't find the Medical History")
    return render(request, 'website/patient_MH_details.html', {'patient': history[0].patient.name, 'history': history, 'lg':login})

def patient_Pres_details(request, patient_id):
    try:
        prescript = Prescription.objects.filter(patient__pk=patient_id)
        print(type(prescript[0].medicine))
    except Prescription.DoesNotExist:
        raise Http404("Couldn't find the doctor's Prescription")
    return render(request, 'website/patient_Pres_details.html', {'patient': prescript[0].patient.name, 'prescript': prescript, 'lg':login})

def pharmacist_details(request, pharmacist_id):
    return HttpResponse("You're looking at Pharmacist %s." % pharmacist_id)


def prescription_details(request, prescription_id):
    return HttpResponse("You're looking for Doctor's prescription %s." % prescription_id)


def medicine_details(request, medicine_id):
    return HttpResponse("You're looking for Medicine %s." % medicine_id)
    
def create_new_permission(request, doctor_id, patient_id, resource_id, resource_type):
    new_object = Permission(patient=Patient.objects.get(pk=patient_id), doctor=Doctor.objects.get(pk=doctor_id), resourceId=resource_id, resourceType=resource_type)
    return HttpResponse("OK")
    
def view_all_permission_requests(request, patient_id):
    all_requests = Permission.objects.filter(patient__pk=patient_id, pending=True)
    context = { 'requests_list': all_requests }
    return render(request, 'website/view_my_requests.html', context)

def view_all_doctor_requests(request, doctor_id):
    all_requests = Permission.objects.filter(patient__pk=doctor_id, pending=True)
    context = { 'requests_list': all_requests }
    return render(request, 'website/view_all_my_doctor_requests.html', context)

    
def check_status_doctor(request, doctor_id):
    all_requests = Permission.objects.filter(doctor__pk=doctor_id)
    approved_requests = all_requests.objects.filter(approved=True)
    declined_requests = all_requests.objects.filter(pending=False, approved=False)
    pending_requests = all_requests.objects.filter(pending=True)
    context = { 'approved_requests': approved_requests, 'declined_requests': declined_requests, 'pending_requests': pending_requests }
    return render(request, 'website/view_my_requests_status.html', context)
    

