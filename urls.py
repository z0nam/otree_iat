from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf.urls import url
from otree.urls import urlpatterns

import otree.constants_internal as constants
import otree.views.participant as participant
from introduction import pages

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

urlpatterns.append(
    url(r'^InitializeParticipant/(?P<{}>[a-z0-9]+)/panel_id/(?P<panel_id>[\w\-]+)/$'.format(
            constants.participant_code
        ), pages.InitializeParticipant_panel_id,
        name="setting_panel_id"
    )
)

