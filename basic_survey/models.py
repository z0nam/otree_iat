from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Namun Cho <mailto:kberi.namun@gmail.com>'

doc = """
기초정보 설문조사
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
        [FAMILY_OTHER, "기타"],
    ]

    LIVE_WITH_FAMILY, LIVE_WITH_NONFAMILY, ALONE = 1,2,3
    RESIDENCE_TYPE_CHOICE = [
        [LIVE_WITH_FAMILY, "가족 동거인 있음"],
        [LIVE_WITH_NONFAMILY, "가족 동거인 없음"],
        [ALONE, "동거인 없음"],
    ]

    FATHER, MOTHER, GRANDFATHER, GRANDMOTHER, SPOUSE, \
    CHILDREN, SIBLING, ETC, NONAPPLICABLE = 1, 2, 3, 4, 5, 6, 7, 8, 99

    FAMILY_CHOICE = [
        [FATHER, "부"],
        [MOTHER, "모"],
        [GRANDFATHER, "조부"],
        [GRANDMOTHER, "조모"],
        [SPOUSE, "배우자"],
        [CHILDREN, "자녀"],
        [SIBLING, "형제"],
        [ETC, "그 외 친척"],
        [NONAPPLICABLE, "해당없음(가족동거인 없음)"],
    ]

    OCCUPATION_CHOICE = [
        [1, "농업"],
        [2, "제조업"],
        [3, "공무원"],
        [4, "전문직"],
        [5, "무직"],
        [99, "기타"],
    ]

    EDUCATION_CHOICE = [
        [1, "초졸 이하"],
        [2, "초졸"],
        [3, "중졸"],
        [4, "고졸"],
        [5, "대학졸"],
        [6, "대학원졸"],
        [99, "모름, 무응답"]
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
        label = "선생님은 몇년도에 태어나셨습니까? (4자리)",
    )

    born_month = models.IntegerField(
        label = "태어난 달을 선택해주세요",
        choices = range(1,13),
        widget = widgets.RadioSelectHorizontal,
    )

    gender = models.IntegerField(
        label = "선생님의 성별은 무엇입니까?",
        choices = Constants.GENDER_CHOICE,
        widget = widgets.RadioSelectHorizontal,
    )

    marriage_state = models.IntegerField(
        label = "선생님의 결혼 상태는 다음 중 무엇입니까?",
        choices = Constants.MARRIAGE_CHOICE,
        widget = widgets.RadioSelectHorizontal,
    )

    family_income_type = models.IntegerField(
        label = "선생님의 가정은 어떤 형태인지요? 또한 가족 중에서 주로 소득을 버는 사람은 누구입니까?",
        choices = Constants.FAMILY_INCOME_CHOICE,
        widget = widgets.RadioSelectHorizontal,
    )
        # 'residence_type',
    residence_type = models.IntegerField(
        label = "선생님의 거주 형태는 무엇인가요?",
        choices = Constants.RESIDENCE_TYPE_CHOICE,
        widget = widgets.RadioSelectHorizontal,
    )
        # 'family_living_with',
    # family_living_with = models.IntegerField(
    #     label = "(가족 동거인 있는 경우만 응답) 함께 사는 동거 가족은 누구입니까? (복수응답 가능)",
    #     choices = Constants.FAMILY_CHOICE,
    #     widget = widgets.CheckboxSelectMultiple,
    # )
        # 'occupation',
    occupation = models.IntegerField(
        label = "선생님의 직업은 무엇입니까? (수정필요)",
        choices = Constants.OCCUPATION_CHOICE,
        widget = widgets.RadioSelectHorizontal,
    )

    education = models.IntegerField(
        label = "선생님의 학력은 무엇입니까? (수정필요)",
        choices = Constants.EDUCATION_CHOICE,
        widget = widgets.RadioSelectHorizontal,
    )
        # 'education',
        
    income_level = models.IntegerField(
        label = "선생님의 지난 6개월 평균 월 소득 (세후)은 얼마 정도인지요?",
        choices = Constants.INCOME_LEVEL_CHOICE,
        widget = widgets.RadioSelect,
    )

