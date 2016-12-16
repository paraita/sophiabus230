#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sophiabus230

for t in sophiabus230.get_next_buses():
    bus_time = t['bus_time']
    dest = t['dest']
    print "Next bus at {0} to {1}".format(bus_time, dest)
