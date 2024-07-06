from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item', 'quantidade']
        widgets = {
            'item': forms.TextInput(attrs={
                'class':'form-control d-inline', 
                'placeholder': 'Item',
                'style' : 'width: 400px; margin-right: 10px; display: inline-block;'
                }),
            'quantidade': forms.NumberInput(attrs={
                'class': 'form-control d-inline', 
                'placeholder': 'Quantidade',
                'style' : 'width: 100px; margin-right: 10px;'
                }),
        }