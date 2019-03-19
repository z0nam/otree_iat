from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from iat_order import *
import iat_order


author = 'Namun Cho <kberi.namun@gmail.com>'

doc = """
IAT (Implicit Association Test) solution for KBERI 2019 research"
"""


class Constants(BaseConstants):
    name_in_url = 'iat'
    players_per_group = None

    LEFT, RIGHT = iat_order.LEFT, iat_order.RIGHT
    FIRST, SECOND = iat_order.LEFT, iat_order.RIGHT

    num_rounds = len(default_iat_blocks.iat_block_list)
    LEFT_KEYCODE = 69
    LEFT_KEY_NAME = '"ㄷ" (영문 E)'
    RIGHT_KEYCODE = 73
    RIGHT_KEY_NAME = '"ㅑ" (영문 I)'
    META_KEYCODE = 32
    META_KEY_NAME = '스페이스 바'

    OR = " 또는 "


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['blocks'] = Blocks()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    category_table = models.LongStringField()
    item_table = models.LongStringField()
    keypress_table = models.LongStringField()
    iat_table = models.LongStringField()
