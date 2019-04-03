from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import otree.constants_internal as constants
import vanilla
import django.utils.timezone
from django.http import(
    HttpResponse, HttpResponseRedirect,
    HttpResponseNotFound
)


from IAT_Global_Constants import GlobalConstants
import time

import otree.views.participant
from otree.views import participant
from django.shortcuts import get_object_or_404, render_to_response
from otree.models import Participant, Session


class Introduction(Page):

    # overriding get() to set panel_id
    # url should be like: http://my_example_site.com/p/cmr1o61p/introduction/Introduction/1/?panel_id=mypanelid

    def get(self):
        panel_id = self.request.GET.get('panel_id', 'NO_PANEL_ID')
        self.player.participant.vars['panel_id'] = panel_id
        self.player.panel_id = panel_id

        return Page.get(self)
        # 또는
        # return super().get()

    def vars_for_template(self):
        return{
            'panel_id': self.player.panel_id
        }


class Quiz_Introduction(Page):

    def before_next_page(self):
        # print("#### before_next_page called")
        self.participant.vars['expiry'] = time.time() + GlobalConstants.EXPIRE_SECONDS
        self.participant.vars['start_time'] = time.time()
        # print("expiry = ", self.participant.vars['expiry'])

    def vars_for_template(self):
        expiry_minutes = int(round(GlobalConstants.EXPIRE_SECONDS / 60, 0))
        return {
            "EXPIRY_MINUTES": expiry_minutes,
        }


# class InitializeParticipant_panel_id(vanilla.UpdateView):

#     # url_pattern = r'^InitializeParticipant/(?P<{}>[a-z0-9]+)/panel_id/(?P<panel_id>[\w\-]+)/$'.format(
#     #         constants.participant_code
#     #     )

#     def get(self, *args, **kwargs):
#         print("panel_id: ", kwargs['panel_id'])
#         print("participant_code: ", kwargs['participant_code'])
#         print("constants:", dir(constants))
#         print("participant_label:", constants.participant_label)
#         print("request_absolute_url: ", self.request.build_absolute_uri())
#         print("args:", args)
#         print("kwargs:", kwargs)
#         print("request:", dir(self.request))

#         participant_with_panel_id = get_object_or_404(
#             Participant,
#             code=kwargs[constants.participant_code]
#         )

#         if participant_with_panel_id._index_in_pages == 0:
#             participant_with_panel_id._index_in_pages = 1
#             participant_with_panel_id.visited = True

#             participant_with_panel_id.label = kwargs['panel_id']
#             del kwargs['panel_id']
#             participant_with_panel_id.ip_address = self.request.META['REMOTE_ADDR']

#             now = django.utils.timezone.now()
#             participant_with_panel_id.time_started = now
#             participant_with_panel_id._last_page_timestamp = time.time()

#             participant_with_panel_id.save()

#         first_url = participant_with_panel_id._url_i_should_be_on()

#         return HttpResponseRedirect(first_url)


page_sequence = [
    Introduction,
    Quiz_Introduction,
]
