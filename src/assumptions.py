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


def linear (regres_model):
    rainbow_statistic, rainbow_p_value = linear_rainbow(regres_model)
    print("Rainbow statistic:", rainbow_statistic)
    print("Rainbow p-value:", rainbow_p_value)
    
    return


def normal (regres_model):  
    fig = sm.graphics.qqplot(regres_model.resid, xlabel = 'Theoretical Quantiles',
                             ylabel= 'Sample Quantiles', dist=stats.norm, line='45', fit=True)
    
    return
# In[ ]:

def homoscad (regres_model, regres):
    
    y = regres["SalePrice"]
    y_hat = regres_model.predict()
    
    fig5, ax5 = plt.subplots(figsize=(7,7))
    ax5.set(xlabel="Predicted Sale Price",
        ylabel="Residuals (Predicted - Actual Sale Price)")
    ax5.scatter(x=y_hat, y=y_hat-y, alpha=0.2);
    
    return

def bpag_test(regres_model, df, target):
    
    cols = df.columns[1:]
    y = df[target]
    y_hat = regres_model.predict()
    lm, lm_p_value, fvalue, f_p_value = het_breuschpagan(y-y_hat, df[cols])
    print('Lagrange Multiplier p-value:', lm_p_value)
    print('F-statistic p-value:', f_p_value)
    
    return

def inverse_log(regres_model, predictor, percent):
    
    for pr in predictor:
        print(round(regres_model.params[pr]*np.log(1+percent),2))
        
    return


def indep(df):
    
    cols = df.columns[1:]
    rows = df[cols].values
    indep_df = pd.DataFrame()
    indep_df["VIF"] = [variance_inflation_factor(rows, i) for i in range(len(cols))]
    indep_df["feature"] = cols
    
    return indep_df

def mapper_heat(df, column, number, lookup):
    df_temp = lookup[(lookup.LUType == number)]
    dict1 = dict(df_temp[['LUItem', 'LUDescription']].values)
    df.HeatSystem.map(dict1)
    df.reset_index(inplace=True, drop=True)
    df['temp'] = df.HeatSystem.map(dict1)
    df[column] = df.temp
    df.drop('temp', axis=1, inplace=True)

    return 

def formula (df, target):
    
    features = df.drop(target, axis=1).columns
    features = "+".join(features)
    return target + "~" + features



def forward_selected(data, response):
    """Linear model designed by forward selection.

    Parameters:
    -----------
    data : pandas DataFrame with all possible predictors and response

    response: string, name of response column in data

    Returns:
    --------
    model: an "optimal" fitted statsmodels linear model
           with an intercept
           selected by forward selection
           evaluated by adjusted R-squared
    """
    remaining = set(data.columns)
    remaining.remove(response)
    selected = []
    current_score, best_new_score = 0.0, 0.0
    while remaining and current_score == best_new_score:
        scores_with_candidates = []
        for candidate in remaining:
            formula = "{} ~ {} + 1".format(response,
                                           ' + '.join(selected + [candidate]))
            score = ols(formula, data).fit().rsquared_adj
            scores_with_candidates.append((score, candidate))
        scores_with_candidates.sort()
        best_new_score, best_candidate = scores_with_candidates.pop()
        if current_score < best_new_score:
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_new_score
    formula = "{} ~ {} + 1".format(response,
                                   ' + '.join(selected))
    model = ols(formula, data).fit()
    return model









                        
