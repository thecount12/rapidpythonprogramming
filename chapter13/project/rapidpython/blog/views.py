from django.http import HttpResponse 
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django.shortcuts import render_to_response, render
from django.core.context_processors import csrf
from forms import PostReg



def mainindex(request):  
	#return HttpResponse("Hello world!") 
	return render_to_response("index.html") 



from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from blog.models import *

def main(request):
	"""Main listing."""
	posts = Post.objects.all().order_by("-created")
	paginator = Paginator(posts, 5)
	try: page = int(request.GET.get("page", '1'))
	except ValueError: page = 1
	try:
		posts = paginator.page(page)
	except (InvalidPage, EmptyPage):
		posts = paginator.page(paginator.num_pages)
	return render_to_response("list.html", dict(posts=posts, user=request.user))

def post(request, pk):
	"""Single post with comments and a comment form."""
	post = Post.objects.get(pk=int(pk))
	comments=Comment.objects.filter(post=post)
	#d = dict(post=post, user=request.user)
	d = dict(post=post, comments=comments, form=CommentForm(),user=request.user)
	d.update(csrf(request))
	return render_to_response("post.html", d)

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		exclude = ["post"]

def add_comment(request, pk):
	"""Add a new comment."""
	p = request.POST

	if p.has_key("body") and p["body"]:
		author = "Anonymous"
		if p["author"]: author = p["author"]

		comment = Comment(post=Post.objects.get(pk=pk))
		cf = CommentForm(p, instance=comment)
		cf.fields["author"].required = False

		comment = cf.save(commit=False)
		comment.author = author
		comment.save()
	return HttpResponseRedirect(reverse("blog.views.post", args=[pk]))

def msg(request):
	return render_to_response("contact.html") 

def addcontact(request, pk):
	"""Single post with comments and a comment form."""
	addcom = Contact.objects.get(pk=int(pk))
	comments=Comment.objects.filter(post=addcom)
	#d = dict(post=post, user=request.user)
	d = dict(post=addcom, comments=comments, form=CommentForm())
	return render_to_response("contact.html", d)

def newreg(request):
#       use next two lines to view form first before testing if
       	#form=PostReg()
       	#return render(request,'reg.html', {'form':form})
	
        if request.method == "POST":
                form = PostReg(request.POST)
                if form.is_valid():
                        post = form.save(commit=False)
                        #post.author = request.user
                        post.date= "2015-05-18" #use python date libs 
                        post.save()
#               return redirect('blog.views.post_detail', pk=post.pk)
                return render_to_response("thanks.html")
        else:
                form = PostReg()
        return render(request, 'reg.html', {'form': form})
	
