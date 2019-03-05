from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random


class Quiz(Page):
    form_model = 'player'
    form_fields = [
        'question_number',
        'isCorrect',
        'answer',
    ]

    def vars_for_template(self):
        current_quiz = self.participant.vars['shuffled_quiz_set'][self.round_number]
        print("***round number:{}".format(self.round_number))
        # print("****length of self.participant.vars: {}".format(len(self.participant.vars)))
        location_of_correct_answer = random.choice(['left', 'right'])
        self.player.location_of_correct_answer = location_of_correct_answer
        if location_of_correct_answer == 'left':
            left_quiz = current_quiz['right_answer']
            right_quiz = current_quiz['wrong_answer']
        else:
            left_quiz = current_quiz['wrong_answer']
            right_quiz = current_quiz['right_answer']
        return {
            'quiz_title': Constants.quiz_title,
            'left_key': chr(Constants.left_keycode),
            'right_key': chr(Constants.right_keycode),
            'left_explanation': left_quiz,
            'right_explanation': right_quiz,
            'location_of_correct_answer': location_of_correct_answer,
            'image_path': Constants.name_in_url+"/"+current_quiz['filename'],
            'filename': current_quiz['filename'],
            'name': current_quiz['name'],
        }


class Results(Page):

    def vars_for_template(self):
        return Quiz.vars_for_template(self)


page_sequence = [
    Quiz,
    Results,
]
