from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass

class Results(Page):
    pass


page_sequence = [
    MyPage,
    Results
]


"""
김빛내리
김영란
박정림
송연순
심상정
이은숙
피우진
"""