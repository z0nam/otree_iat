from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'basic_survey'
    players_per_group = None
    num_rounds = 1

    BORN_YEAR_MIN = 1900
    BORN_YEAR_MAX = 2019
    
    MALE,FEMALE,GENDER_OTHER = 1,2,3
    GENDER_CHOICE = [
        [MALE, "남성"],
        [FEMALE, "여성"],
        [GENDER_OTHER, "기타"],
    ]


    NOT_MARRIED,MARRIED,DIVORCED_BEREAVEMENT,MARRIAGE_OTHER = 1,2,3,4
    MARRIAGE_CHOICE = [
        [NOT_MARRIED, "결혼 안함"],
        [MARRIED, "결혼함"],
        [DIVORCED_BEREAVEMENT, "이혼/사별함"],
        [MARRIAGE_OTHER, "기타"],
    ]

    FAMILY_BOTH_FATHER, FAMILY_BOTH_MOTHER, FAMILY_BOTH_BOTH,\
        FAMILY_SINGLE_FATHER, FAMILY_SINGLE_MOTHER, FAMILY_OTHER\
            = 1,2,3,\
                4,5,6
    FAMILY_INCOME_CHOICE = [
        [FAMILY_BOTH_FATHER, "양부모 가정 - 아버지"],
        [FAMILY_BOTH_MOTHER, "양부모 가정 - 어머니"],
        [FAMILY_BOTH_BOTH, "양부모 가정 - 부모 양쪽 비슷한 소득"],
        [FAMILY_SINGLE_FATHER, "한부모 가정 - 아버지"],
        [FAMILY_SINGLE_MOTHER, "한부모 가정 - 어머니"],
        [FAMILY_OTHER, "기타"]
    ]

    NO,UNDER_M100,M100,M200,M300,M400,OVER_M500 = 1,2,3,4,5,6,7
    INCOME_LEVEL_CHOICE = [
        [NO, "0 (소득없음)"],
        [UNDER_M100, "100만원 미만"],
        [M100, "100만원 - 199만원"],
        [M200, "200만원 - 299만원"],
        [M300, "300만원 - 399만원"],
        [M400, "400만원 - 499만원"],
        [OVER_M500, "500만원 이상"],
    ]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    born_year = models.IntegerField(
        label = "태어난 해 (4자리)",
    )

    born_month = models.IntegerField(
        label = "태어난 달",
        choices = range(1,12),
        widget = widgets.RadioSelectHorizontal,
    )

    gender = models.IntegerField(
        label = "성별",
        choices = Constants.GENDER_CHOICE,
        widget = widgets.RadioSelectHorizontal,
    )

    marriage_state = models.IntegerField(
        label = "결혼 상태",
        choices = Constants.MARRIAGE_CHOICE,
        widget = widgets.RadioSelectHorizontal,
    )

    family_income_type = models.IntegerField(
        label = "가정 환경 - 주된 소득 주체",
        choices = Constants.FAMILY_INCOME_CHOICE,
        widget = widgets.RadioSelectHorizontal,
    )
        # 'residence_type',
        # 'family_living_with',
        # 'occupation',
        # 'education',
        
    income_level = models.IntegerField(
        label = "지난 6개월 평균 월 소득 (세후)",
        choices = Constants.INCOME_LEVEL_CHOICE,
        widget = widgets.RadioSelect,
    )

