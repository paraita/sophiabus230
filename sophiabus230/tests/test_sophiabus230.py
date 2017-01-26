#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
import os
from datetime import datetime
from datetime import timedelta
import sophiabus230
from dateutil.tz import gettz
from dateutil.tz import tzfile
from mock import patch
from future.moves.urllib import request


class TestSophiabus230(TestCase):

    expected = [
        {'dest': u'Cathédrale-Vieille Ville',
         'bus_time': None,
         'is_real_time': True},
        {'dest': u'Cathédrale-Vieille Ville',
         'bus_time': None,
         'is_real_time': True},
        {'dest': u'Cathédrale-Vieille Ville',
         'bus_time': None,
         'is_real_time': True},
        {'dest': u'Gambetta / France',
         'bus_time': datetime(2017, 1, 26, 17, 37),
         'is_real_time': True},
        {'dest': u'Cathédrale-Vieille Ville',
         'bus_time': datetime(2017, 1, 26, 17, 42),
         'is_real_time': False},
        {'dest': u'Cathédrale-Vieille Ville',
         'bus_time': datetime(2017, 1, 26, 17, 52),
         'is_real_time': False},
        {'dest': u'Cathédrale-Vieille Ville',
         'bus_time': datetime(2017, 1, 26, 17, 59),
         'is_real_time': False},
        {'dest': u'Gambetta / France',
         'bus_time': datetime(2017, 1, 26, 18, 7),
         'is_real_time': False}
    ]

    @patch('sophiabus230._get_html_from_cg06')
    def test_get_next_buses(self, mock_content):
        parent_path = os.path.dirname(os.path.abspath(__file__))
        with open(parent_path + os.sep + "example_content.html", 'rb') as fd:
            mock_content.return_value = fd.read()
        result_list = sophiabus230.get_next_buses(debug=True)
        self.assertEqual(len(result_list), 8)
        #TODO: add the expected tt's here (look at the logging stuff for the full list)
        for index in range(len(result_list)):
            if index > 2:
                actual_date = result_list[index]['bus_time']
                expected_date = self.expected[index]['bus_time']
                self.assertEqual(actual_date.year, expected_date.year)
                self.assertEqual(actual_date.month, expected_date.month)
                self.assertEqual(actual_date.day, expected_date.day)
                self.assertEqual(actual_date.hour, expected_date.hour)
                self.assertEqual(actual_date.minute, expected_date.minute)
            self.assertEqual(result_list[index]['dest'], self.expected[index]['dest'])
            self.assertEqual(result_list[index]['is_real_time'], self.expected[index]['is_real_time'])

    @patch('future.moves.urllib.request.urlopen')
    def test_get_html_from_cg06(self, mock_urlopen):
        parent_path = os.path.dirname(os.path.abspath(__file__))
        with open(parent_path + os.sep + "example_content.html", 'rb') as fd:
            mock_urlopen.return_value = fd
            sophiabus230._get_html_from_cg06(1939)
            assert mock_urlopen.called
            mock_urlopen.assert_called_once_with('http://cg06.tsi.cityway.fr/qrcode/?id=1939')
