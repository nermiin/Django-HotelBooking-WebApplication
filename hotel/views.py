from django.shortcuts import render, redirect
from hotel.forms import HotelCreate
from hotel.models import Hotel


# Create your views here.
def hotel(request):
    if request.method == "POST":
        form = HotelCreate(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = HotelCreate()
    return render(request, 'base.html', {'form': form})


def show(request):
    employees = HotelCreate.objects.all()
    return render(request, "show.html", {'hotels': HotelCreate})


def edit(request, id):
    hotel = HotelCreate.objects.get(id=id)
    return render(request, 'edit.html', {'hotel': HotelCreate})


def update(request, id):
    hotel = HotelCreate.objects.get(id=id)
    form = HotelCreate(request.POST, instance=hotel)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'hotel': HotelCreate})


def destroy(request, id):
    employee = HotelCreate.objects.get(id=id)
    employee.delete()
    return redirect("/show")
