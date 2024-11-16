from django.contrib import messages
from django.shortcuts import render, redirect
from .form import ProductForm, CategoryForm, TagForm, ProductTypeForm
from .models import Product, Category, Tag, ProductType

# View to create and list categories
def category_create_list(request):
    category = Category.objects.all()
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            if Category.objects.filter(name=form.cleaned_data['name']).exists():
                messages.error(request, 'Category already exists')
                return redirect('category_create_list')
            else:
                form.save()
                messages.success(request, 'Category created successfully')
                return redirect('category_create_list')
    context = {
        'category': category,
        'form': form,
    }
    return render(request, 'Category/category_create_list.html', context)

# View to update a category
def category_update(request, pk):
    category = Category.objects.get(id=pk)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            if Category.objects.filter(name=form.cleaned_data['name']).exists():
                messages.error(request, 'Category already exists')
                return redirect('category_create_list')
            else:
                form.save()
                messages.success(request, 'Category updated successfully')
                return redirect('category_create_list')
    context = {
        'form': form,
    }
    return render(request, 'Category/category_update.html', context)

# View to delete a category
def category_delete(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    messages.success(request, 'Category deleted successfully')
    return redirect('category_create_list')

# View to create and list tags
def tag_create_list(request):
    tag = Tag.objects.all()
    form = TagForm()
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            if Tag.objects.filter(name=form.cleaned_data['name']).exists():
                messages.error(request, 'Tag already exists')
                return redirect('tag_create_list')
            else:
                form.save()
                messages.success(request, 'Tag created successfully')
                return redirect('tag_create_list')
    context = {
        'tag': tag,
        'form': form,
    }
    return render(request, 'Tag/tag_create_list.html', context)

# View to update a tag
def tag_update(request, pk):
    tag = Tag.objects.get(id=pk)
    form = TagForm(instance=tag)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            if Tag.objects.filter(name=form.cleaned_data['name']).exists():
                messages.error(request, 'Tag already exists')
                return redirect('tag_create_list')
            else:
                form.save()
                messages.success(request, 'Tag updated successfully')
                return redirect('tag_create_list')
    context = {
        'form': form,
    }
    return render(request, 'Tag/tag_update.html', context)

# View to delete a tag
def tag_delete(request, pk):
    tag = Tag.objects.get(id=pk)
    tag.delete()
    messages.success(request, 'Tag deleted successfully')
    return redirect('tag_create_list')

# View to create and list product types
def product_type_create_list(request):
    product_type = ProductType.objects.all()
    form = ProductTypeForm()
    if request.method == 'POST':
        form = ProductTypeForm(request.POST)
        if form.is_valid():
            if ProductType.objects.filter(name=form.cleaned_data['name']).exists():
                messages.error(request, 'Product Type already exists')
                return redirect('product_type_create_list')
            else:
                form.save()
                messages.success(request, 'Product Type created successfully')
                return redirect('product_type_create_list')
    context = {
        'product_type': product_type,
        'form': form,
    }
    return render(request, 'ProductType/product_type_create_list.html', context)

# View to update a product type
def product_type_update(request, pk):
    product_type = ProductType.objects.get(id=pk)
    form = ProductTypeForm(instance=product_type)
    if request.method == 'POST':
        form = ProductTypeForm(request.POST, instance=product_type)
        if form.is_valid():
            if ProductType.objects.filter(name=form.cleaned_data['name']).exists():
                messages.error(request, 'Product Type already exists')
                return redirect('product_type_create_list')
            else:
                form.save()
                messages.success(request, 'Product Type updated successfully')
                return redirect('product_type_create_list')
    context = {
        'form': form,
    }
    return render(request, 'ProductType/product_type_update.html', context)

# View to delete a product type
def product_type_delete(request, pk):
    product_type = ProductType.objects.get(id=pk)
    product_type.delete()
    messages.success(request, 'Product Type deleted successfully')
    return redirect('product_type_create_list')

# View to create a product
def product_create(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product_info = {
                'name': form.cleaned_data['name'],
                'sku': form.cleaned_data['sku'],
                'brand': form.cleaned_data['brand'],
                'model_number': form.cleaned_data['model_number'],
                'category': form.cleaned_data['category'],
                'tags': form.cleaned_data['tags'],
                'product_type': form.cleaned_data['product_type'],
            }
            if Product.objects.filter(**product_info).exists():
                messages.error(request, 'Product already exists')
                return redirect('product_create')
            else:
                form.save()
                messages.success(request, 'Product created successfully')
                return redirect('product_create')
    context = {
        'form': form,
    }
    return render(request, 'Product/product_create.html', context)

# View to list products with search functionality
def product_list(request):
    # Search functionality
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
        if not products.exists():
            messages.error(request, 'No products found')
    else:
        # List all products
        products = Product.objects.all()
        if not products.exists():
            messages.error(request, 'No products found')
    context = {
        'products': products,
        'query': query,
    }
    return render(request, 'Product/product_list.html', context)

# View to display product details
def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product,
    }
    return render(request, 'Product/product_detail.html', context)

# View to update a product
def product_update(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product_info = {
                'name': form.cleaned_data['name'],
                'sku': form.cleaned_data['sku'],
                'brand': form.cleaned_data['brand'],
                'model_number': form.cleaned_data['model_number'],
                'category': form.cleaned_data['category'],
                'tags': form.cleaned_data['tags'],
                'product_type': form.cleaned_data['product_type'],
            }
            if Product.objects.filter(**product_info).exists():
                messages.error(request, 'Product already exists')
                return redirect('product_list')
            else:
                form.save()
                messages.success(request, 'Product updated successfully')
                return redirect('product_list')
    context = {
        'form': form,
    }
    return render(request, 'Product/product_update.html', context)

# View to delete a product
def product_delete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    messages.success(request, 'Product deleted successfully')
    return redirect('product_list')