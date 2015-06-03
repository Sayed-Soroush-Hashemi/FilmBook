from django.shortcuts import render, redirect
from film_book.models import Movie, Post, Comment, Crew, Role, Rate
from film_book.forms import NewPostForm
from users.models import FBUser
from django.core.urlresolvers import reverse

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
    user = request.user
    posts = Post.objects.all().filter(poster__followers=user)
    comments = []
    for post in posts:
        comments.append(Comment.objects.all().filter(post=post))
    return render(request, 'timeline.html', {
        'posts': posts,
        'user': FBUser.objects.get(id=request.user.id),
        'form': form,
        'comments': comments,
    })

def add_comment(request):
    print("addComment")
    if request.method == "POST":
        comment = request.POST.get('comment', '');
        postId = request.POST.get('postId', '');
        user = FBUser.objects.get(id=request.user.id)
        newComment = Comment(commenter=user, post=Post.objects.get(id=postId), content=comment)
        newComment.save()
        return "{'commenter': {}, 'content': {}, 'pubDate': {}}".format(user.username, comment, newComment.pub_date)
    else:
        return redirect(reverse('user_edit_profile'))
    
