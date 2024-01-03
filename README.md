"# tenants_test" 

Property Management System
Overview
This is a Property Management System built with Django that helps manage properties, units within properties, and tenants residing in these units. The system allows users to perform various tasks like creating properties, adding units, assigning tenants to units, and managing tenant profiles.

Features
Create Property: Users can add new properties with details such as name, address, and location.
Add Units: For each property, users can add different types of units (1BHK, 2BHK, etc.) with associated rent costs.
Manage Tenants: Tenant profiles can be created and assigned to specific units within properties. Each tenant profile contains details like name, address, and document proof.
View Property Details: Provides an overview of properties, their addresses, and locations. Users can also view assigned units and associated tenants.



cd property-management-system
python manage.py makemigrations
python manage.py migrate
