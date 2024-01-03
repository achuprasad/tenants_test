from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.http import HttpResponse
from .models import  Person, Property, TenantProfile, Unit ,Tenant
from django.contrib.auth import authenticate, login
# Create your views here.

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('/')  
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

class CreateProperty(View):

    def get(self,request):
        
        return render(request, 'create_prop.html')
    def post(self, request):
        context = {}
        req_type = request.POST.get('type')
        if req_type == 'create_prop':
            prop_name = request.POST.get('name')
            prop_address = request.POST.get('address')
            prop_location = request.POST.get('location')
            prop = Property.objects.get_or_create(name=prop_name, address=prop_address, location= prop_location)
            all_props = Property.objects.all().order_by('-id')
            context['props'] = all_props
        return redirect('/')

def view_property(request):   
    context = {}
    all_props = Property.objects.all().order_by('-id')
    context['props'] = all_props
    return render(request, 'prop_list.html', context)

class CreateUnit(View):
    def get(self, request):
        context = {}
        prop_id = request.GET.get('prop_id')
        prop_obj = Property.objects.get(id=prop_id)
        context['prop']=prop_obj
        return render(request, 'create_unit.html',context)
    def post(self, request):
        try:
            prop_id = request.POST.get('prop')
            rent = request.POST.get('rent')
            unit_type = request.POST.get('unit_type')
            prop_obj = get_object_or_404(Property, id=prop_id)
            unit = Unit.objects.create(property=prop_obj, unit_type=unit_type, rent_cost=rent)
            return redirect('/')
        except Exception as e:
           ...



class CreateTenantProfileView(View):
    def get(self, request):
        context={}
        tenantProfile = TenantProfile.objects.all()
        context['tenantProfile'] = tenantProfile

        return render(request, 'create_tenant.html',context)

    def post(self, request):
        try:
            name = request.POST.get('name')
            address = request.POST.get('address')
            document_type = request.POST.get('document_type')
            document_proof = request.FILES.get('document_proof') 

            tenant_profile = TenantProfile.objects.create(
                name=name,
                address=address,
                document_type=document_type,
                document_proof=document_proof
            )
            return redirect('/create-tenant-profile/')
            
        except Exception as e:
            print('-------',e)


class PropertyDetailView(View):
    def get(self, request):
        
        context = {}
        property_id = request.GET.get('prop_id')
        property_obj = get_object_or_404(Property, id=property_id)
        
        units = property_obj.units.all()

        context['property'] = property_obj
        context['units'] = units
        context['tenants'] = [unit.tenants.all() for unit in units]

        return render(request, 'property_detail.html', context)
    


class AssignTenantToUnitView(View):
    def post(self, request):
        try:
            print(request.POST.dict())
            tenant_id = request.POST.get('tenant_id')
            unit_id = request.POST.get('unit_id')

            tenant = get_object_or_404(Tenant, id=tenant_id)
            unit = get_object_or_404(Unit, id=unit_id)

            unit.tenant = tenant
            unit.save()

            print("Tenant assigned successfully")
            return redirect('/')
        except Exception as e:
            return HttpResponse("Error assigning tenant to unit: " + str(e))