# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


def vars_for_all_templates(self):
    return {
            'producer_budget': Constants.producer_budget,
            'consumer_budget': Constants.consumer_budget,
            'album_production_cost': Constants.album_production_cost,
            'album_own_cost': Constants.album_own_cost,
            'role': self.player.role()
    }


class MyPage(Page):

    form_model = models.Player
    form_fields = ['my_field']

    def is_displayed(self):
        return self.player.role() == 'producer'

    def vars_for_template(self):
        return {
            'my_variable_here': 1,
        }


class MyPageWait(WaitPage):

    def body_text(self):
        return "Waiting for other participants to contribute."



class ConsumerPhase(Page):


    form_model = models.Player
    form_fields = ['album_purchase']





    def is_displayed(self):
        return self.player.role() == 'consumer'


    def vars_for_template(self):
        return {
            'album1': self.group.val,
            'album2': self.group.val1,
            'album3': self.group.val2,
            'album4': self.group.val3
        }


class ConsumerPhaseWait(WaitPage):

    def body_text(self):
        return "Waiting for other participants to contribute."


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()



class Results(Page):

    pass


page_sequence =[
        MyPage,
        MyPageWait,
        ConsumerPhase,
        ConsumerPhaseWait,
        ResultsWaitPage,
        Results
    ]
