from django import forms
from .models import Restaurant #?

from inventory.models import Restaurant

class PostForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = ('name', 'description', 'priceLevel', 'category', 'address', 'rating')




