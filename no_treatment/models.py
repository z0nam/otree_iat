from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Namun Cho <mailto:kberi.namun@gmail.com>'

doc = """
중립 이미지 treatment
"""


class Constants(BaseConstants):
    name_in_url = 'no_treatment'
    quiz_title = "사물 퀴즈"
    left_keycode = 49  # 1
    right_keycode = 48  # 0
    META_KEYCODE = 32  # space bar
    META_KEYNAME = "스페이스 바"
    players_per_group = None

    quiz_flower = [
        {
            'filename': '1.png',
            'name': '튤립',
            'right_answer': '튤립: 백합과의 구근초',
            'wrong_answer': '장미: 장미목 장미과에 속하는 식물',
        },
        {
            'filename': '2.png',
            'name': '백합',
            'right_answer': '백합: 백합과에 속한 다년생 초본식물',
            'wrong_answer': '목련: 목련과에 속하는 낙엽교목',
        },
        {
            'filename': '3.png',
            'name': '카네이션',
            'right_answer': '카네이션: 중심자목 석죽과의 여러해살이풀',
            'wrong_answer': '달리아: 초롱꽃목 국화과의 여러해살이풀',
        },
        {
            'filename': '4.png',
            'name': '동백꽃',
            'right_answer': '동백꽃: 물레나무목 차나무과의 속씨식물',
            'wrong_answer': '연꽃: 수련과에 속하는 다년생 초본식물',
        },
        {
            'filename': '5.png',
            'name': '라벤더',
            'right_answer': '라벤더: 꿀풀과 라반둘라속에 속하는 25-30종의 식물',
            'wrong_answer': '프리지아: 백합목 붓꽃과의 구근초',
        },
        {
            'filename': '6.png',
            'name': '벚꽃',
            'right_answer': '벚꽃: 이판화군 장미목 장미과의 낙엽교목',
            'wrong_answer': '사과나무꽃: 장미목 장미과의 낙엽성 활엽 소교목',
        },
        {
            'filename': '7.png',
            'name': '국화',
            'right_answer': '국화: 초롱꽃목 국화과의 여러해살이풀',
            'wrong_answer': '금잔화: 초롱꽃목 국화과의 한해살이풀',
        },
    ]

    num_rounds = len(quiz_flower) * 2


class Subsession(BaseSubsession):

    def creating_session(self):  # shuffle quiz order
        # print("######creating session!")
        if self.round_number == 1:
            for p in self.get_players():
                doubled_quiz_list = Constants.quiz_flower + Constants.quiz_flower  # 두번씩 나와야 하므로
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
