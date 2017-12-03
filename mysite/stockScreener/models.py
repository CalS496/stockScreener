# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import stockScreener

class FinalList(models.Model):
    def list(self): 
        returnList = stockScreener.main()
        printList = "<html><body>Results List: %s.</body></html>" % returnList
        return HttpResponse(printList)

        
