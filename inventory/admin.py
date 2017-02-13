from django.contrib import admin

# Register your models here.

from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
	list_display = ['name', 'rating']

admin.site.register(Restaurant, RestaurantAdmin)