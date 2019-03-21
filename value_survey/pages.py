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


class ThanksNext(Page):
    pass

page_sequence = [
    ValueSurvey,
    ThanksNext,
]