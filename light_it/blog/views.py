from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.utils import timezone

from .models import Post, Comment
from .forms import PostForm, CommentForm


def authorization_page(request):
    return render(request, 'blog/authorization_page.html', {'m_page': m_page})


def m_page(request):
    posts = (
        Post.objects
        .select_related('author')
        .prefetch_related('comments')
        .order_by('-published_date'))

    form = PostForm(request.POST or None)

    if form.is_valid():
        form = form.save(commit=False)
        form.author = request.user
        form.published_date = timezone.now()
        form.save()
        return redirect('m_page')

    context = {'messages': posts, 'form': form, 'm_edit': mess_edit}
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


def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    form = CommentForm(request.POST or None)

    if form.is_valid():
        form = form.save(commit=False)
        form.author = request.user
#        form.post = post
        form.post = post
#        form.published_date = timezone.now()
        form.save()
        return redirect ('m_page')
    else:
        form = CommentForm()
    context ={'form': form}
    return render (request, 'blog/add_comment.html', context)


def add_comment_2(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    form = CommentForm(request.POST or None)

    if form.is_valid():
        form = form.save(commit=False)
        form.author = request.user
#        form.post = post
        form.comment = comment
#        form.published_date = timezone.now()
        form.save()
        return redirect ('m_page')
    else:
        form = CommentForm()
    context ={'form': form, 'comment': comment}
    return render (request, 'blog/add_comment.html', context)
