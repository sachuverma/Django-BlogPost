from django.shortcuts import render

posts = [
  {
    'author': 'Sachin',
    'title': 'Blog Post 1',
    'content': 'First post',
    'date_posted': '10 May, 2020' 
  },
  {
    'author': 'Jhane',
    'title': 'Blog Post 2',
    'content': 'Second post',
    'date_posted': '11 Jul, 2020' 
  },
]

def home(request):
  context = {
    'posts': posts,
    'title': 'Home'
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})

