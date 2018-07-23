# -*- coding: utf-8 -*-
r"""
	                        _ooOoo_
                           o8888888o
                           88" . "88
                           (| -_- |)
                            O\ = /O
                        ____/`---'\____
                      .   ' \\| |// `.
                       / \\||| : |||// \
                     / _||||| -:- |||||- \
                       | | \\\ - /// | |
                     | \_| ''\---/'' | |
                      \ .-\__ `-` ___/-. /
                   ___`. .' /--.--\ `. . __
                ."" '< `.___\_<|>_/___.' >'"".
               | | : `- \`.;`\ _ /`;.`/ - ` : | |
                 \ \ `-. \_ __\ /__ _/ .-` / /
         ======`-.____`-.___\_____/___.-`____.-'======
                            `=---='

         .............................................
                  佛祖镇楼                  BUG辟易
"""
from .db import *
db.connect()
db.create_tables([AIC])

def onQQMessage(bot, contact, menber, content):
	if content == '-task':
		bot.SendTo(contact, '请用\'-task:类型\'来看任务，例如：-task:time(对，目前只能看)')
		data = AIC.select().where((AIC.TIMESCOOLDONE == 0) or (AIC.TRANSLATEDONE == 0) or (AIC.REVISIONDONE == 0))
		if not data:
			bot.SendTo(contact, '现在暂时没有任务哟~各位辛苦了(OvO)b~')
			return
		for undo in data:
			bot.SendTo(contact, undo.TITLE)	
	
	elif content == '-task:time':
		data = AIC.select().where(AIC.TIMESCOOLDONE == 0)
		if not data:
			bot.SendTo(contact, '无')
			return
		for undo in data:
			bot.SendTo(contact, '时轴： %s' % undo.TITLE)
	
	elif content == '-task:tran':
		data = AIC.select().where(AIC.TRANSLATEDONE == 0)
		if not data:
			bot.SendTo(contact, '无')
			return
		for undo in data:
			bot.SendTo(contact, '翻译：%s : %s' % (undo.TIMESCOOL, undo.TITLE))
	
	elif content == '-task:revi':
		data = AIC.select().where(AIC.REVISIONDONE == 0)
		if not data:
			bot.SendTo(contact, '无')
			return
		for undo in data:
			bot.SendTo(contact, '校对：%s：%s' % (AIC.TRANSLATE, undo.TITLE))
	elif content.startWith('-task:time'):
		data = AIC.select().where(AIC.TIMESCOOLDONE == 0)
		arg = content[10:]
		#例如-time:task:xxx,则arg=xxx
		#然后遍历数据库，找到TITLE=xxx的。把那一行的TRANSLATE UPDATE为contact
		#也可以这么来 
		# if content.startWith('-task')
		#	arg = content[5:]
		#	if arg == ‘:time’
		#		...and so on
	elif content == '-all':
		data = AIC.select()
		if not data:
			bot.SendTo(contact, '无')
			return
		for undo in data:
			bot.SendTo(contact, '%s | 时轴：%s 翻译：%s 校对：%s' % (undo.TITLE, undo.TIMESCOOL, undo.TRANSLATE, undo.REVISION))
	
	elif content == '-hello':
		bot.SendTo(contact, 'hello')

	elif content == '-Q':
		bot.SendTo(contact, '花Q')
	