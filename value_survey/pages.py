from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class ValueSurvey(Page):
    form_model = 'player'
    form_fields = [
        'faminist_self_awareness',
        'faminist_definition',
        'female_boss_experience',
        'male_boss_experience',
    ]


class ThanksNext(Page):
    pass

page_sequence = [
    ValueSurvey,
    ThanksNext,
]