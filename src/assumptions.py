#!/usr/bin/env python
# coding: utf-8

# # Functions to Check Assumptions of LR Model

# This file contains functions that will help to check the assumptions of the Linear Regression Model: linearity, normality, homoscadasticity and independance.

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.diagnostic import linear_rainbow, het_breuschpagan
from statsmodels.stats.outliers_influence import variance_inflation_factor

from sklearn.preprocessing import LabelEncoder
import scipy.stats as stats


# 

# In[4]:


def assumptions (regres_model, regres):
    rainbow_statistic, rainbow_p_value = linear_rainbow(regres_model)
    print("LINEARITY CHECK\n")
    print("Rainbow statistic:", rainbow_statistic)
    print("Rainbow p-value:", rainbow_p_value)
    
    print("\nNORMALITY CHECK")
    fig = sm.graphics.qqplot(regres_model.resid, dist=stats.norm, line='45', fit=True)
    
    print("\nHOMOSCADASTICITY CHECK")
    
    y = regres["SalePrice"]
    y_hat = regres_model.predict()
    
    fig5, ax5 = plt.subplots(figsize=(10,10))
    ax5.set(xlabel="Predicted Sale Price",
        ylabel="Residuals (Predicted - Actual Sale Price)")
    ax5.scatter(x=y_hat, y=y_hat-y, color="blue", alpha=0.2);

    
    return

# In[ ]:




