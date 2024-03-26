from django.shortcuts import render, redirect
from .forms import PeopleForm
from .models import People


def create_order(request):
    template_name = "peopleapp/create.html"
    form = PeopleForm()
    if request.method == "POST":
        form = PeopleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {"form": form}
    return render(request, template_name, context)


def show_order(request):
    template_name = "peopleapp/show.html"
    orders = People.objects.all()
    context = {"orders": orders}
    return render(request, template_name, context)


def update_order(request, pk):
    obj = People.objects.get(id=pk)
    form = PeopleForm(instance=pk)
    if request.method == "POST":
        form = PeopleForm(request.POST, instance=pk)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    return render(request, 'create_url')


def cancel_order(request, pk):
    obj = People.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request, 'peopleapp/confirmation.html')

