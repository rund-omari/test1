# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 14:31:08 2025

@author: SDK
"""

import streamlit as st 
from dataread import data
st.title("data")
st.table(data)
