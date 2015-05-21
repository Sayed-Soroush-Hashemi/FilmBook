from django.shortcuts import render
from film_book.models import Movie, Post, Comment, Crew, Role
from users.models import FBUser

def show_movie(request, movie_id):
    movie = Movie.objects.filter(id=movie_id)
    cast = Role.objects.filter(movie=movie).filter(is_cast=True)
    crew = Role.objects.filter(movie=movie).filter(is_cast=False)
    rates = Rate.objects.filter(movie=movie)
    av_rate = 0
    for rate in rates:
        av_rate += rate.rate
    av_rate /= len(rates)
    try:
        rate = Rate.objects.get(movie=movie, user=request.user).rate
    except:
        rate = None        
    
    return render(request, 'movie-profile.html', {
        'movie': movie,
        'av_rate': av_rate,
        'rate': rate,
        'cast': cast,
        'crew': crew,
    })

def show_post(request, post_id):
    post = Post.objects.filter(id=post_id)
    comments = Comment.objects.filter(post=post)
    
    return render(request, 'post.html', {
        'post': post,
        'comment': comment,
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
