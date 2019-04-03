from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf.urls import url
from otree.urls import urlpatterns


urlpatterns.append(
    url(
        r'^favicon.ico$',
        RedirectView.as_view(
            url=staticfiles_storage.url('favicon.ico'),
            permanent=False
        ),
        name='favicon'
    )
)
