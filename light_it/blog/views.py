from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.core.urlresolvers import reverse
from .forms import PostForm
from django.utils import timezone


def authorization_page(request):
    return render(request, 'blog/authorization_page.html', {'m_page': m_page})


def m_page(request):
    messages = Post.objects.order_by('-published_date')
    form = PostForm(request.POST or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.author = request.user
        form.published_date = timezone.now()
        form.save()
        return redirect('m_page')
    context = {'messages': messages, 'form': form, 'm_edit': mess_edit}
    return render(request, 'blog/m_page.html', context)


def mess_edit(request, pk):
    message = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=message)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
#            form.published_date = timezone.now()  # If change pub. date nessesary
            form.save()
            return redirect('m_page')
    else:
        form = PostForm(instance=message)
    context = {'message': message, 'form': form}
    return render(request, 'blog/edit.html', context)
