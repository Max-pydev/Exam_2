from django.shortcuts import render, redirect

# Create your views here.
from .models import TodoModel
from .forms import TodoForm



def todo_view(request):

    form = TodoForm()
    book = request.filter(status=True)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            return redirect('home')
    return render(request, template_name='home.html', context={
        'form': form,
        'book': book,
    })




