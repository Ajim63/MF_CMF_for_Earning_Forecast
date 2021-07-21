#definations

import numpy as np
import pandas as pd



def per_miss(File):
    # Calculate the percentage of missing value in a data file
     return File.isnull().sum().sum()/(File.shape[0]*File.shape[1])

def MSE(original, imputed):
    # calculate Mean Squared Error
    return np.square(original-imputed).mean().mean()

def MPE(y_true, y_pred, threshold=0.01):
    v = np.copy(y_true)
    np.place(v, v==0, threshold)
    #v = np.clip(np.abs(y_true), threshold, None)
    diff = np.abs((y_true - y_pred) / v)
    return np.mean(diff, axis=-1).mean()


def MPE_2(y_true, y_pred, threshold=0.01):
    diff = np.abs(y_true - y_pred)
    return np.mean(diff, axis=-1).mean()


def Creat_missing(File, Perc):
    X = File.copy()
    for col in X:
        vals_to_nan = X[col].dropna().sample(frac= Perc).index
        X.loc[vals_to_nan, col] = np.NaN
    return X

"""
def R_squared_2(original, predicted):
    Differ = np.square(original-predicted)
    denom = np.square(original)
    R_sq = 1 - ((Differ.sum())/denom.sum())
    return R_sq
"""

def R_squared(original, predicted):
    Differ = np.square(original-predicted)
    m = np.mean(original)
    denom = np.square(original - m)
    R_sq = 1 - ((Differ.sum())/denom.sum())
    return R_sq


def Get_performance(Y_true, Y_pred):
    print ("R2 : ", np.round(R_squared(Y_true, Y_pred), 5))
    print ("MSE",  np.round(MSE(Y_true, Y_pred), 5))
    print ("MAPE", np.round(MPE(Y_true, Y_pred), 5)*100)
    
    
def create_W_matrix(Data):
    # create the 0,1 matrix for missing and non missing values
    X = Data.values.copy()
    for i in range (0, X.shape[0]):
        for j in range (0, X.shape[1]):
            if np.isnan(X[i,j]) == True:
                X[i,j] = 0
            else:
                X[i,j] = 1
    return X

def create_ori_W_nan(Data):
    # create the NAN,1 matrix for missing and non missing values
    X = Data.values.copy()
    for i in range (0, X.shape[0]):
        for j in range (0, X.shape[1]):
            if np.isnan(X[i,j]) == False:
                X[i,j] = 1
    return X
    
    
    
def Zero_impute(data):
    X = data.copy().fillna(0)
    return X
    
def random_walk(X_Data, Y_data):
    # create the 0,1 matrix for missing and non missing values
    #concatenate actual eps for next quarter to replace missing values, at the last columns
    X = np.concatenate((X_Data.drop(X_Data.head(1).index).values, Y_data.drop(Y_data.tail(1).index).values), axis=1)
    for i in range (0, X.shape[0]):
        for j in range (0, X.shape[1]):
            if np.isnan(X[i,j]) == True:
                X[i,j] = X[i,-1]
    #return only the forecast, by avoiding concatenated actual value
    return X[:,:-1]


def Evaluate_performance(imputed_data, original_data):
    W = create_W_matrix(original_data)
    ori = np.nan_to_num(original_data.values)
    Imputed = imputed_data*W
    Imputed = np.nan_to_num(Imputed)
    Get_performance(ori, Imputed)