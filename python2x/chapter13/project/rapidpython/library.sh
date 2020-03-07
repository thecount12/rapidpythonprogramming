# django library 
#manage.py startapp library
cd library
#cat <<"LIBMODEL">> models.py
CHOICES=(
	('S','Science Fiction'),
	('F','Fantacy'), 
	('H','History'), 
	('T','Technical'), 
	('R','Religious'), 
	)

class BOOK(models.Model):
	title=models.CharField(max_length=100)
	description=models.TextField(null=True, blank=True)
	author=models.CharField(max_length=40)
	date=models.DateField()
	genre=models.CharField(max_length=1, choices=CHOICES)

	def __unicode__(self):
		return "%s by %s, %s" %(self.title,self,author,self.date.year)

LIBMODEL

#cat <<"LIBADMIN">> admin.py
from django.contrib import admin
from models import BOOK

admin.site.register(BOOK)

LIBADMIN 

echo "add to urls.py"
echo "url(r'^booklist/', BookList.as_view()), " 
echo "from library.views import BookList " 
echo "create library under django_templates"
echo "add library/book_list.html or change template name" 

#cat <<"BLIST">book_list.html
{% block content %}
<h2>Book Stuff</h2>
<ul>
	{% for b in object_list %}
		<li>{{ b.author}}</li>
	{% endfor %}
</ul>
{% endblock %}

	BLIST

