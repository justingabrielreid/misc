#!/usr/bin/python
#Getting the current date and time
from datetime import datetime
now = datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day  
print 'Current year %s' % (current_year)
print 'Current month %s' %(current_month)
print 'Current day %s'%(current_day)
print 'Current time %s:%s:%s'%(now.hour,now.minute,now.second)

