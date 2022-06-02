from django.shortcuts import render, redirect
from app.forms import EmailsForm
from app.models import Emails
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    data = {}
    search = request.GET.get('search')

    if search:
        data['db'] = Emails.objects.filter(email__icontains=search)
        return render(request, 'index.html', data)
    else:
        all = Emails.objects.all()
        paginator = Paginator(all, 5)
        pages = request.GET.get('page')
        data['db'] = paginator.get_page(pages)
        return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = EmailsForm()
    return render(request, 'form.html', data)

def create(request):
    form = EmailsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Emails.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Emails.objects.get(pk=pk)
    data['form'] = EmailsForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Emails.objects.get(pk=pk)
    form = EmailsForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('home')

def delete(request, pk):
    db = Emails.objects.get(pk=pk)
    db.delete()
    return redirect('home')
