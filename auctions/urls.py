from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("<int:category_id>", views.lot_category, name="lot_category"),
    path("lot/<int:lot_id>", views.lot, name="lot"),
    path("create_auction/<int:user_id>", views.create_auction, name="create_auction"),
    path("edit_auction/<int:lot_id>", views.edit_auction, name="edit_auction"),
    path("watchlist", views.watchlist, name='watchlist'),
    path("lot_au/<int:lot_id>/<int:user_id>", views.lot_au, name="lot_au"),
    path("watch_list/<int:user_id>", views.watch_list, name='watch_list'),
]
