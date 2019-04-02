# iat_order

from category_words import word_bundle
import random

DEFAULT_BLOCK_NUMBER = 20
FIRST, SECOND = 0, 1
LEFT, RIGHT = 99, 100

class Block:
    iat_items = []
    correct_side = []
    left_main_category_index = None
    right_main_category_index = None
    left_sub_category_index = None
    right_sub_category_index = None
    additional_message = None

    def __init__(self, block_scheme):
        self.iat_items = []
        self.correct_side = []

        self.num_periods = block_scheme['num_periods']
        if block_scheme['left_main_category'] is not None:
            self.left_main_category_index = block_scheme['left_main_category']
            self.right_main_category_index = SECOND if self.left_main_category_index == FIRST else FIRST
        if block_scheme['left_sub_category'] is not None:
            self.left_sub_category_index = block_scheme['left_sub_category']
            self.right_sub_category_index = SECOND if self.left_sub_category_index == FIRST else FIRST
        self.construct()

    def swap_main_category(self):
        tmp = self.left_main_category_index
        self.left_main_category_index = self.right_main_category_index
        self.right_main_category_index = tmp
        self.determine_correct_side()

    # this method is not used in 2019 KBERI experiment, but leaved this for generality
    # location of sub category is fixed
    def swap_sub_category(self):
        tmp = self.left_sub_category_index
        self.left_sub_category_index = self.right_sub_category_index
        self.right_sub_category_index = tmp
        self.determine_correct_side()

    def swap_both_category(self):
        self.swap_main_category()
        self.swap_sub_category()
        self.determine_correct_side()

    def construct(self):
        self.construct_base_iat_list()

    def construct_base_iat_list(self):
        left_main_category = None
        right_main_category = None
        left_sub_category = None
        right_sub_category = None
        left_word_list = []
        right_word_list = []
        self.iat_items = []

        if self.left_main_category_index is not None:
            left_main_category = \
                self.get_keys(word_bundle['main_category'])[self.left_main_category_index]
            right_main_category = \
                self.get_keys(word_bundle['main_category'])[self.right_main_category_index]
        if self.left_sub_category_index is not None:
            left_sub_category = \
                self.get_keys(word_bundle['sub_category'])[self.left_sub_category_index]
            right_sub_category = \
                self.get_keys(word_bundle['sub_category'])[self.right_sub_category_index]

        if left_main_category is not None:
            left_word_list = word_bundle['main_category'][left_main_category].copy()
            right_word_list = word_bundle['main_category'][right_main_category].copy()

        if left_sub_category is not None:
            left_word_list += word_bundle['sub_category'][left_sub_category].copy()
            right_word_list += word_bundle['sub_category'][right_sub_category].copy()

        for i in range(0, self.num_periods):
            item = random.choice(left_word_list + right_word_list)
            self.iat_items.append(item)
        self.determine_correct_side()

    def determine_correct_side(self):
        self.correct_side = []
        left_items = []
        right_items = []
        if self.left_main_category_index is not None:
            left_items += \
                word_bundle['main_category'][(self.get_keys(word_bundle['main_category'])[self.left_main_category_index])]
            right_items += \
                word_bundle['main_category'][(self.get_keys(word_bundle['main_category'])[self.right_main_category_index])]
        if self.left_sub_category_index is not None:
            left_items += \
                word_bundle['sub_category'][(self.get_keys(word_bundle['sub_category'])[self.left_sub_category_index])]
            right_items += \
                word_bundle['sub_category'][(self.get_keys(word_bundle['sub_category'])[self.right_sub_category_index])]

        for i in range(0, self.num_periods):
            item = self.iat_items[i]
            if item in left_items:
                self.correct_side.append(LEFT)
            elif item in right_items:
                self.correct_side.append(RIGHT)
            else:
                print("ERROR!!!! item does not belong to L R")

    def get_keys(self, dictionary):
        return list(dictionary.keys())

    def set_period(self, periods):
        self.num_periods = periods
        self.construct_base_iat_list()

    def get_category_names(self):
        if self.left_main_category_index is not None and self.left_sub_category_index is not None:
            return_dict = {
                'left_main_category':
                    self.get_keys(word_bundle['main_category'])[self.left_main_category_index],
                'right_main_category':
                    self.get_keys(word_bundle['main_category'])[self.right_main_category_index],
                'left_sub_category':
                    self.get_keys(word_bundle['sub_category'])[self.left_sub_category_index],
                'right_sub_category':
                    self.get_keys(word_bundle['sub_category'])[self.right_sub_category_index],
            }
        elif self.left_main_category_index is not None and self.left_sub_category_index is None:
            return_dict = {
                'left_main_category':
                    self.get_keys(word_bundle['main_category'])[self.left_main_category_index],
                'right_main_category':
                    self.get_keys(word_bundle['main_category'])[self.right_main_category_index],
            }
        elif self.left_main_category_index is None and self.left_sub_category_index is not None:
            return_dict = {
                'left_sub_category':
                    self.get_keys(word_bundle['sub_category'])[self.left_sub_category_index],
                'right_sub_category':
                    self.get_keys(word_bundle['sub_category'])[self.right_sub_category_index],
            }
        else:
            return_dict = {
                "THERE IS NO CATEGORY!"
            }
        return return_dict


class Blocks:
    block_set = {
        'main': {
            'num_periods': DEFAULT_BLOCK_NUMBER,
            'left_main_category': FIRST,
            'left_sub_category': None,
        },
        'sub': {
            'num_periods': DEFAULT_BLOCK_NUMBER,
            'left_main_category': None,
            'left_sub_category': FIRST,
        },
        'both': {
            'num_periods': DEFAULT_BLOCK_NUMBER,
            'left_main_category': FIRST,
            'left_sub_category': FIRST,
        },
    }

    additional_messages = [  # size must be exactly same as self.iat_block_list
        "아래 설명을 읽어주세요",
        "아래 설명을 읽어주세요",
        "위쪽을 보십시오. 따로 제시되던 네 가지 범주가 이제는 함께 나타납니다. 단어는 한 번에 하나씩만 제시되며, 각 단어는 오직 한 가지 범주에만 해당된다는 것을 잊지 마십시오",
        "이번 세트는 직전 세트와 동일합니다. 단어는 한 번에 하나씩만 제시되며, 각 단어는 네 범주 중 오직 한가지 범주에만 해당된다는 것을 잊지 마십시오.",
        "위쪽을 보십시오. 범주의 위치가 바뀌었습니다.",
        "따로 제시되던 네 가지 범주가 함께 나타납니다. 바뀐 범주의 위치에 주의해주십시오. 단어는 한 번에 하나씩만 제시되며, 각 단어는 네 범주 중 오직 한가지 범주에만 해당된다는 것을 잊지 마십시오.",
        "이번 세트는 직전 세트와 동일합니다. 단어는 한 번에 하나씩만 제시되며, 각 단어는 네 범주 중 오직 한가지 범주에만 해당된다는 것을 잊지 마십시오.",
    ]

    def __init__(self):
        self.iat_block_list = []
        self.construct_base_block_list()

    def construct_base_block_list(self):
        self.iat_block_list = [  # list of default Blocks
            Block(self.block_set['main']),
            Block(self.block_set['sub']),
            Block(self.block_set['both']),
            Block(self.block_set['both']),
            Block(self.block_set['main']),
            Block(self.block_set['both']),
            Block(self.block_set['both']),
        ]
        for i in range(4, 7):
            self.iat_block_list[i].swap_main_category()

        self.iat_block_list[3].set_period(DEFAULT_BLOCK_NUMBER*2)
        self.iat_block_list[6].set_period(DEFAULT_BLOCK_NUMBER*2)

        for i in range(0,len(self.iat_block_list)):
            self.iat_block_list[i].additional_message = self.additional_messages[i]

        # decide whether default or swapped
        coin = random.randint(1, 2)
        if coin == 1:
            for block in self.iat_block_list:
                block.swap_main_category()


default_iat_blocks = Blocks()
default_iat_block = Block(Blocks.block_set['both'])
