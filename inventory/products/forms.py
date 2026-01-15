from django import forms

from .models import product

class product_form(forms.ModelForm):
    class Meta:
        model = product
        fields = [
            'Product_no',
            'Product_name',
            'Product_type',
            'qty'
        ]
    
    #data validation
    def clean(self):
        cleaned_data = self.cleaned_data
        Product_no = cleaned_data.get('Product_no')
        Product_name = cleaned_data.get('Product_name')
        Product_type = cleaned_data.get('Product_type')
        qty = cleaned_data.get('qty')

        qs = about.objects.filter(Product_no = Product_no)
        if qs.exists():
            self.add_error('Product-', f"\"{Product_no} \"is already present, please pick a unique Product number")

        
# class old_about_form(forms.Form):
#     tittle = forms.CharField()
#     content = forms.CharField() 

#     # def clean_title(self):
#     #     cleaned_data = self.cleaned_data
#     #     tittle = cleaned_data.get('tittle')
#     #     return tittle

#     def clean(self):
#         cleaned_data = self.cleaned_data
#         tittle = cleaned_data.get('tittle')
#         content = cleaned_data.get('content')
#         if "office" in content or "office" in tittle.lower():
#             #adding error comments to fields
#             self.add_error('tittle', 'Tittle Taken')
#             self.add_error('content', 'Content Taken')
#             #adding error comments to form
#             raise forms.ValidationError("Taken")
#         return cleaned_data    