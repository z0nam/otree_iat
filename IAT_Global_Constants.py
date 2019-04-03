class GlobalConstants:
    EXPIRE_SECONDS_TEST = 1*60
    EXPIRE_SECONDS_PRODUCTION = 20*60
    TIMER_TEXT = "권장 완료 시간:"
    TIME_FORMAT = '"%Y년 %m월 %d일 %H시 %M분 %S초"'

    EXTERNAL_URL_TEST = 'http://127.0.0.1/~j/test/'  # running url
    EXTERNAL_URL_PRODUCTION = 'http://survey.panel.co.kr/2019/78469/m5.asp'  # reserved

    IS_TEST = False

    DEFAULT_PANEL_ID = "NO_PANEL_ID"

    if IS_TEST:
        EXTERNAL_URL = EXTERNAL_URL_TEST
        EXPIRE_SECONDS = EXPIRE_SECONDS_TEST
    else:
        EXTERNAL_URL = EXTERNAL_URL_PRODUCTION
        EXPIRE_SECONDS = EXPIRE_SECONDS_PRODUCTION

