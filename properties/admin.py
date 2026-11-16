from django.contrib import admin
from .models import Property, PropertyMedia


# Register your models here.

# 1. This creates the spreadsheet-style box for multiple photos/videos
class PropertyMediaInline(admin.TabularInline):
    model = PropertyMedia
    extra = 3 # Gives you 3 empty upload rows by default

# 2. This customizes how the main Property page looks
class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyMediaInline] # Injects our photo box right into the property page!
    list_display = ('title', 'property_type', 'price', 'is_available')
    list_filter = ('is_available', 'property_type')
    search_fields = ('title', 'description')

# 3. Register the Property using its custom admin rules
admin.site.register(Property, PropertyAdmin)
