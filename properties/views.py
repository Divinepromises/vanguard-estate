from django.shortcuts import render, get_object_or_404
from .models import Property
from django.db.models import Q

# Create your views here.

def home(request):
    # Fetch all properties that are marked as available
    properties = Property.objects.filter(is_available=True)
    
    # Pass the properties database records to the HTML template
    context = {
        'properties': properties
    }
    
    return render(request, 'index.html', context)

def properties(request):
    # 1. Grab whatever text the user typed into the search box
    search_query = request.GET.get('search', '')
    dropdown_filter = request.GET.get('property_type', '')  # Get the selected property type from the dropdown
    # 2. Start with all available properties
    properties = Property.objects.filter(is_available=True)

    # 3. If the user searched for something, filter by location OR title
    if search_query:
        properties = properties.filter(
            Q(area__icontains=search_query) | Q(state__icontains=search_query)
        )
    if dropdown_filter:
        properties = properties.filter(property_type=dropdown_filter)
  
    # Pass the properties database records to the HTML template
    context = {
        'properties': properties,
        'property_types': Property.PROPERTY_TYPES,  # Pass the property types to the template
    }
    
    return render(request, 'properties.html', context)

# View function to show a single property's details
def property_detail(request, pk):
    # Fetch the exact house by its Primary Key (ID), or show a 404 Error page if not found
    property_item = get_object_or_404(Property, pk=pk)
    
    context = {
        'property': property_item
    }
    
    return render(request, 'property_detail.html', context)

def philosophies(request):
    return render(request, 'philosophies.html')

def contact(request):
    return render(request, 'contact.html')