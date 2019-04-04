from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "한국행동경제학연구소의 2019년 국회 여성가족위원회 프로젝트를 위한 행동실험 플랫폼",
}

# 처치효과 리스트. 가급적 순서에 맞춰 배열할 것

SESSION_CONFIGS = [
    {
       'name': 'introduction',
       'display_name': "실험 안내문 및 동의서",
       'num_demo_participants': 5,
       'app_sequence': ['introduction'],
    },
    {
        'name': 'quiz_bz',
        'display_name': "여성이미지 처치",
        'num_demo_participants': 3,
        'app_sequence': ['introduction', 'quiz_bz'],
        'treatment': 'quiz_bz',
    },
    {
        'name': 'quiz_ra',
        'display_name': "남성이미지 처치",
        'num_demo_participants': 3,
        'app_sequence': ['introduction', 'quiz_ra'],
        'treatment': 'quiz_ra',
    },
    {
        'name': 'quiz_kd',
        'display_name': "중립이미지(quiz_kd) 처치",
        'num_demo_participants': 3,
        'app_sequence': ['introduction', 'quiz_kd'],
        'treatment': 'quiz_kd',
    },
    {
        'name': 'quiz_ab',
        'display_name': "인식개선퀴즈 처치",
        'num_demo_participants': 3,
        'app_sequence': ['introduction', 'quiz_ab'],
        'treatment': 'quiz_ab',
    },
    {
        'name': 'value_survey',
        'display_name': "가부장적 가치관 설문조사",
        'num_demo_participants': 1,
        'app_sequence': ['introduction', 'value_survey'],
    },
    {
        'name': 'basic_survey',
        'display_name': "기초 설문조사",
        'num_demo_participants': 1,
        'app_sequence': ['introduction', 'basic_survey'],
    },
    {
        'name': 'iat',
        'display_name': "IAT",
        'num_demo_participants': 3,
        'app_sequence': ['introduction', 'iat'],
    },
    {
        'name': 'kberi_treatment_image_female',
        'display_name': "IAT for KBERI (여성이미지처치)",
        'num_demo_participants': 3,
        'app_sequence': ['introduction', 'quiz_bz', 'iat', 'value_survey'],
        'treatment': 'quiz_bz',
    },
    {
        'name': 'kberi_treatment_image_male',
        'display_name': "IAT for KBERI (남성이미지처치)",
        'num_demo_participants': 3,
        'app_sequence': ['introduction', 'quiz_ra', 'iat', 'value_survey'],
        'treatment': 'quiz_ra',
    },
    {
        'name': 'kberi_no_treatment',
        'display_name': "IAT for KBERI (꽃과나비이미지처치)",
        'num_demo_participants': 3,
        'app_sequence': ['introduction', 'quiz_kd', 'iat', 'value_survey'],
        'treatment': 'quiz_kd',
    },
    {
        'name': 'kberi_treatment_educative_quiz',
        'display_name': "IAT for KBERI (인식개선퀴즈처치)",
        'num_demo_participants': 3,
        'app_sequence': ['introduction', 'quiz_ab', 'iat', 'value_survey'],
        'treatment': 'educative_quiz',
    },
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ko'
# TIME_ZONE = 'Asia/Seoul'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'KRW'
USE_POINTS = True

ROOMS = [
    {
        'name': 'test001',
        'display_name': 'room panel_id test',
    },
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ 환영합니다! 한국행동경제학연구소 (KBERI)
의 IAT 테스트 페이지입니다! """

SECRET_KEY = 'rl6fs##!%y73glp&vojb!73ly^j#92201erbzlj!l)yh52l0g3'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']


# declare urls.py to get panel_id from embrain

ROOT_URLCONF = 'urls'


