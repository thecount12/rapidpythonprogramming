from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog.models import Post


class PostListView(ListView):
    model = Post
    paginate_by = 3
    queryset = Post.objects.order_by('-created')


class PostDetailView(DetailView):
    model = Post


def PostCommentView(request,pk):
        user = User.objects.get(pk=pk)
        myedit = Profile.objects.get(user=user)

        post = get_object_or_404(Post,pk=pk)
        if request.method == 'POST':
                form = PostComment(request.POST)
                if form.is_valid():
                        comment = form.save(commit=False)
                        comment.post = post
                        comment.author=user
                        comment.save()
                        return redirect('/thanks/')
                        # return redirect('asdf.html',pk=post.pk)
        else:
                form = PostComment()
        return render(request, 'postcomment.html',{'form':form})
