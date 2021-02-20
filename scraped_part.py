# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 17:03:34 2021

@author: admin
"""        


import json
import pandas as pd
import requests
from datetime import date, timedelta
import numpy as np
import os
import sys


def daterange(date1, date2):
    '''
    
    Parameters
    ----------
    date1 : date.datetime 
        This is the starting date in the range of dates.
        
    date2 : date.datetime
        This is the Ending date in the range of dates.

    Yields
    ------
    The output of this function is range of dates from date1 to date2.
    Ex: daterange((2021/02/01),(2021/02/17)) will returns all the dates between 
    the provided range of dates as an input to the function. 

    '''
    
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

# =============================================================================
# 
# =============================================================================


def cric(url):
    """
    
    Parameters
    ----------
    url : Https URL
     This Url help us to connect with the ICC cricket api to send the request
     and recieve the desired output which is reflected as an output of this
     Function.

    Returns
    -------
    A List of Lists containing the scrapped content for the provided Format,
    Details such as Full_Name and Nationality will be collected from the page.

    """
    
    s = json.loads(requests.get(url).content.decode("utf8"))
    P = s['content']
    Z = pd.DataFrame(P)
    S3 = pd.DataFrame(Z["player"].to_list())
    rec_cols = ["fullName","nationality"]
    S3 = S3[rec_cols] 
    return(S3)

# =============================================================================
# 
# =============================================================================


def type(var):
    """
    
    Parameters
    ----------
    var : str
    This varibale contains only three types of inputs (i.e bat,bowl,allround)

    Returns
    -------
    A URL which help in scraping the type of content you had choosen while 
    providing input to the function (i.e bat,bowl,allround)

    """
    
    stype =  {"BAT" :'https://cricketapi-icc.pulselive.com/icc-ratings/ranked/players/odi/bat?pageSize=100&dmsPlayerIdRequired=true&at=',
    "BOWL": 'https://cricketapi-icc.pulselive.com/icc-ratings/ranked/players/odi/bowl?pageSize=100&dmsPlayerIdRequired=true&at=',
    "ALL_ROUNDER" : 'https://cricketapi-icc.pulselive.com/icc-ratings/ranked/players/odi/allround?pageSize=20&dmsPlayerIdRequired=true&at='}
    return(stype[var])

# =============================================================================
# 
# =============================================================================

# def apenddata():    
#     if os.path.exists(str(format_type) + "_" + str(date(year,month,day).strftime('%y-%m-%d')) +'.csv') != True:
#         dataframe.to_csv(str(format_type) + "_" + str(date(year,month,day).strftime('%y-%m-%d')) +'.csv',index = False, encoding = 'utf-8')
#     else:    
        
#     return(dataframe)


# =============================================================================
# 
# =============================================================================

def scrapd(year,month,day, format_type):
    """
    
    Parameters
    ----------
    year : int
        starting Year from which the scraping of content begins.
    month : int
        starting Month from which the scraping of content begins.
    day : int
        starting day from which the scraping of content begins.
    format_type : str
     This varibale contains only three types of inputs (i.e bat,bowl,allround).

    Returns
    -------
    A dataframe with columns [Rank,Date,Player,Nationality] and the respective 
    contents that are recieved and scraped from the ICC api.

    """

    os.chdir(os.path.dirname(os.path.abspath('__file__')))
    data_list = []
    for dt in daterange(date(year,month,day),date.today()):
        dates = dt.strftime("%Y-%m-%d")
        url = type(format_type)+str(dates)
        df = cric(url)
        df['date'] = dates
        try :
            df['Rank'] = np.arange(1,101)
        except sys.exc_info()[0]:
            df['Rank'] = np.arange(1,21)
        df = df.iloc[:,[3,2,0,1]]
        data_list.append(df)
        dataframe = pd.concat(data_list)
        # for download ### dataframe.to_csv(str(format_type) + "_" + str(date(year,month,day).strftime('%y-%m-%d')) +'.csv',index = False, encoding = 'utf-8')
    return(dataframe)


# =============================================================================
# 
# =============================================================================

# bats = scrapd(2021,2,1,'BAT')
# bowls = scrapd(2016,1,1,'bowl')
# allround = %time scrapd(2016,1,1,'allround')











