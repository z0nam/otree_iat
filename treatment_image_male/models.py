from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


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

    quiz_male = [
        {
            'filename': 'm1.png',
            'name': '윤호영',
            'right_answer': '한국카카오은행 공동대표이사',
            'wrong_answer': '카카오프렌즈샵 판매직원',
        },
        {
            'filename': 'm2.png',
            'name': '임지순',
            'right_answer': '석좌교수 (서울대학교 물리천문학부), 석학교수 (포항공과대학교 물리학과)',
            'wrong_answer': '서울대학교 교무부 행정직원',
        },
        {
            'filename': 'm3.png',
            'name': '유승민',
            'right_answer': '국회의원 (제 17, 18, 19, 20대 국회의원 선거 당선)',
            'wrong_answer': '국회 9급기능직 속기사',
        },
        {
            'filename': 'm4.png',
            'name': '반기문',
            'right_answer': '전 외교통상부장관, 전 UN사무총장',
            'wrong_answer': '외무부 영사 직원',
        },
        {
            'filename': 'm5.png',
            'name': '이탄희',
            'right_answer': '판사 (수원지방법원 안양지원)',
            'wrong_answer': '법원 행정처 9급 공무원',
        },
        {
            'filename': 'm6.png',
            'name': '류영수',
            'right_answer': '건국대학교 수의과대학 학장, 수의학 교수',
            'wrong_answer': '경기도청 동물위생방역과 직원',
        },
        {
            'filename': 'm7.png',
            'name': '황성식',
            'right_answer': '쉐라톤 서울팔래스강남호텔 총괄영업이사',
            'wrong_answer': '쉐라톤 서울팔래스강남호텔 레스토랑 서빙 직원',
        },
    ]

    num_rounds = len(quiz_male)*2


class Subsession(BaseSubsession):

    def creating_session(self):  # shuffle quiz order
        # print("######creating session!")
        if self.round_number == 1:
            for p in self.get_players():
                doubled_quiz_list = Constants.quiz_male + Constants.quiz_male  # 두번씩 나와야 하므로
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

