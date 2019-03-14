from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player, Subsession
from category_words import word_bundle
import iat_order
import random

LEFT, RIGHT = iat_order.LEFT, iat_order.RIGHT
FIRST, SECOND = iat_order.LEFT, iat_order.RIGHT


class Introduction(Page):

    def vars_for_template(self):
        left_category = make_category_title(self, LEFT)
        right_category = make_category_title(self, RIGHT)
        return {
            'left_key': Constants.LEFT_KEY_NAME,
            'right_key': Constants.RIGHT_KEY_NAME,
            'left_keycode': Constants.LEFT_KEYCODE,
            'right_keycode': Constants.RIGHT_KEYCODE,
            'left_category': left_category,
            'right_category': right_category,
            'additional_message': self.participant.vars['blocks'].additional_messages[self.round_number-1],
            'meta_keycode': Constants.META_KEYCODE,
            'meta_key': Constants.META_KEY_NAME,
        }



class IAT(Page):

    def vars_for_template(self):
        vars_for_return = {
            'iat_items': self.participant.vars['blocks'].iat_block_list[self.round_number-1].iat_items,
            'correct_sides': self.participant.vars['blocks'].iat_block_list[self.round_number-1].correct_side,
        }
        vars_for_return.update(get_category_names(self))
        vars_for_return['left_category_name'] = make_category_title(self, LEFT)
        vars_for_return['right_category_name'] = make_category_title(self, RIGHT)
        category_names = get_category_names(self)
        vars_for_return['left_main_category']=None
        vars_for_return['right_main_category']=None
        vars_for_return['left_sub_category']=None
        vars_for_return['right_sub_category']=None
        print(category_names)
        if 'left_main_category' in category_names:
            vars_for_return['left_main_category'] = category_names['left_main_category']
            vars_for_return['right_main_category'] = category_names['right_main_category']
        if 'left_sub_category' in category_names:
            vars_for_return['left_sub_category'] = category_names['left_sub_category']
            vars_for_return['right_sub_category'] = category_names['right_sub_category']
        vars_for_return['seed_for_refresh_js_cache'] = random.random()
        return vars_for_return

    form_model = 'player'
    form_fields = [
        'category_table',
        'item_table',
        'keypress_table',
        'iat_table',
    ]


def get_category_names(self):
    category_names = self.participant.vars['blocks'].iat_block_list[self.round_number-1].get_category_names()
    return category_names


def make_category_title(self, side):
    category_names = get_category_names(self)
    print(category_names)
    if ('left_main_category' in category_names) and ('left_sub_category' in category_names):
        if side == Constants.LEFT:
            str_to_return = category_names['left_main_category']+Constants.OR+category_names['left_sub_category']
            return str_to_return
        elif side == Constants.RIGHT:
            str_to_return = category_names['right_main_category']+Constants.OR+category_names['right_sub_category']
            return str_to_return
    elif ('left_main_category' in category_names) and (not 'left_sub_category' in category_names):
        if side == Constants.LEFT:
            return category_names['left_main_category']
        elif side == Constants.RIGHT:
            return category_names['right_main_category']
    elif (not 'left_main_category' in category_names) and ('left_sub_category' in category_names):
        if side == Constants.LEFT:
            return category_names['left_sub_category']
        elif side == Constants.RIGHT:
            return category_names['right_sub_category']
    else:
        return "NO CATEGORY"


page_sequence = [
    Introduction,
    IAT,
]
