from django.shortcuts import render, redirect

from products.forms import ProductCreateForm, ReviewCreateForm
from products.models import Product, Review, Category, HashTag


# Create your views here.

def main(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        category_id = request.GET.get('category')
        if category_id:
            products = Product.objects.filter(category=Category.objects.get(id=category_id))
        else:
            products = Product.objects.all()
        context = {
            'products': products,
            'users': request.user
        }
        return render(request, 'products/products.html', context=context)


def product_detail_view(request, post_id):
    if request.method == 'GET':
        product_obj = Product.objects.get(id=post_id)
        reviews = Review.objects.filter(product=product_obj)

        context = {
            'product': product_obj,
            'reviews': reviews,
            'form': ReviewCreateForm,
        }
        return render(request, 'products/detail.html', context=context)
    if request.method == 'POST':
        product_obj = Product.objects.get(id=post_id)
        reviews = Review.objects.filter(product=product_obj)
        form = ReviewCreateForm(data=request.POST)
        if form.is_valid() and not request.user.is_anonymous:
            Review.objects.create(
                author_id=request.user.id,
                title=form.cleaned_data.get('title'),
                product=product_obj
            )
            return redirect(f'/products/{product_obj.id}/')
        else:
            form.add_error('title', 'Pleas login')
        return render(request, 'products/detail.html', context={
            'product': product_obj,
            'reviews': reviews,
            'form': form
        })


def hashtags_view(request):
    if request.method == 'GET':
        hashtags = HashTag.objects.all()

        context = {
            "hashtags": hashtags
        }

        return render(
            request,
            'products/hashtags.html',
            context=context
        )


def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            'categories': categories,
        }

        return render(request, 'categories/index.html', context=context)


def create_product_view(request):
    if request.method == 'GET' and not request.user.is_anonymous:
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context)
    elif request.user.is_anonymous:
        return redirect('/products')

    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            Product.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data['price'] if form.cleaned_data['price'] is not None else 0,
                rate=form.cleaned_data['rate'],
                image=form.cleaned_data['image']
            )
            return redirect('/products/')

        return render(request, 'products/create.html', context={"form": form})
