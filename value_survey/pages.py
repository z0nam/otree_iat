from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time, datetime
from datetime import timedelta
from IAT_Global_Constants import GlobalConstants
import requests

from django.http import HttpResponseRedirect


class TimeOutError(Page): # timeout 구현하지 않을 경우 미사용

    def is_displayed(self):
        if self.participant.vars['expiry'] - time.time() < 0:
            self.participant.vars['is_timeout'] = True
            params = {
                'panel_id': self.participant.vars['panel_id'],
                'status': '002',
            }
            r = requests.get(url=GlobalConstants.EXTERNAL_URL, params=params)
            self.player.embrain_response = r.json()
            print(r.json())
            return True
        else:
            self.participant.vars['is_timeout'] = False
            return False

    def vars_for_template(self):
        start_time = self.participant.vars['start_time']
        current_time = time.time()
        elapsed_time = current_time - start_time
        print("elapsed_time =", elapsed_time)
        # elapsed_time = int(round(elapsed_time / 60, 0))
        # print("elapsed_time =", elapsed_time)

        start_time_str \
            = datetime.datetime.fromtimestamp(start_time).strftime(GlobalConstants.TIME_FORMAT)
        end_time_str \
            = datetime.datetime.fromtimestamp(current_time).strftime(GlobalConstants.TIME_FORMAT)
        elapsed_time_minutes = str(elapsed_time) + "분"

        return {
            'START_TIME': start_time_str,
            'END_TIME': end_time_str,
            'ELAPSED_TIME': elapsed_time_minutes,
            'MINIMUM_TIME_MINUTES': int(round(GlobalConstants.EXPIRE_SECONDS/60, 0))
        }


class ValueSurvey(Page):

    # def is_displayed(self):
    #     return not self.participant.vars['is_timeout']
    def is_displayed(self):
        self.player.elapsed_time_seconds = self.player.get_elapsed_time_seconds() or "UNWATCHED"
        return True


    form_model = 'player'
    form_fields = [
        'faminist_self_awareness',
        'faminist_definition',
        'female_boss_experience',
        'male_boss_experience',
    ]


class ValueSurvey02(Page):

    # def is_displayed(self):
    #     return not self.participant.vars['is_timeout']

    form_model = 'player'
    form_fields = [
        'value_q_01',
        'value_q_02',
        'value_q_03',
        'value_q_04',
        'value_q_05',
        'value_q_06',
        'value_q_07',
        'value_q_08',
        'value_q_09',
        'value_q_10',
    ]


class ValueSurvey03(Page):

    # def is_displayed(self):
    #     return not self.participant.vars['is_timeout']

    form_model = 'player'
    form_fields = [
        'value_q_11',
        'value_q_12',
        'value_q_13',
        'value_q_14',
        'value_q_15',
        'value_q_16',
        'value_q_17',
        'value_q_18',
        'value_q_19',
        'value_q_20',
    ]


class ValueSurvey04(Page):

    # def is_displayed(self):
    #     return not self.participant.vars['is_timeout']

    form_model = 'player'
    form_fields = [
        'value_q_21',
        'value_q_22',
        'value_q_23',
        'value_q_24',
        'value_q_25',
        'value_q_26',
        'value_q_27',
        'value_q_28',
        'value_q_29',
    ]


class Thanks(Page):

    def get(self):
        url = GlobalConstants.EXTERNAL_URL + "?panel_id=" \
              + self.participant.vars['panel_id']+"&elapsed_time_sec="+str(self.player.elapsed_time_seconds)
        print("return url:", url)
        return HttpResponseRedirect(url)

    def vars_for_template(self):
        return {
            'URL': GlobalConstants.EXTERNAL_URL,
            'PANEL_ID': self.participant.vars['panel_id']
        }


page_sequence = [
    ValueSurvey,
    ValueSurvey02,
    ValueSurvey03,
    ValueSurvey04,
    Thanks,
]
