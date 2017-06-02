from django.conf.urls import url
from dtables import views

urlpatterns = [
    url(r'^test/$',
        views.TestView.as_view())
]