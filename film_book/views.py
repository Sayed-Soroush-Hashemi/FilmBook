from django.shortcuts import render, redirect
from film_book.models import Movie, Post, Comment, Crew, Role, Rate
from film_book.forms import NewPostForm
from users.models import FBUser
from django.core.urlresolvers import reverse
import json
from django.http import HttpResponse
import time, pytz
from datetime import datetime

def show_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    cast = Role.objects.filter(movie=movie).filter(is_cast=True)
    crew = Role.objects.filter(movie=movie).filter(is_cast=False)
    rates = Rate.objects.filter(movie=movie)
    av_rate = 0
    for rate in rates:
        av_rate += rate.rate
    try:
        av_rate /= len(rates)
    except:
        pass
    av_rate = range(av_rate)
    try:
        rate = range(Rate.objects.get(movie=movie, user=request.user).rate)
    except:
        rate = None        
    
    return render(request, 'movie-profile.html', {
        'movie': movie,
        'av_rate': av_rate,
        'rate': rate,
	'range10': range(10),
        'cast': cast,
        'crew': crew,
    })

def show_post(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post)
    
    return render(request, 'post.html', {
        'post': post,
        'comments': comments,
	'rate': range(post.rate.rate)
    })

def search_results(request):
    search = request.GET.get('search')
    #    roles = Roles.objects.filter(role_name__contains=search)
    #    for role in roles:
    #        movies += role.movie
    movies = Movie.objects.filter(name__contains=search[i:j])
    movies += Movie.objects.filter(plot__contains=search[i:j])
    movies += Movie.objects.filter(role__role_name__contains=search[i:j])
    
    people = FBUser.objects.filter(firstname__contains=search[i:j])
    people += FBUser.objects.filter(lastname__contains=search[i:j])
    people += FBUser.objects.filter(username__contains=search[i:j])
    people += FBUser.objects.filter(nickname__contain=search[i:j])
    for i in range(len(search)):
        for j in range(i, len(search)):
            movies += Movie.objects.filter(name=search[i:j])
            movies += Movie.objects.filter(plot=search[i:j])
            movies += Movie.objects.filter(role__role_name=search[i:j])
            people += FBUser.objects.filter(firstname=search[i:j])
            people += FBUser.objects.filter(lastname=search[i:j])
            people += FBUser.objects.filter(username=search[i:j])
            people += FBUser.objects.filter(nickname=search[i:j])

    return render(request, 'search-results.html', {
        'movies': movies,
        'people': people,
    })


def user_followers(request, user_id):
    user = FBUser.objects.filter(id=user_id)
    users = user.followers
    return render(request, 'user-lists.html', {
        'users': users,
    })

def user_following(request, user_id):
    user = FBUser.objects.filter(id=user_id)
    users = FBUser.objects.filter(followers__contains=user)
    return render(request, 'user-lists.html', {
        'users': users,
    })

def show_timeline(request):
    if request.user.is_authenticated() == False:
        return redirect(reverse('user_edit_profile'))

    if request.method == "POST":
        form = NewPostForm(request.POST)        
        if form.is_valid():
            post = form.save(commit=False)
            post.poster = FBUser.objects.get(id=request.user.id)
            rate = Rate(movie=Movie.objects.get(id=request.POST.get('movie', None)), user=FBUser.objects.get(id=request.user.id), rate=request.POST.get('rating', 0))
            rate.save()
            post.rate = rate
            post.save()
            form = NewPostForm()
    else:
        form = NewPostForm()    
    user = FBUser.objects.get(id=request.user.id)
    posts = Post.objects.all().filter(poster__followers=user)
    return render(request, 'timeline.html', {
        'posts': posts,
        'user': FBUser.objects.get(id=request.user.id),
        'form': form,
    })

def add_comment(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('ascii'))
        comment = data['comment']
        postId = data['postId']
        user = FBUser.objects.get(id=request.user.id)
        newComment = Comment(commenter=user, post=Post.objects.get(id=postId), content=comment, pub_date=datetime.now().replace(tzinfo=pytz.utc).astimezone(pytz.timezone("Asia/Tehran")))
        newComment.save()
        res = {
            'commenter': user.username,
            'content': comment,
            'pubDate': newComment.pub_date.strftime("%d/%m/%Y"),
        }
        return HttpResponse(json.dumps(res), content_type="application/json")
    
def get_comments(request, all):
    user = FBUser.objects.get(id=request.user.id)
    if all == "true":
        comments = Comment.objects.all()
        print(comments)
    else:
        comments = Comment.objects.all().filter(post__poster__followers=user).filter(pub_date__gte=user.lastget)
    user.lastget = datetime.now().replace(tzinfo=pytz.utc).astimezone(pytz.timezone("Asia/Tehran"))
    user.save()
    res = {}
    for comment in comments:
        res["{}_{}".format(comment.post.id , comment.id)] = {
            'commenter': comment.commenter.username,
            'content': comment.content,
            'pubDate': comment.pub_date.replace(tzinfo=pytz.utc).astimezone(pytz.timezone("Asia/Tehran")).strftime("%d/%m/%y %H:%M"),
        }
    return HttpResponse(json.dumps(res), content_type="application/json")

