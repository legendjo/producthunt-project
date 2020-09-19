from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'products/home.html')

'''
1A-Check if a POST request i.e user want to create products
2A-Check if they have all required fileds
2A1-If all filed are set, the make a new product object. Import the Product model
2A2-Set all the propertyz of the product object
     votesTotal has been set to 1 in Model else set it to 0/1 i.e [ product.votesTotal = 1]
2A3- Check if product object already has a url else, we will pre-append a url to its url filed
2A4- Save created object to database
2A5-Return reidirect to Product page
2B-If all fileds are not there, render the error that All fields are required
1B-If not POST, the its a GET
'''

@login_required
def create(request):
    if request.method =='POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']

            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('htt://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']

            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user # set hunter to the user that request this POST
            product.save()
            #votesTotal has been set to 1 in Model else set it to 0/1 i.e [ product.votesTotal = 1]
            return redirect('home') #We will come back and redirect to Product Page return redirect('product')
        else:
            return render(request, 'products/create.html', {'error':'All fields are required'})
    else:
        return render(request, 'products/create.html')
