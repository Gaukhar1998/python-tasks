from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from .models import Album
from .forms import UserForm, UserLoginForm
from django.contrib.auth.decorators import login_required

#@login_required()
class IndexView(generic.ListView):
    template_name = 'text/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class HomeView(generic.ListView):
    template_name = 'text/home.html'
    context_object_name = 'all_albums'
    def get_queryset(self):
        return Album.objects.all()

class AboutView(generic.ListView):
    template_name = 'text/about.html'
    context_object_name = 'all_albums'
    def get_queryset(self):
        return Album.objects.all()

def logout_view(request):
    logout(request)
    return redirect('text:home')

class DetailView(generic.DetailView):
    model = Album
    template_name = 'text/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('text:index')

def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        login(request,user)
        #print(request.user.is_authenticated())
        return redirect('text:home')
    return render(request, 'text/form.html', {'form':form})

class UserFormView(View):
    form_class = UserForm
    template_name = 'text/registration_form.html'

    #display blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    #process form data
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user.set_password(password)
            user.save()

            #returns User objects if credentials are correct
            user = authenticate(username=username,password=password,email=email)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('text:home')
        return render(request, self.template_name, {'form':form})