from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from category_words import wordBundle # main categorys and words 


author = 'Namun Cho <kberi.namun@gmail.com>'

doc = """
IAT (Implicit Association Test) solution for KBERI 2019 research"
"""
# 이제 수정 됨 ㅋㅋㅋ

class Constants(BaseConstants):
    name_in_url = 'iat'
    players_per_group = None
    num_rounds = 180 # 20+20+20+40+20+20+40

    class Decision:
        LEFT, RIGHT = 9999, 8888
    
    iat_order = { #todo 얘네들을 클래스로 만들어서 partner 호출하게 하고 스왑도 구현하고. 클래스 여러개여야 할 수도 있음
        "block_1": {
            "rounds":20,
            "leftCategory_1":list(wordBundle["mainCategory"].keys())[0], 
            "rightCategory_1":list(wordBundle["mainCategory"].keys())[1],
        },
        "block_2": {
            "rounds":20,
            "leftCategory":list(wordBundle["subCategory"].keys())[0], 
            "rightCategory":list(wordBundle["subCategory"].keys())[1],
        },
        "block_3": { # 그룹 절반은 sub catetory swap 되어야 함;;
            "rounds":20,
            "leftCategory_1":list(wordBundle['mainCategory'].keys())[0], 
            "leftCategory_2":list(wordBundle['subCategory'].keys())[1],
            "rightCategory_1":list(wordBundle['mainCategory'].keys())[1],
            "rightCategory_2":list(wordBundle['subCategory'].keys())[0]
        },
        "block_4": { # 그룹 절반은 sub catetory swap 되어야 함;; 근데 왜 어박사는 block 3과 4를 동일한 세팅인데 굳이 분류했을까?
            "rounds":40,
            "leftCategory_1":list(wordBundle['mainCategory'].keys())[0], 
            "leftCategory_2":list(wordBundle['subCategory'].keys())[1],
            "rightCategory_1":list(wordBundle['mainCategory'].keys())[1],
            "rightCategory_2":list(wordBundle['subCategory'].keys())[0]
        },
        "block_5": {
            "rounds":20,
            "leftCategory_1":list(wordBundle["mainCategory"].keys())[1], 
            "rightCategory_1":list(wordBundle["mainCategory"].keys())[0],
        },
        "block_6": { # 그룹 절반은 sub catetory swap 되어야 함;;
            "rounds":20,
            "leftCategory_1":list(wordBundle['mainCategory'].keys())[1], 
            "leftCategory_2":list(wordBundle['subCategory'].keys())[0],
            "rightCategory_1":list(wordBundle['mainCategory'].keys())[0],
            "rightCategory_2":list(wordBundle['subCategory'].keys())[1]
        },
        "block_7": { # 그룹 절반은 sub catetory swap 되어야 함;;
            "rounds":40,
            "leftCategory_1":list(wordBundle['mainCategory'].keys())[1], 
            "leftCategory_2":list(wordBundle['subCategory'].keys())[0],
            "rightCategory_1":list(wordBundle['mainCategory'].keys())[0],
            "rightCategory_2":list(wordBundle['subCategory'].keys())[1]
        },
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    success = models.BooleanField() # it is abundant but included to crosscheck
    elapsedTime = models.IntegerField()
    
    leftCategory = models.TextField()
    rightCategory = models.TextField()
    leftWord = models.TextField()
    rightWord = models.TextField()
    
    correctChoice = models.IntegerField() # also this is abundant but included to crosscheck
    userChoice = models.IntegerField()


