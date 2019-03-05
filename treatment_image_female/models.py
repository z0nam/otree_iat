from typing import Dict, List

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Namun Cho <mailto:kberi.namun@gmail.com>'

doc = """
여성 이미지 treatment
"""


class Constants(BaseConstants):
    name_in_url = 'treatment_image_female'
    quiz_title = "인물 퀴즈"
    left_keycode = 49 # 1
    right_keycode = 48 # 0
    players_per_group = None

    quiz_female = [
        {
            'filename': 'f1.png',
            'name': '피우진',
            'right_answer': """국가보훈처장, 육군 예비역 중령""",
            'wrong_answer': """육군 하사관""",
        },
        {
            'filename': 'f2.png',
            'name': '심상정',
            'right_answer': """국회의원 (제 17, 19, 20대 국회의원 선거 당선)""",
            'wrong_answer': """국회의원실 9급 행정비서""",
        },
        {
            'filename': 'f3.png',
            'name': '박정림',
            'right_answer': """KB증권 대표이사 사장""",
            'wrong_answer': """KB증권 상담창구 인턴""",
        },
        {
            'filename': 'f4.png',
            'name': '송연순',
            'right_answer': """노보텔 앰배서더 독산 대표이사, 총지배인""",
            'wrong_answer': """노보텔 앰배서더 독산 웨딩홀 서빙직원""",
        },
        {
            'filename': 'f5.png',
            'name': '김빛내리',
            'right_answer': """서울대학교 생명과학부 석좌교수""",
            'wrong_answer': """서울대학교 자연과학대 대학원 조교""",
        },
        {
            'filename': 'f6.png',
            'name': '이은숙',
            'right_answer': """국립암센터 원장""",
            'wrong_answer': """고려대학교 구로병원 흉부외과 레지던트""",
        },
        {
            'filename': 'f7.png',
            'name': '김영란',
            'right_answer': """전 대법관, 서강대학교 법학전문대학원 석좌교수""",
            'wrong_answer': """법원 행정처 9급 공무원""",
        },
    ]

    num_rounds = len(quiz_female)*2-1


class Subsession(BaseSubsession):

    def creating_session(self):  # shuffle quiz order
        print("######creating session!")
        if self.round_number == 1:
            for p in self.get_players():
                doubled_quiz_list = Constants.quiz_female + Constants.quiz_female  # 두번씩 나와야 하므로
                random.shuffle(doubled_quiz_list)
                p.participant.vars['shuffled_quiz_set'] = doubled_quiz_list
                # print("###in models: p.participant.vars:{}".format(p.participant.vars))


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    isCorrect = models.BooleanField()
    question_number = models.StringField()
    answer = models.StringField()
    location_of_correct_answer = models.StringField()
    
    def get_current_quiz(self):
        return self.participant.vars
