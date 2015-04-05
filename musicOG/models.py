# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from random import randint

# </standard imports>

author = 'Dylan Hurwitz'

# The description of the app support HTML tags
doc = """
This is a music piracy game. It is testing the effect of subscription services on the music market.
"""

# Link of the source code of your app or empty
source_code = "https://github.com/oTree-org/oTree/"


# List of strings of recomended literature for this app or an empty list
bibliography = (
    (
        'Basar, T., Olsder, G. J., Clsder, G. J., Basar, T., Baser, T., & '
        'Olsder, G. J. (1995). Dynamic noncooperative game theory (Vol. 200). '
        'London: Academic press.'
    ),
    (
        'Harsanyi, J. C., & Selten, R. (1988). A general theory of '
        'equilibrium selection in games. MIT Press Books, 1.'
    )
)


# Resources for understand your app, normally a wikipedia articles
# or an empty dict (This will be sorted alphabetically)
links = {
    "Wikipedia": {
        "Game Theory": "http://en.wikipedia.org/wiki/Game_theory",
        "Nash Equilibrim": "http://en.wikipedia.org/wiki/Nash_equilibrium"
    },
    "Resources": {
        "Introduction to Game Theory [Video]":
                "https://www.youtube.com/watch?v=nM3rTU927io",
    }
}


# A list of relevant keywords for your app or an empty list. This keyword will
# be automatically linked with duckduckgo.com anonymous search
keywords = ("Game Theory", "Nash Equilibrium", "Economics")


class Constants:
    name_in_url = 'music'
    players_per_group = 2
    num_rounds = 1
    producer_budget = 200
    consumer_budget = 100
    album_production_cost = 50
    album_own_cost = 20


    # define more constants here


class Subsession(otree.models.BaseSubsession):
    pass


class Album():

    def __init__(self, player):
        self.player = player
        self.value = randint(7, 13)

    def get_value(self):
        return self.value


class Group(otree.models.BaseGroup):
    # <built-in>
    subsession = models.ForeignKey(Subsession)
    # </built-in>


    x = Album(1)
    y = Album(2)
    z = Album(3)
    a = Album(4)

    val = x.value
    val1 = y.value
    val2 = z.value
    val3 = a.value




    def set_payoffs(self):
        consumer = self.get_player_by_role('consumer')
        producer = self.get_player_by_role('producer')


        consumer.payoff = self.val
        producer.payoff = 20




class Player(otree.models.BasePlayer):
    # <built-in>
    subsession = models.ForeignKey(Subsession)
    group = models.ForeignKey(Group, null = True)
    # </built-in>

    def other_player(self):
        """Returns other player in group. Only valid for 2-player groups."""
        return self.get_others_in_group()[0]

    # example field
    my_field = models.PositiveIntegerField(
        min=0,
        max=(Constants.producer_budget/Constants.album_production_cost),
        doc="""
        Description of this field, for documentation
        """
    )

    consumer_purchase = models.PositiveIntegerField(
        min=0,
        max=(Constants.consumer_budget/Constants.album_own_cost),
        doc="""
        Description of this field, for documentation
        """
    )

    album_purchase = models.PositiveIntegerField(
        min = 0,
        max = 1,
        doc = """ Binary album purchase
        """
    )


    def role(self):
        # you can make this depend of self.id_in_group
        if self.id_in_group == 1:
            return 'producer'
        if self.id_in_group == 2:
            return 'consumer'



