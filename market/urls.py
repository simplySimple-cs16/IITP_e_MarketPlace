from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'market'

urlpatterns = [
    # /market
    path('', TemplateView.as_view(template_name='market/options.html'), name='home'),

    # /market/login
    url(r'^login/$', LoginView.as_view(template_name='market/login.html'), name='login'),

    # /market/register
    path('register/', views.UserFormView.as_view(), name='register'),

    # /market/logout
    url(r'^logout/$', LogoutView.as_view(template_name='market/logout.html'), name='logout'),

    # /market/buysell
    path('buysell/', views.BuySellView.as_view(), name='buysell'),

    # /market/buysell/sell
    url(r'buysell/sell/$', views.bsSellItem.as_view(), name='sell'),

    # /market/buysell/pk
    url(r'buysell/(?P<pk>[0-9]+)/$', views.bsItemUpdate.as_view(), name='bsItem-update'),

    # /market/buysell/pk/delete
    url(r'buysell/(?P<pk>[0-9]+)/delete/$', views.bsItemDelete.as_view(), name='bsItem-delete'),

    # /market/lost
    path('lost/', views.LostView.as_view(), name='lost'),

    # /market/lost/lost_sth
    url(r'lost/lost_sth/$', views.lAddItem.as_view(), name='lost_sth'),

    # /market/lost/pk
    url(r'lost/(?P<pk>[0-9]+)/$', views.lItemUpdate.as_view(), name='lItem-update'),

    # /market/lost/pk/delete
    url(r'lost/(?P<pk>[0-9]+)/delete/$', views.lItemDelete.as_view(), name='lItem-delete'),

    # /market/found
    path('found/', views.FoundView.as_view(), name='found'),

    # /market/found/found_sth
    url(r'found/found_sth/$', views.fAddItem.as_view(), name='found_sth'),

    # /market/found/pk
    url(r'found/(?P<pk>[0-9]+)/$', views.fItemUpdate.as_view(), name='fItem-update'),

    # /market/found/pk/delete
    url(r'found/(?P<pk>[0-9]+)/delete/$', views.fItemDelete.as_view(), name='fItem-delete'),

    # /market/rent
    path('rent/', views.RentView.as_view(), name='rent'),

    # /market/rent/rent_sth
    url(r'rent/to_let/$', views.rAddItem.as_view(), name='rent_sth'),

    # /market/rent/pk
    url(r'rent/(?P<pk>[0-9]+)/$', views.rItemUpdate.as_view(), name='rItem-update'),

    # /market/rent/pk/delete
    url(r'rent/(?P<pk>[0-9]+)/delete/$', views.rItemDelete.as_view(), name='rItem-delete'),

    # /market/found/pk/delete
    url(r'found/(?P<pk>[0-9]+)/delete/$', views.fItemDelete.as_view(), name='fItem-delete'),

    # /market/to_let
    path('to_let/', views.To_LetView.as_view(), name='to_let'),

    # /market/to_let/to_let_sth
    url(r'to_let/to_let_sth/$', views.tAddItem.as_view(), name='to_let_sth'),

    # /market/rent/pk
    url(r'to_let/(?P<pk>[0-9]+)/$', views.tItemUpdate.as_view(), name='tItem-update'),

    # /market/rent/pk/delete
    url(r'to_let/(?P<pk>[0-9]+)/delete/$', views.tItemDelete.as_view(), name='tItem-delete'),
]
