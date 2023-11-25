from django.urls import path
from . import views

app_name = "election_poll"


urlpatterns = [
    path("listpollingresult/", views.ListPollingResult, name='listpollingresult'),
    path("getpollingresult/<int:polling_id>", views.GetPollingResult, name='getpollingresult'),
    path("listlga/", views.ListLgas, name='listlga'),
    path("gettotallgaresult/", views.GetTotalLgaResult, name='gettotallgaresult'),
    path("partypollingresult/", views.PartyPollingResult, name='partypollingresult'),

]