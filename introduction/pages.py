from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

from IAT_Global_Constants import GlobalConstants
import time


class Introduction(Page):

    def vars_for_template(self):
        self.player.panel_id = self.participant.label
        self.participant.vars['panel_id'] = self.participant.label
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


page_sequence = [
    Introduction,
    Quiz_Introduction,
]
