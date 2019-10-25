from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil



def index(request):
    return render(request, 'shopping/index.html')

def home(request):
    # all_product = Product.objects.all()
    # print(all_product)
    # n = len(all_product)
    # nslides = n//4 + ceil((n/4)-(n//4))
    # # context = {'no_of_slides': nslides, 'range': range(1, nslides), 'all_product': all_product}
    # all_prods = [[all_product, range(1, nslides),  nslides],
    #              [all_product, range(1, nslides),  nslides]]
    # context = {'all_prods': all_prods}
    # return render(request, 'shopping/home.html', context)

    # category wise products-------------------
    all_prods = []
    catproducts = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catproducts}  #set comprehension
    for cat in cats:
        prods = Product.objects.filter(category=cat)
        n = len(prods)
        nslides = n//4 + ceil((n/4)-(n//4))
        all_prods.append([prods, range(1, nslides), nslides])
    context = {'all_prods': all_prods}
    return render(request, 'shopping/home.html', context)
    #
    # context = {'no_of_slides': nslides, 'range': range(1, nslides), 'all_product': all_product}

    # def product.objets.all()


def searchMatch(query, item):
    if query in item.description or query in item.subcategory or query in item.category or query in item.product_name:
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search')
    all_prods = []
    catproducts = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catproducts}  # set comprehension
    for cat in cats:
        prodstemp = Product.objects.filter(category=cat)
        prods = [item for item in prodstemp if searchMatch(query, item)]
        n = len(prods)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        all_prods.append([prods, range(1, nslides), nslides])
    context = {'all_prods': all_prods}
    return render(request, 'shopping/home.html', context)



def test(request):
    return render(request, 'shopping/test.html')


def product(request, myid):
    #fetch the product using id
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, 'shopping/product.html',{'product': product[0]})


def about(request):
    return render(request, 'shopping/about.html')


def contact(request):
    if request.method == 'POST':
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        # print(fname, lname, email, phone, desc)
        contact = Contact(First_Name=fname, Last_Name=lname, Email=email, Phone=phone, Description=desc)
        contact.save()
    return render(request, 'shopping/contact.html')



def productView(request):
    return HttpResponse('<h1> we are in productView page</h1>')
def tracking(request):
    return HttpResponse('<h1> we are in tracking page</h1>')

def checkout(request):
    if request.method == 'POST':
        item_json = request.POST.get('itemjson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        phone = request.POST.get('phone', '')

        # print(fname, lname, email, phone, desc)
        order = Order(Item_json=item_json, Name=name, Email=email, Address1=address, Address2=address,  City=city, State=state, Phone=phone)
        id = order.order_id
        order.save()

        # update = OrderUpdate(order_id=Order.Order_id, update_desc='The order has been placed')
        # print(update)
        # update.save()
    return render(request, 'shopping/checkout.html', {'id': id})


# Create your views here.
