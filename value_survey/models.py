from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Namun Cho <mailto:kberi.namun@gmail.com>'

doc = """
Part of the KBERI's experimental study for 가부장제 인식개선 project
"""


class Constants(BaseConstants):
    name_in_url = 'value_survey'
    players_per_group = None
    num_rounds = 1

    L5_1, L5_2, L5_3, L5_4, L5_5, L5_OTHER = 1,2,3,4,5,99
    L5_CHOICES = [
        [L5_1, "매우 그렇지 않다"],
        [L5_2, "그렇지 않다"],
        [L5_3, "잘 모르겠다"],
        [L5_4, "그렇다"],
        [L5_5, "매우 그렇다"],
        [L5_OTHER, "응답거부"],
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
    faminist_self_awareness = models.IntegerField(
        label = "'나는 페미니스트이다' 에 대한 자신의 인식",
        choices = Constants.L5_CHOICES,
        widget = widgets.RadioSelectHorizontal,
    )

    faminist_definition = models.LongStringField(
        label = "'페미니스트'의 정의",
    )

    female_boss_experience = models.BooleanField(
        label = "여성 상사와의 업무 경험",
        choices = Constants.BINARY_CHOICES,
        widget = widgets.RadioSelectHorizontal,
    )

    male_boss_experience = models.BooleanField(
        label = "남성 상사와의 업무 경험",
        choices = Constants.BINARY_CHOICES,
        widget = widgets.RadioSelectHorizontal,
    )