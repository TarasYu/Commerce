from django.contrib import admin
from .models import User, Auctions, Lot, Bid, Category, Watchlist, Profile, Watchlist_item, Comments
# Register your models here.
#class Watchlist_itemAdmin(admin.ModelAdmin):
 #  filter_horizontal = ("watchlists",)

admin.site.register(User)
admin.site.register(Auctions)
admin.site.register(Comments)
admin.site.register(Lot)
admin.site.register(Bid)
admin.site.register(Category)
admin.site.register(Watchlist)
admin.site.register(Profile)
admin.site.register(Watchlist_item)# Watchlist_itemAdmin)
