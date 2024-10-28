from django import forms
from .models import Newsletter
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Subscribe'))


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