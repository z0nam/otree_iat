from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random


class BasicSurvey(Page):
    form_model = 'player'
    form_fields = [
        'born_year', 
        'born_month',
        'gender',
        'marriage_state',
        'family_income_type',
        # 'residence_type',
        # 'family_living_with',
        # 'occupation',
        # 'education',
        'income_level',
    ]

    def born_year_error_message(self, value):
        if (value > Constants.BORN_YEAR_MAX or value < Constants.BORN_YEAR_MIN):
            return str.format("태어나신 해는 유효한 네자리 숫자 (가령 {} - {} 사이의 숫자) 로 입력하셔야 합니다.", Constants.BORN_YEAR_MIN, Constants.BORN_YEAR_MAX)

    def gender_choices(self):
        choices = Constants.GENDER_CHOICE.copy()
        random.shuffle(choices)
        return choices


class Thanks(Page):
    pass


page_sequence = [
    BasicSurvey,
    Thanks,
]
