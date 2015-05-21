from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateTimeField()
    imdb_link = models.CharField(max_length=300)
    image = models.ImageField(upload_to="images/movies/")
    plot = models.TextField()

    def __str__(self):
        return "{}({})".format(self.name, self.release_date)

class Post(models.Model):
    movie = models.ForeignKey(Movie)
    poster = models.ForeignKey(FBUser)
    rate = models.IntegerField(default=0)
    review = models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return "{} has written review on {}".format(self.poster, self.movie)

class Comment(models.Model):
    commenter = models.ForeignKey(FBUser)
    post = models.ForeignKey(Post)
    content = models.TextField()

    def __str__(self):
        return "{} says: {}".format(self.commenter, self.content)

class Crew(models.Model):
    image = models.ImageField(upload_to="images/crew/")
    name = models.CharField(max_length=100)
    imdb_link  = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name

class Role(models.Model):
    movie = models.ForeignKey(Movie)
    crew = models.ForeignKey(Crew)
    role_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
