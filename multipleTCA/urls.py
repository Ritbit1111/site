from django.conf.urls import url
import multipleTCA.views as vw
from django.contrib.auth import views as auth_views

urlpatterns=[
        url(r'^$', vw.FormView.as_view()),
        url(r'summary/', vw.Summary.as_view(), name="next"),
]