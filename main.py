#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sophiabus230

for t in sophiabus230.get_next_buses(stop_id=1939, debug=True):
    bus_time = t['bus_time']
    dest = t['dest']
    rt = "theoretical"
    if t['is_real_time']:
        rt = "real time"
    print(u"Next bus at {0} to {1} ({2})".format(bus_time, dest, rt))
