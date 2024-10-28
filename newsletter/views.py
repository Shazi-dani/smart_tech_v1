from django.shortcuts import render, redirect
from .forms import NewsletterForm

def subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = NewsletterForm()

    return render(request, 'newsletter/subscribe.html', {'form': form})

def thank_you(request):
    return render(request, 'newsletter/thank_you.html')
