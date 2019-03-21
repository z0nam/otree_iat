from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import quiz_lists


author = 'Namun Cho <mailto:kberi.namun@gmail.com>'

doc = """
남성 이미지 treatment
"""


class Constants(BaseConstants):
    name_in_url = 'treatment_image_male'
    quiz_title = "인물 퀴즈"
    left_keycode = 49  # 1
    right_keycode = 48  # 0
    META_KEYCODE = 32  # space bar
    META_KEYNAME = "스페이스 바"
    players_per_group = None

    quizzes = quiz_lists.male_quizzes

    num_rounds = len(quizzes) * 2


class Subsession(BaseSubsession):

    def creating_session(self):  # shuffle quiz order
        # print("######creating session!")
        if self.round_number == 1:
            for p in self.get_players():
                doubled_quiz_list = Constants.quizzes + Constants.quizzes  # 두번씩 나와야 하므로
                random.shuffle(doubled_quiz_list)
                p.participant.vars['shuffled_quiz_set'] = doubled_quiz_list


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    isCorrect = models.BooleanField()
    question_number = models.StringField()
    answer = models.StringField()
    location_of_correct_answer = models.StringField()

    def get_current_quiz(self):
        return self.participant.vars

