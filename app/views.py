from django.shortcuts import render
from django.views.generic import  ListView  ,DetailView #list des objects
from django.views.generic.edit import FormView
from .models import  Bd
from .forms import BdForm
def index(request):
    return render(request,'app/index.html')

class BdView(FormView):
    form_class = BdForm
    template_name = 'app/index.html'

    def form_valid(self, form):
        form.save()
        return super(BdView, self).form_valid(form)

class PostList(ListView):
    model = Bd

class PostDetail(DetailView):
    model = Bd
# Create your views here.


# Create your views here.
