from .views import CreateProperty, CreateTenantProfileView, CreateUnit, PropertyDetailView,AssignTenantToUnitView, view_property

from django.urls import path,include


urlpatterns = [
    path('', view_property, name='view-property'),
    path('create-property/', CreateProperty.as_view(), name='create-property'),
    path('create-unit/', CreateUnit.as_view(), name='create-unit'),
    path('create-tenant-profile/', CreateTenantProfileView.as_view(), name='create-tenant-profile'),
    path('property/', PropertyDetailView.as_view(), name='property-detail'),
    path('assign-tenant/', AssignTenantToUnitView.as_view(), name='assign-tenant'),
]
