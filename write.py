#coding:utf-8
#!/usr/bin/python
from db import *
import sys
import getopt

db.connect()
db.create_tables([AIC])

opts, args = getopt.getopt(sys.argv[1:], "htitle:time:trans:revi")			
	# title -> 标题 (title)
	# time  -> 时轴 (time scool)
	# trans -> 翻译 (translate)
	# revi  -> 校对 (revision)
	# done  -> 完成 (0->没有 1->完成)

a = sys.argv
AIC.create(
	TITLE=a[1],
	TIMESCOOL=a[2],
	TRANSLATE=a[3],
	REVISION=a[4],
	TIMESCOOLDONE=0,
	TRANSLATEDONE=0,
	REVISIONDONE=0).save()
