#!/usr/bin/env python2
#!-*- encoding: cp949 -*-

from pygooglechart import PieChart3D

chart = PieChart3D(250, 100)
chart.add_data([20, 10])
chart.set_pie_labels([u'�ȳ�'.encode('utf-8'), u'����'.encode('utf-8')])
print chart.get_url()
chart.download('pie_ko.png')
