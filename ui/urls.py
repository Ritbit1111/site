from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import RedirectView
import home.views as invw

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name = "home/login.html"), name="login"),
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
    path('home/', invw.welcome),
    path(r'singledayTCA/', include('singleTCA.urls')),
    path(r'multipledayTCA/', include('multipleTCA.urls')),
    path('logout/', auth_views.LogoutView.as_view()),
]
