from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Namun Cho <mailto:kberi.namun@gmail.com>'

doc = """
여성 이미지 treatment
"""


class Constants(BaseConstants):
    name_in_url = 'treatment_image_female'
    players_per_group = None
    num_rounds = 20


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    correctness = models.BooleanField()

