from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Property
from django.db.models import Q

# How many properties to show on each page of the Properties page.
# 6 = three rows in the two-column grid.
PROPERTIES_PER_PAGE = 6

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
    # 2. Start with all available properties.
    #    order_by is required for pagination: without a fixed order the database
    #    may return rows in a different order on each request, so items could
    #    repeat or go missing between pages. '-pk' = newest first.
    properties = Property.objects.filter(is_available=True).order_by('-pk')

    # 3. If the user searched for something, filter by location OR title
    if search_query:
        properties = properties.filter(
            Q(area__icontains=search_query) | Q(state__icontains=search_query)
        )
    if dropdown_filter:
        properties = properties.filter(property_type=dropdown_filter)

    # 4. Split the (already filtered) results into pages
    paginator = Paginator(properties, PROPERTIES_PER_PAGE)
    page_number = request.GET.get('page')       # the "2" in /properties/?page=2
    # get_page() never crashes: a missing, non-numeric or out-of-range
    # number falls back to the first / last page instead of an error.
    page_obj = paginator.get_page(page_number)

    # 5. Page links must keep the user's search and filter, so rebuild the
    #    query string from the current URL, minus 'page' (each link adds its own).
    query_params = request.GET.copy()
    query_params.pop('page', None)

    # 6. For a long list, show "1 ... 4 5 6 ... 20" instead of every page number
    page_range = paginator.get_elided_page_range(
        page_obj.number, on_each_side=1, on_ends=1
    )
  
    # Pass the properties database records to the HTML template
    context = {
        'properties': page_obj,   # the template loops over this: only this page's items
        'page_obj': page_obj,     # page info for the pagination bar (has_next, number, ...)
        'page_range': page_range,
        'query_string': query_params.urlencode(),
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