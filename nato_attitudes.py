#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 14:50:55 2022

@author: veronikasamborska
"""




import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
from palettable import wesanderson as wes

colors = wes.Moonrise5_6.mpl_colors+wes.Royal2_5.mpl_colors



nato = pd.read_excel('/Users/veronikasamborska/Desktop/nato support in ukraine.xlsx')

year = nato['Year']
for_ = nato['for']
against = nato['against']
arrowprops = dict(arrowstyle="wedge,tail_width=0.5", alpha=0.7, color='grey')

plt.plot(for_, label = 'for NATO', color = colors[0], linewidth = '2')
plt.plot(against, label = 'against NATO',color = colors[1],linewidth = '2')
plt.xticks(np.arange(len(year)),year)
plt.xticks(rotation=45)
plt.ylabel('%')
plt.legend(frameon=False)
plt.xlabel('Year')
invade = for_[np.where(year==2014)[0]]
invade_2 = against[np.where(year==2014)[0]]

plt.vlines(12.1,ymin = 0,ymax = 70, linestyle = '--')
plt.text(x =11.6, y = 30,s = 'Russia invades Ukraine', rotation = 90)
# label_frac_x = 0.35
# label_frac_y = 0.4

# plt.annotate('Russia invades Ukraine',
#               xy=(12, invade_2),
#               xytext=(label_frac_x,label_frac_y+0.009), 
#               textcoords='axes fraction',
#               size=8,
#               ha='center', va="center",
#               arrowprops=dict(arrowstyle="-|>",
#                       connectionstyle="arc3,rad=-0.3",
#                       fc="w"), rotate ='90')




# plt.annotate('Russia invades Ukraine',
#              xy=(12, invade_2),
#              xytext=(label_frac_x,label_frac_y+0.009), 
#              textcoords='axes fraction',
#              size=8,
#              ha='center', va="center",
#              arrowprops=dict(arrowstyle="-|>",
#                       connectionstyle="arc3,rad=-0.3",
#                       fc="w"))

# plt.annotate('',
#              xy=(12, invade),
#              xytext=(label_frac_x,label_frac_y+0.001), 
#              textcoords='axes fraction',
#              size=10, 
#              ha='center', va="center",
#              arrowprops=dict(arrowstyle="-|>",
#                       connectionstyle="arc3,rad=0.3",
#                       fc="w"))
sns.despine()
plt.tight_layout()