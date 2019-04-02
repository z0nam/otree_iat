from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player, Subsession
from category_words import word_bundle
import iat_order
import random
import time
from IAT_Global_Constants import GlobalConstants

LEFT, RIGHT = iat_order.LEFT, iat_order.RIGHT
FIRST, SECOND = iat_order.LEFT, iat_order.RIGHT


class Instruction(Page):

    def is_displayed(self):
        return self.round_number == 1

    timer_text = GlobalConstants.TIMER_TEXT

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def vars_for_template(self):
        vars_to_return = {}
        main_category_keys = list(word_bundle['main_category'].keys())
        sub_category_keys = list(word_bundle['sub_category'].keys())

        vars_to_return['main_categories'] = main_category_keys
        vars_to_return['sub_categories'] = sub_category_keys
        index = 0
        for main_key in main_category_keys:
            index += 1
            key = 'main_' + str(index)
            vars_to_return[key] = main_key
            key += '_keywords'
            vars_to_return[key] = word_bundle['main_category'][main_key]

        index = 0
        for sub_key in sub_category_keys:
            index += 1
            key = 'sub_' + str(index)
            vars_to_return[key] = sub_key
            key += '_keywords'
            vars_to_return[key] = word_bundle['sub_category'][sub_key]

        return vars_to_return

class Introduction(Page):

    def vars_for_template(self):
        vars_for_return = {}
        vars_for_return.update(get_category_names_from_block(self))
        category_names = get_category_names_from_block(self)
        vars_for_return['left_main_category'] = None
        vars_for_return['right_main_category'] = None
        vars_for_return['left_sub_category'] = None
        vars_for_return['right_sub_category'] = None
        # print(category_names)
        if 'left_main_category' in category_names:
            vars_for_return['left_main_category'] = category_names['left_main_category']
            vars_for_return['right_main_category'] = category_names['right_main_category']
        if 'left_sub_category' in category_names:
            vars_for_return['left_sub_category'] = category_names['left_sub_category']
            vars_for_return['right_sub_category'] = category_names['right_sub_category']
        vars_for_return['additional_message'] = \
            self.participant.vars['blocks'].additional_messages[self.round_number-1]
        return vars_for_return



class IAT(Page):

    def vars_for_template(self):
        vars_for_return = {
            'iat_items': self.participant.vars['blocks'].iat_block_list[self.round_number-1].iat_items,
            'correct_sides': self.participant.vars['blocks'].iat_block_list[self.round_number-1].correct_side,
        }

        vars_for_return.update(get_category_names_from_block(self))

        category_names_for_block = get_category_names_from_block(self)
        category_names = iat_order.default_iat_block.get_category_names()

        vars_for_return['left_main_category'] = None
        vars_for_return['right_main_category'] = None
        vars_for_return['left_sub_category'] = None
        vars_for_return['right_sub_category'] = None
        vars_for_return['main_items'] = None
        vars_for_return['sub_items'] = None
        vars_for_return['main_items'] = word_bundle['main_category'][category_names['left_main_category']] \
                                        + word_bundle['main_category'][category_names['right_main_category']]
        vars_for_return['sub_items'] = word_bundle['sub_category'][category_names['left_sub_category']] \
                                       + word_bundle['sub_category'][category_names['right_sub_category']]

        if 'left_main_category' in category_names_for_block:
            vars_for_return['left_main_category'] = category_names_for_block['left_main_category']
            vars_for_return['right_main_category'] = category_names_for_block['right_main_category']

        if 'left_sub_category' in category_names_for_block:
            vars_for_return['left_sub_category'] = category_names_for_block['left_sub_category']
            vars_for_return['right_sub_category'] = category_names_for_block['right_sub_category']

        # vars_for_return['seed_for_refresh_js_cache'] = random.random() #todo: delete after production
        vars_for_return['seed_for_refresh_js_cache'] = 0
        return vars_for_return

    form_model = 'player'
    form_fields = [
        'category_table',
        'item_table',
        'keypress_table',
        'iat_table',
    ]


def get_category_names_from_block(self):
    category_names = self.participant.vars['blocks'].iat_block_list[self.round_number-1].get_category_names()
    return category_names


page_sequence = [
    Instruction,
    Introduction,
    IAT,
]
