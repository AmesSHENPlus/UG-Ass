# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 12:59:20 2018

@author: Ames SHEN
"""

import pandas as pd
import numpy as np
from pandas.plotting import scatter_matrix
import scipy
import statsmodels.formula.api as smf
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor as VIF

M = pd.read_csv('./MONEY.csv')
R = M.R[5:40].reset_index().R
M1 = M.M1
m = pd.DataFrame({'R':R,'M_0':M1[5:40].reset_index().M1,'M_1':M1[4:39].reset_index().M1,'M_2':M1[3:38].reset_index().M1,
                 'M_3':M1[2:37].reset_index().M1,'M_4':M1[1:36].reset_index().M1,'M_5':M1[0:35].reset_index().M1})
r_m5 = smf.ols('R~M_0+M_1+M_2+M_3+M_4+M_5',data=m).fit()
print(r_m5.summary().as_latex())
#anova table
table = sm.stats.anova_lm(r_m5, typ=2)
# plot variables' parameters
r_m5.params[1:7].plot(kind='bar')
scatter_matrix(m, alpha=1)
#vif
vif = pd.DataFrame()
vif["VIF Factor"] = [VIF(m.values, i) for i in range(m.shape[1])]
vif["features"] = m.columns
#F threshold
dist = scipy.stats.f(dfn=6,dfd=28)
f=dist.ppf(0.95)
