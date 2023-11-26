from django.http import JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import *



def home(request):
  template = loader.get_template('eaters/home.html')
  return HttpResponse(template.render())

def eaters(request):
    menus = Menu.objects.all()
    context = {'menus': menus}
    return render(request, 'eaters/eaters.html', context)

def cart(request):
  template = loader.get_template('eaters/cart.html')
  return HttpResponse(template.render())

def restaurant(request):
  restaurants = Restaurant.objects.all()
  context = {'restaurants': restaurants}
  return render(request, 'eaters/restaurant.html', context)


def login(request):
  template = loader.get_template('eaters/login.html')
  return HttpResponse(template.render())

def checkout(request):
  template = loader.get_template('eaters/checkout.html')
  return HttpResponse(template.render())

# update menu functionality
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Menu

def update_menu(request, pk):
    # Retrieve the Menu instance based on the provided primary key (pk)
    menu_item = get_object_or_404(Menu, pk=pk)

    if request.method == 'POST':
        # Update the menu item fields directly from the form data
        menu_item.name = request.POST.get('name')
        menu_item.description = request.POST.get('description')
        menu_item.prices = request.POST.get('prices')
        
        # Handle image file upload
        if 'image' in request.FILES:
            menu_item.image = request.FILES['image']

        # Save the updated menu item
        menu_item.save()

        # Optionally, you can return a JSON response for AJAX requests
        if request.is_ajax():
            return JsonResponse({'message': 'Menu item updated successfully'})

        # Redirect to a success page or any other logic you want
        return render(request, 'eaters/success.html')  # Create a success.html template

    # Render the update_menu.html template with the menu item
    return render(request, 'eaters/update_menu.html', {'menu_item': menu_item})
  
  
  # add menu functionality
def add_menu(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        restaurant_id = request.POST.get('restaurant')
        name = request.POST.get('name')
        description = request.POST.get('description')
        prices = request.POST.get('prices')
        image = request.FILES.get('image')

        # Create a new Menu instance with the form data
        new_menu = Menu.objects.create(
            restaurant_id=restaurant_id,
            name=name,
            description=description,
            prices=prices,
            image=image
        )

        # Redirect to the menu page or another appropriate page
        return redirect('eaters')  # Change 'menu' to the actual name of your menu page

    # Render the form for GET requests
    return render(request, 'eaters/add_menu.html')
  
  # delete functionality
def delete_menu(request, pk):
    menu_item = get_object_or_404(Menu, pk=pk)

    if request.method == 'POST':
        menu_item.delete()
        return redirect('eaters')  # Redirect to the eaters page after deletion

    return render(request, 'eaters/delete_menu.html', {'menu_item': menu_item})
  
  # search functionality
def search_results(request):
    query = request.GET.get('q', '')
    results = Menu.objects.filter(name__icontains=query)
    return render(request, 'eaters/search_results.html', {'results': results, 'query': query})
  
# login functionality
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'eaters/login.html'  # Specify your login template

    def get_success_url(self):
        return reverse('eaters/home')  # Adjust the URL name based on your project

    def form_valid(self, form):
        response = super().form_valid(form)

        # Redirect to the home page after successful login
        return redirect('eaters/home')


  


