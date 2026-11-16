from django.contrib.auth import admin
from django.db import models

# Create your models here.

# Define the 36 states of Nigeria + FCT
NIGERIA_STATES = [
        ('Abia', 'Abia'),
        ('Adamawa', 'Adamawa'),
        ('Akwa Ibom', 'Akwa Ibom'),
        ('Anambra', 'Anambra'),
        ('Bauchi', 'Bauchi'),
        ('Bayelsa', 'Bayelsa'),
        ('Benue', 'Benue'),
        ('Borno', 'Borno'),
        ('Cross River', 'Cross River'),
        ('Delta', 'Delta'),
        ('Ebonyi', 'Ebonyi'),
        ('Edo', 'Edo'),
        ('Ekiti', 'Ekiti'),
        ('Enugu', 'Enugu'),
        ('FCT', 'Federal Capital Territory'),
        ('Gombe', 'Gombe'),
        ('Imo', 'Imo'),
        ('Jigawa', 'Jigawa'),
        ('Kaduna', 'Kaduna'),
        ('Kano', 'Kano'),
        ('Katsina', 'Katsina'),
        ('Kebbi', 'Kebbi'),
        ('Kogi', 'Kogi'),
        ('Kwara', 'Kwara'),
        ('Lagos', 'Lagos'),
        ('Nasarawa', 'Nasarawa'),
        ('Niger', 'Niger'),
        ('Ogun', 'Ogun'),
        ('Ondo', 'Ondo'),
        ('Osun', 'Osun'),
        ('Oyo', 'Oyo'),
        ('Plateau', 'Plateau'),
        ('Rivers', 'Rivers'),
        ('Sokoto', 'Sokoto'),
        ('Taraba', 'Taraba'),
        ('Yobe', 'Yobe'),
        ('Zamfara', 'Zamfara'),
    ]
class Property(models.Model):
    
    
    title = models.CharField(max_length=255, help_text="Enter the title of the property")
    # LOCATION SPLIT (Area & State)
    area = models.CharField(max_length=100, help_text="e.g. Lekki Phase 1, Victoria Island, Ikeja") # Required
    state = models.CharField(max_length=100,choices=NIGERIA_STATES, default="Lagos") # Required
    
    # Decorative price display (e.g. 150,000,000)
    price = models.DecimalField(max_digits=12, decimal_places=2, help_text="Enter the price of the property")
    
    # Property features
    PROPERTY_TYPES = [
        ('commercial', 'Commercial'),
        ('residential', 'Residential'),
        ('land', 'Land'),
    ]
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPES, help_text="Select the type of property")
    
    #Description and Main Photo
    description = models.TextField(help_text="Enter a description of the property")
    main_image = models.ImageField(upload_to='properties/', help_text="Upload the main image of the property")
   
    # WhatsApp Integration: Agent phone number to receive messages for this property
    whatsapp_number = models.CharField(max_length=15,default='+2340000000000', help_text="Enter the agent's WhatsApp number in international format (e.g. +234XXXXXXXXXX)")
    is_available = models.BooleanField(default=True, help_text="Is the property available for sale?")
    created_at = models.DateTimeField(auto_now_add=True)
    

    
    class Meta:
        verbose_name_plural = "Properties"  # Fixes "Propertys" -> "Properties"

    # 5. Helper function that automatically combines Area and State!
    def full_location(self):
        return f"{self.area}, {self.state}"
    
    def __str__(self):
        return f"{self.title} - {self.full_location()}"  # Fixes "Property object (1)" -> "Mshel Hutu - Guzape"
    
class PropertyMedia(models.Model):
    MEDIA_TYPES = [
        ('image', 'Image'),
        ('video', 'Video')
    ]
    # The Foreign key bridge links every individual photo/video back to one Property
    property = models.ForeignKey(Property, related_name='media_items', on_delete=models.CASCADE)
    file = models.FileField(upload_to='property_media/')
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    
    class Meta:
        verbose_name_plural = "Property Media Files"
    
    def __str__(self):
        return f"{self.property.title} {self.media_type}"
    
    
    
