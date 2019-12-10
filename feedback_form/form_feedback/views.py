from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import FeedBack

# Create your views here.
def homeView(request):
    form_class = FeedBack
    return render(request, 'form_feedback/form.html', {'form':form_class})

def successView(request):
    if request.method == 'POST':
        form = FeedBack(request.POST)

        if form.is_valid():
            form.save()
        return HttpResponse('Thank you for bearing us!')
    
    else:
        form=FeedBack()
    return render(request, 'form_feedback/form.html', {'form':form})