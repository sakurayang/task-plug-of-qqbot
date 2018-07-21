# -*- coding: utf-8 -*-
from peewee import *

db = SqliteDatabase("/var/www/nextcloud/aic.db")

class AIC(Model):

    TITLE = TextField()
    TIMESCOOL = TextField()
    TRANSLATE = TextField()
    REVISION = TextField()
    TIMESCOOLDONE = IntegerField()
    TRANSLATEDONE = IntegerField()
    REVISIONDONE = IntegerField()

    class Meta:
        database = db