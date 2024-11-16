from django import forms
from .models import Product, Category, Tag, ProductType


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        labels = {"name": "Category"}
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Category"}
            )
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
        labels = {"name": "Tag"}
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Tag"}
            )
        }


class ProductTypeForm(forms.ModelForm):
    class Meta:
        model = ProductType
        fields = "__all__"
        labels = {"name": "Product Type"}
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Product Type"}
            )
        }


class ProductForm(forms.ModelForm):
    GRAPHICS_CHOICES = [
        ("Integrated", "Integrated"),
        ("Dedicated", "Dedicated"),
    ]

    # Custom fields for specifications
    processor = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Processor"}
        ),
    )
    graphics = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.Select(
            choices=GRAPHICS_CHOICES,
            attrs={"class": "form-control", "placeholder": "Select Graphics"},
        ),
    )
    ram = forms.CharField(
        required=False,
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter RAM"}
        ),
    )
    storage = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Storage"}
        ),
    )
    screen_size = forms.CharField(
        required=False,
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Screen Size"}
        ),
    )
    resolution = forms.CharField(
        required=False,
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Resolution"}
        ),
    )
    operating_system = forms.CharField(
        required=False,
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Operating System"}
        ),
    )
    battery_capacity = forms.CharField(
        required=False,
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Battery Capacity"}
        ),
    )
    camera = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Camera"}
        ),
    )
    connectivity = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Connectivity"}
        ),
    )
    ports = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Ports"}
        ),
    )

    class Meta:
        model = Product
        fields = "__all__"
        exclude = ["product_id"]
        labels = {
            "name": "Product Name",
            "description": "Product Description",
            "sku": "SKU",
            "brand": "Brand",
            "model_number": "Model Number",
            "price": "Price",
            "discounted_price": "Discounted Price",
            "cost_price": "Cost Price",
            "stock_quantity": "Stock Quantity",
            "availability_status": "Availability Status",
            "category": "Category",
            "tags": "Tags",
            "product_type": "Product Type",
            "image_1": "Image 1",
            "image_2": "Image 2",
            "image_3": "Image 3",
            "image_4": "Image 4",
            "image_5": "Image 5",
            "weight": "Weight",
            "dimensions": "Dimensions",
            "color": "Color",
            "material": "Material",
            "warranty_period": "Warranty Period",
            "power_consumption": "Power Consumption",
            "battery_life": "Battery Life",
            "processor": "Processor",
            "graphics": "Graphics",
            "ram": "RAM",
            "storage": "Storage",
            "screen_size": "Screen Size",
            "resolution": "Resolution",
            "operating_system": "Operating System",
            "battery_capacity": "Battery Capacity",
            "camera": "Camera",
            "connectivity": "Connectivity",
            "ports": "Ports",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Product Name"}
            ),
            "description": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Product Description",
                }
            ),
            "sku": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Product SKU"}
            ),
            "brand": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Product Brand"}
            ),
            "model_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Product Model Number",
                }
            ),
            "price": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Enter Product Price"}
            ),
            "discounted_price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Product Discounted Price",
                }
            ),
            "cost_price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Product Cost Price",
                }
            ),
            "stock_quantity": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Product Stock Quantity",
                }
            ),
            "availability_status": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Product Availability Status",
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Select Product Category",
                }
            ),
            "tags": forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"}),
            "product_type": forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Select Product Type",
                }
            ),
            "image_1": forms.FileInput(
                attrs={"class": "form-control", "placeholder": "Select Product Image 1"}
            ),
            "image_2": forms.FileInput(
                attrs={"class": "form-control", "placeholder": "Select Product Image 2"}
            ),
            "image_3": forms.FileInput(
                attrs={"class": "form-control", "placeholder": "Select Product Image 3"}
            ),
            "image_4": forms.FileInput(
                attrs={"class": "form-control", "placeholder": "Select Product Image 4"}
            ),
            "image_5": forms.FileInput(
                attrs={"class": "form-control", "placeholder": "Select Product Image 5"}
            ),
            "weight": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Enter Product Weight"}
            ),
            "dimensions": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Product Dimensions",
                }
            ),
            "color": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Product Color"}
            ),
            "material": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Product Material"}
            ),
            "warranty_period": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Warranty Period"}
            ),
            "power_consumption": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Power Consumption",
                }
            ),
            "battery_life": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Battery Life"}
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        specifications = {
            "Processor": cleaned_data.get("processor"),
            "RAM": cleaned_data.get("ram"),
            "Graphics": cleaned_data.get("graphics"),
            "Storage": cleaned_data.get("storage"),
            "Screen Size": cleaned_data.get("screen_size"),
            "Resolution": cleaned_data.get("resolution"),
            "Operating System": cleaned_data.get("operating_system"),
            "Battery Capacity": cleaned_data.get("battery_capacity"),
            "Camera": cleaned_data.get("camera"),
            "Connectivity": cleaned_data.get("connectivity"),
            "Ports": cleaned_data.get("ports"),
        }

        # Filter out empty values
        filtered_specifications = {k: v for k, v in specifications.items() if v}
        self.cleaned_data["specifications"] = filtered_specifications
        return self.cleaned_data

    def save(self, commit=True):
        product = super().save(commit=False)
        product.specifications = self.cleaned_data.get("specifications")
        if commit:
            product.save()
        return product