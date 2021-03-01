# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 12:18:38 2021

@author: admin
"""

import streamlit as st
from scraped_part import *
import datetime
st.title(' ICC ODI Player Rankings')

date = st.sidebar.date_input('start date', None) #datetime.date(2021,02,17)
format_type = st.sidebar.selectbox('Format Type', ['BAT','BOWL','ALL_ROUNDER'])
dataa = scrapd(date.year,date.month,date.day,format_type)
x = st.sidebar.selectbox('Teams', ["ALL","AUS", "ENG", "NZ", "SA"])
if x == 'ALL':
    st.dataframe(dataa)
else:
    st.dataframe(dataa[dataa['nationality'] == x])
st.write(f"You're looking at {x} players")




# =============================================================================
# Below are dumps but these snippets can be used later so let them stay here or 
# in another script
# =============================================================================




# data = pd.read_csv('D:\\admin\\Ext Projects\\ICC Scraping\\CSvs\\final.csv').head(1000)
# st.dataframe(data)

# XX = pd.DataFrame(
#     np.random.randn(10, 20),
#     columns=('col %d' % i for i in range(20)))

# st.dataframe(XX.style.highlight_max(axis=0))

# x = st.slider('x')  # 👈 this is a widget
# st.write(x, 'squared is', x * x)



# # Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )

# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )

# def _max_width_():
#     max_width_str = f"max-width: 2000px;"
#     st.markdown(
#         f"""
#     <style>
#     .reportview-container .main .block-container{{
#         {max_width_str}
#     }}
#     </style>    
#     """,
#         unsafe_allow_html=True,
#     )


# _max_width_()

# left_column, right_column = st.beta_columns(2)

# You can use a column just like st.sidebar:
# left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     chosen = st.radio(
#         'Teams',
#         ("AUS", "ENG", "NZ", "SA"))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
