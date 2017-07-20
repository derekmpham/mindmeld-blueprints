#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from mmworkbench.components import Conversation
from mmworkbench.components import NaturalLanguageProcessor

from conversation_test import ConversationTest

APP_PATH = '../..'

nlp = NaturalLanguageProcessor(app_path=APP_PATH)
nlp.load()


@pytest.fixture()
def convo():
    return Conversation(nlp=nlp, app_path=APP_PATH)


class TestFrame(ConversationTest):
    @pytest.mark.frame
    def test_action_movie(self, convo):
        convo.say('action movies')
        expected = {
            'type': [{'type': 'type', 'text': 'movies', 'cname': 'movie'}],
            'genre': [{'type': 'genre', 'text': 'action', 'cname': 'Action'}]
        }
        self.assert_frame(convo, expected)

    def test_comedy_tv(self, convo):
        convo.say('i want to watch a funny show')
        expected = {
            'type': [{'type': 'type', 'text': 'show', 'cname': 'tv-show'}],
            'genre': [{'type': 'genre', 'text': 'funny', 'cname': 'Comedy'}]
        }
        self.assert_frame(convo, expected)

    def test_jennifer_aniston_movie(self, convo):
        convo.say('i want to watch a movie starring Jennifer Aniston')
        expected = {
            'type': [{'type': 'type', 'text': 'movie', 'cname': 'movie'}],
            'cast': [{'type': 'cast', 'text': 'Jennifer Aniston', 'cname': None}]
        }
        self.assert_frame(convo, expected)

    def test_canadian_movie(self, convo):
        convo.say('i want to watch a Canadian movie')
        expected = {
            'type': [{'type': 'type', 'text': 'movie', 'cname': 'movie'}],
            # 'country': [{'type': 'country', 'text': 'Canadian'}]
        }
        self.assert_frame(convo, expected)

    @pytest.mark.frame
    def test_best_action_movie(self, convo):
        convo.say('best action movies at 2002')
        expected = {
            'genre': [{'cname': 'Action', 'text': 'action', 'type': 'genre'}],
            'sort': [{'cname': 'popular', 'text': 'best', 'type': 'sort'}],
            'sys_time': [{
                'cname': None, 'text': '2002', 'type': 'sys_time',
                'value': {'grain': 'year', 'value': '2002-01-01T00:00:00.000-07:00'}
            }],
            'type': [{'cname': 'movie', 'text': 'movies', 'type': 'type'}]
        }
        self.assert_frame(convo, expected)

    @pytest.mark.frame
    def test_tv_range(self, convo):
        convo.say('tv shows from the 90s')
        expected = {
            'sys_interval': [{'cname': None,
                              'text': '90s',
                              'type': 'sys_interval',
                              'value': {'grain': 'year',
                                        'value': ['1990-01-01T00:00:00.000-07:00',
                                                  '2000-01-01T00:00:00.000-07:00']}}],
            'type': [{'cname': 'tv-show', 'text': 'tv shows', 'type': 'type'}]
        }
        self.assert_frame(convo, expected)