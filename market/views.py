from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic import View

from .models import BuySell, Lost, Found, Rent, To_Let
from .forms import UserForm

# Create your views here.


class BuySellView(generic.ListView):
    template_name = 'market/buysell.html'
    # context_object_name = 'object_list'  # default object name
    context_object_name = 'items'

    def get_queryset(self):
        return BuySell.objects.all()


class bsSellItem(CreateView):
    model = BuySell
    fields = ['userName', 'name', 'price', 'contact', 'image']


class bsItemUpdate(UpdateView):
    model = BuySell
    fields = ['name', 'price', 'contact', 'image']


class bsItemDelete(DeleteView):
    model = BuySell
    success_url = reverse_lazy('market:buysell')

class LostView(generic.ListView):
    template_name = 'market/lost.html'
    # context_object_name = 'object_list'  # default object name
    context_object_name = 'items'

    def get_queryset(self):
        return Lost.objects.all()


class lAddItem(CreateView):
    model = Lost
    fields = ['userName', 'ItemName', 'OwnerName', 'contact', 'image']


class lItemUpdate(UpdateView):
    model = Lost
    fields = ['ItemName', 'OwnerName', 'contact', 'image']


class lItemDelete(DeleteView):
    model = Lost
    success_url = reverse_lazy('market:lost')

class FoundView(generic.ListView):
    template_name = 'market/found.html'
    # context_object_name = 'object_list'  # default object name
    context_object_name = 'items'

    def get_queryset(self):
        return Found.objects.all()


class fAddItem(CreateView):
    model = Found
    fields = ['userName', 'ItemName', 'FinderName', 'contact', 'image']


class fItemUpdate(UpdateView):
    model = Found
    fields = ['ItemName', 'FinderName', 'contact', 'image']


class fItemDelete(DeleteView):
    model = Found
    success_url = reverse_lazy('market:found')


class RentView(generic.ListView):
    template_name = 'market/rent.html'
    # context_object_name = 'object_list'  # default object name
    context_object_name = 'items'

    def get_queryset(self):
        return Rent.objects.all()


class rAddItem(CreateView):
    model = Rent
    fields = ['userName', 'ItemName', 'Rentee', 'contact', 'image']


class rItemUpdate(UpdateView):
    model = Rent
    fields = ['ItemName', 'Rentee', 'contact', 'image']


class rItemDelete(DeleteView):
    model = Rent
    success_url = reverse_lazy('market:rent')


class To_LetView(generic.ListView):
    template_name = 'market/to_let.html'
    # context_object_name = 'object_list'  # default object name
    context_object_name = 'items'

    def get_queryset(self):
        return To_Let.objects.all()


class tAddItem(CreateView):
    model = To_Let
    fields = ['userName', 'ItemName', 'OwnerName', 'contact', 'ChargesPerDay', 'image']


class tItemUpdate(UpdateView):
    model = To_Let
    fields = ['ItemName', 'OwnerName', 'contact', 'ChargesPerDay', 'image']


class tItemDelete(DeleteView):
    model = To_Let
    success_url = reverse_lazy('market:to_let')


class UserFormView(View):
    form_class = UserForm  # class created in forms.py in music app
    template_name = 'market/registration_form.html'

    # display blank form to fill in
    def get(self, request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    # process form data (after submitting)
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    # request.user.username to access username
                    # request.user.profile_pic to access profile photo
                    return redirect('market:home')

        return render(request, self.template_name, {'form': form})


