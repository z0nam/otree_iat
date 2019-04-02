from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)
from . import value_questions


author = 'Namun Cho <mailto:kberi.namun@gmail.com>'

doc = """
Part of the KBERI's experimental study for 가부장제 인식개선 project
"""


class Constants(BaseConstants):
    name_in_url = 'value_survey'
    players_per_group = None
    num_rounds = 1

    value_questions = value_questions.value_questions

    L5_1, L5_2, L5_3, L5_4, L5_5, L5_OTHER = 1, 2, 3, 4, 5, 99
    L5_CHOICES = [
        [L5_1, "매우 그렇지 않다"],
        [L5_2, "그렇지 않다"],
        [L5_3, "잘 모르겠다"],
        [L5_4, "그렇다"],
        [L5_5, "매우 그렇다"],
        [L5_OTHER, "응답거부"],
    ]

    L6_1, L6_2, L6_3, L6_4, L6_5, L6_6 = 1, 2, 3, 4, 5, 6
    L6_CHOICES = [
        [L6_1, "매우 동의하지 않음"],
        [L6_2, "동의하지 않음"],
        [L6_3, "다소 동의하지 않음"],
        [L6_4, "다소 동의함"],
        [L6_5, "동의함"],
        [L6_6, "매우 동의함"],
    ]

    YES, NO = True, False
    BINARY_CHOICES = [
        [YES, "있다"],
        [NO, "없다"],
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    embrain_response = models.StringField()
    faminist_self_awareness = models.IntegerField(
        label="'나는 페미니스트이다' 에 대한 자신의 인식",
        choices=Constants.L5_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    faminist_definition = models.LongStringField(
        label="'페미니스트'의 정의",
    )

    female_boss_experience = models.BooleanField(
        label="여성 상사와의 업무 경험",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    male_boss_experience = models.BooleanField(
        label="남성 상사와의 업무 경험",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )
    value_questions = Constants.value_questions

    value_q_01 = models.IntegerField(
        label=value_questions[0],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_02 = models.IntegerField(
        label=value_questions[1],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_03 = models.IntegerField(
        label=value_questions[2],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_04 = models.IntegerField(
        label=value_questions[3],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_05 = models.IntegerField(
        label=value_questions[4],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_06 = models.IntegerField(
        label=value_questions[5],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_07 = models.IntegerField(
        label=value_questions[6],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_08 = models.IntegerField(
        label=value_questions[7],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_09 = models.IntegerField(
        label=value_questions[8],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_10 = models.IntegerField(
        label=value_questions[9],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_11 = models.IntegerField(
        label=value_questions[10],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_12 = models.IntegerField(
        label=value_questions[11],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_13 = models.IntegerField(
        label=value_questions[12],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_14 = models.IntegerField(
        label=value_questions[13],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_15 = models.IntegerField(
        label=value_questions[14],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_16 = models.IntegerField(
        label=value_questions[15],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_17 = models.IntegerField(
        label=value_questions[16],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_18 = models.IntegerField(
        label=value_questions[17],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_19 = models.IntegerField(
        label=value_questions[18],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_20 = models.IntegerField(
        label=value_questions[19],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_21 = models.IntegerField(
        label=value_questions[20],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_22 = models.IntegerField(
        label=value_questions[21],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_23 = models.IntegerField(
        label=value_questions[22],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_24 = models.IntegerField(
        label=value_questions[23],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_25 = models.IntegerField(
        label=value_questions[24],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_26 = models.IntegerField(
        label=value_questions[25],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_27 = models.IntegerField(
        label=value_questions[26],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_28 = models.IntegerField(
        label=value_questions[27],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )
    value_q_29 = models.IntegerField(
        label=value_questions[28],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L6_CHOICES,
    )



