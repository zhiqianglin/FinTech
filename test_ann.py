# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print('hello world')

print('haha')
"""
!git pull
!git add test_ann.py # this step can be ignored
!git commit -m "add"
!git push -u origin master
"""
import pandas as pd
df_th=pd.read_csv('transactionhistory.csv')

# extract recent transactions
df_th_recent=df_th[df_th['date']>20161001]
# extract dining transactions
df_th_recent_dining=df_th_recent[df_th_recent['eventCategory']==1]
# personal transaction summary
df_summary=df_th_recent_dining[['amount','accountId','merchant','postalCode']].groupby(['accountId','merchant','postalCode']).agg(['sum', 'count'])
