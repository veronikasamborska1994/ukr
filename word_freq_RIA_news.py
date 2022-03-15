#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 12:36:11 2022

@author: veronikasamborska
"""

import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter
import googletrans
from googletrans import Translator
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import random

"Function defining the web-crawler/core" 

 
def start():
    
    url = 'https://ria.ru/'
 
    # empty list to store the contents of
    # the website fetched from our web-crawler
    wordlist = []
    source_code = requests.get(url).text
 
    # BeautifulSoup object which will
    # ping the requested url for data
    soup = BeautifulSoup(source_code, 'html.parser')
  
    # Text in given web-page is stored under
    # the <div> tags with class <entry-content>
    for each_text in soup.findAll(class_ = 'share'):
        content = each_text['data-title']
                        
 
        # use split() to break the sentence into
        # words and convert them into lowercase
        words = content.lower().split()
        for each_word in words:
            wordlist.append(each_word)
            
    for each_text in soup.findAll(class_ = 'share m-light'):
        content = each_text['data-title']
                        
 
        # use split() to break the sentence into
        # words and convert them into lowercase
        words = content.lower().split()
        for each_word in words:
            wordlist.append(each_word)
               
    words,count = np.unique(wordlist, return_counts = True)
    war_words = []
    for word in words:
        if 'воев' in word or 'воен' in word:
            war_words.append(word)
            
    count_sort_ind = np.argsort(-count) 
    most_common = words[count_sort_ind][:100]
    number = count[count_sort_ind][:100]
       
    
    translator = Translator()
    word_list = []
    for word in most_common:
          translation = translator.translate(word)
          word_list.append(translation.text)
          
    text_to_plot = {}
    for i,ii in enumerate(word_list):
        text_to_plot[ii] =  number[i]
    
    
    # using word frequency list:
    #word_freq = open("/tmp/word_freq.txt").read()
    # say it looks like this:
    text = " ".join([(k + " ")*v for k,v in text_to_plot.items()])
    
    # Generate a word cloud image
    wordcloud = WordCloud(background_color="white", collocations=False).generate(text)
    plt.imshow(wordcloud.recolor(color_func=grey_color_func, random_state=3), interpolation='bilinear')
    plt.axis("off")
    


def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(0, 50)

