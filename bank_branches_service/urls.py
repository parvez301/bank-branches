from django.conf.urls import url

from bank_branches_service import views

urlpatterns = [
    url(r'^get-bank-branches/$', views.get_branches),
    url(r'^get-bank-branches/(?P<ifsc>[A-Za-z]{4}[a-zA-Z0-9]{7})/$', views.get_branches),
    url(r'^get-bank-branches/(?P<bank_name>\w+)/(?P<city>\w+)/$', views.get_branches)
]