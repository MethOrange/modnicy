
# Create your views here.
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import ContactForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'shop/post_list.html', {'posts': posts})


def contact(request):
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = ContactForm(request.POST)
        # Reference is now a bound instance with user data sent in POST
        # process data, insert into DB, generate email, redirect to a new URL,etc
    else:
        # GET, generate blank form
        form = ContactForm(initial={'email': 'johndoe@coffeehouse.com', 'name': 'John Doe'})
        # Form is now initialized for first presentation to display these values
        # Reference form instance (bound/unbound) is sent to template for rendering
    return render(request, 'shop/post_list.html', {'form': form})