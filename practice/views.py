from django.shortcuts import render
from django.http import HttpResponse
from .models import Human
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def index(request):
    return render(request, 'practice.html')


def detail(request):
    if request.method == "POST":
        print(request)
        email = request.POST.get('email', '')
        print(email)
        name = request.POST.get('name', '')
        age = request.POST.get('age', '')
        note = request.POST.get('note', '')
        # need to understand this
        human = Human(email=email, full_name=name, age=age, special_note=note)
        human.save()
        dynamic = Human.objects.all()
        context = {'dynamic': dynamic,
        }
    return render(request, 'details.html', context)

def per(request):
    dynamic = Human.objects.all()
    print(dynamic)
    return HttpResponse('Hello')


def collection(request):
    all_humans = Human.objects.all()
    html = ''
    for human in all_humans:
        url = '/practice/collection/' + str(human.id) + '/'
        html += '<a href="' + url + '">' + human.full_name + '</a></br>'
    return HttpResponse(html)


def collection_detail(request, id):
    human_all = Human.objects.get(id=id)
    context = {'human_all': human_all}
    return render(request, 'detail.html', context)
    # return HttpResponse('<h2> this is the detail page for :' + str(id) + ' </h2>')


class Create(CreateView):
    model = Human
    fields = ['email', 'full_name', 'age', 'special_note']



class Update(UpdateView):
    model = Human
    fields =['email', 'full_name', 'age', 'special_note']
   # if request.method == "POST":
   #  all_humans = Human.objects.get(id=id)
   #  form = huma
   #  return render(request, 'update.html')


class Delete(DeleteView):
    model = Human
    success_url = reverse_lazy('collection')






# def human_delete_view(request, id):
#     human=get_object_or_404(Human, id=id)


# Create your views here.
