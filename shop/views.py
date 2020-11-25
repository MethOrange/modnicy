
# Create your views here.
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'shop/post_list.html', {'posts': posts})


# def contact(request):
#     if request.method == 'POST':
#         # POST, generate form with data from the request
#         form = ContactForm(request.POST)
#         # Reference is now a bound instance with user data sent in POST
#         # process data, insert into DB, generate email, redirect to a new URL,etc
#     else:
#         # GET, generate blank form
#         form = ContactForm(initial={'email': 'johndoe@coffeehouse.com', 'name': 'John Doe'})
#         # Form is now initialized for first presentation to display these values
#         # Reference form instance (bound/unbound) is sent to template for rendering
#     return render(request, 'shop/post_list.html', {'form': form})
#
#
# from django.forms import ModelForm
#
#
# class ContactUsForm(ModelForm):
#     class Meta:
#         model = MailBox
#         fields = ['subject', 'message', 'sender']
#
#
# from django.core.mail import send_mail
#
# def post_share(request, post_id):
#     # Retrieve post by id
#     post = get_object_or_404(Post, id=post_id, status='published')
#     sent = False
#     if request.method == 'POST':
#         # Form was submitted
#         form = EmailPostForm(request.POST)
#         if form.is_valid():
#             # Form fields passed validation
#             cd = form.cleaned_data
#             post_url = request.build_absolute_uri(post.get_absolute_url())
#             subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
#             message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
#             send_mail(subject, message, 'admin@myblog.com',[cd['to']])
#             sent = True
#     else:
#         form = EmailPostForm()
#     return render(request, 'blog/post/share.html', {'post': post,
#                                                     'form': form,
#                                                     'sent': sent})
#
# from .forms import EmailPostForm
#
# from django.core.mail import send_mail
#
# def post_share(request, post_id):
#     # Retrieve post by id
#     post = get_object_or_404(Post, id=post_id, status='published')
#     sent = False
#     if request.method == 'POST':
#         # Form was submitted
#         form = EmailPostForm(request.POST)
#         if form.is_valid():
#             # Form fields passed validation
#             cd = form.cleaned_data
#             post_url = request.build_absolute_uri(post.get_absolute_url())
#             subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
#             message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
#             send_mail(subject, message, 'meth.orange@gmail.com',[cd['to']])
#             sent = True
#     else:
#         form = EmailPostForm()
#     return render(request, 'shop/post_list.html', {'post': post,
#                                                     'form': form,
#                                                     'sent': sent})

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Person





# сохранение данных в бд
def create(request):
    if request.method == "POST":
        tom = Person()
        tom.name = request.POST.get("name")
        tom.phone = request.POST.get("phone")
        tom.color = request.POST.get("color")
        tom.size = request.POST.get("size")
        tom.save()
    return HttpResponseRedirect("/")