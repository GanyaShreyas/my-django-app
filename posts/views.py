from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostCreateForm,CommentForm
from .models import Post
from .models import Post


from django.http import JsonResponse
@login_required
def post_create(request):
    if request.method == "POST":
        form = PostCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            return redirect('feed')  # Redirect to a success page or the detail view of the post
    else:
        form = PostCreateForm()

    return render(request, 'posts/create.html', {'form': form})




def feed(request):
    if request.method == 'POST':
        comment_form=CommentForm(data=request.POST)
        new_comment=comment_form.save(commit=False)
        post_id = request.POST.get('post_id')
        post=get_object_or_404(Post,id=post_id)
        new_comment.post=post
        new_comment.save()

    else:
        comment_form = CommentForm()

    posts=Post.objects.all()
    logged_user=request.user
    return render(request,'posts/feed.html',{'posts':posts,'logged_user':logged_user,'comment_form':comment_form})



def like_post(request):
    post_id = request.POST.get('post_id')
    post = get_object_or_404(Post, id=post_id)
    liked = False
    if post.liked_by.filter(id=request.user.id).exists():
        post.liked_by.remove(request.user)
    else:
        post.liked_by.add(request.user)
        liked = True
    return JsonResponse({'liked': liked, 'post_id': post_id})




"""
from django.shortcuts import render, redirect, get_object_or_404,
from django.contrib.auth.decorators import login_required
from .forms import PostCreateForm

@login_required
def post_create(request):
    if request.method == "POST":
        form = PostCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            return redirect('post_detail', pk=new_item.pk)  # Redirect to a success page or the detail view of the post
    else:
        form = PostCreateForm()

    return render(request, 'post/create.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post/detail.html', {'post': post})    
"""