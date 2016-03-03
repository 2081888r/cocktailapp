from django.conf.urls import patterns, url
from cocktail import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^cocktails/$', views.cocktails, name='cocktails'),
                       url(r'^cocktails_single/$', views.cocktails_single, name='cocktails_single'),  #change that with slug!
                       url(r'^cocktails_add/$', views.cocktails_add, name='cocktails_add'),
                       url(r'^cocktails/(?P<cocktail_slug>[\w\-]+)/edit/$', views.cocktails_edit, name='cocktails_edit'),
                       url(r'^cocktails/(?P<cocktail_slug>[\w\-]+)/$', views.cocktails_single, name='cocktails_single'),
                       url(r'^bartenders/$', views.bartenders, name='bartenders'),
                       url(r'^$', views.profile, name='profile'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^/accounts/register/$', views.register, name='register'),
                       url(r'^accounts/password_change/$', 'django.contrib.auth.views.password_change', {'post_change_redirect' : '/cocktail/accounts/password_change/done/'},  name="password_change"), 
                       url(r'^accounts/password_change/done/$', 'django.contrib.auth.views.password_change_done'),
                       url(r'^add_profile/$', views.register_profile, name='add_profile'),
                       url(r'^profile/(?P<username>\w{0,50})/$', views.profile, name='profile'),
                       url(r'^profile_update/', views.profile_update, name='profile_update'),
                       url(r'^404/$', views.error_page, name='404'),
                       url(r'^update_cocktail_rating/$', views.updateCocktailRating, name='update_cocktail_rating'),
                       )
