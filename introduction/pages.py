from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

from IAT_Global_Constants import GlobalConstants
import time


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


page_sequence = [
    Introduction,
    Quiz_Introduction,
]
