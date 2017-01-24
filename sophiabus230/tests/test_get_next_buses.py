#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
import os
from datetime import datetime
from datetime import timedelta
import sophiabus230
from dateutil.tz import gettz
from mock import patch


class TestSophiabus230(TestCase):

    @patch('sophiabus230._get_html_from_cg06')
    def test_get_next_buses(self, mock_content):
        parent_path = os.path.dirname(os.path.abspath(__file__))
        with open(parent_path + os.sep + "example_content.html", 'rb') as fd:
            mock_content.return_value = fd.read()
        tz_paris = gettz('Europe/Paris')
        result_list = sophiabus230.get_next_buses(debug=True)
        expected_bus_time = datetime.now(tz=tz_paris) + timedelta(minutes=9)
        assert len(result_list) == 1
        actual_dest = result_list[0]['dest']
        actual_is_real_time = result_list[0]['is_real_time']
        actual_bus_time = result_list[0]['bus_time']
        expected_dest = u'Cathédrale-Vieille Ville'
        expected_is_real_time = True
        self.assertEqual(actual_dest, expected_dest)
        assert actual_is_real_time == expected_is_real_time
        assert actual_bus_time.year == expected_bus_time.year
        assert actual_bus_time.month == expected_bus_time.month
        assert actual_bus_time.day == expected_bus_time.day
        assert actual_bus_time.hour == expected_bus_time.hour
        assert actual_bus_time.minute == expected_bus_time.minute
