from tkinter import W
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user.username)

class Auctions(models.Model):
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    end_auction = models.BooleanField(default=False)

class Category(models.Model):
    category = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.category
    

class Lot(models.Model):
    title = models.CharField(max_length=180)
    photo = models.ImageField(upload_to='images', blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True, related_name='category_lot')
    owner_name = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True)
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.photo.url
        except:
            url=''
        return url

class Bid(models.Model):
    bid = models.DecimalField(max_digits=10, decimal_places=2)
    

class Comments(models.Model):
  item_comment = models.ForeignKey(Lot, on_delete=models.CASCADE)
  author_comment = models.ForeignKey(User, on_delete=models.CASCADE)
  body_comment = models.TextField()
  date_added = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
      return self.body_comment

class Watchlist(models.Model):
    watchlist_owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.watchlist_owner}'s watchlist"

class Watchlist_item(models.Model):
    item = models.OneToOneField(Lot, on_delete=models.CASCADE)
    watchlists = models.ManyToManyField(Watchlist, blank=True, related_name='watchlist_lots')

    def __str__(self):
        return self.item.title

