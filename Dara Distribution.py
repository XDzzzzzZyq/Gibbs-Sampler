import numpy as np
from scipy.stats import invgamma
from scipy.stats import norm

Daily_opening = []
Daily_closing = []

import csv
file_path = 'd:/STATS PROJECT/Project/HistoricalData.csv'
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        
        if row[0] == "Date":
            continue
        open = float(row[3])
        Daily_opening.append(open)
        close = float(row[1])
        Daily_closing.append(close)
           
Daily_return = []        
for i in range(len(Daily_opening) ):
    today_opening = float(Daily_opening[i])
    today_closing = float(Daily_closing[i])
    daily_return = (today_closing - today_opening)/today_opening
    Daily_return.append(round(daily_return, 2))
    
sum = 0
for i in Daily_return:
    sum += i
   
   
    
        
mu  = sum / len(Daily_return)   
diff = 0
for i in Daily_return:
    diff += (i - mu)**2
sigma = diff / len(Daily_return)
mu_var = 1000
mu_mean = 0
a = 0.0001
b = 0.0001
mean = []
variance = []
    
def Get_Mean (Pri_m,Pri_v,data):
    Post_m = (sigma * Pri_m + Pri_v * data)/(sigma + Pri_v)
    Post_v = sigma * Pri_v/(sigma + Pri_v)
    return [Post_m, Post_v]

def Draw_Normal (mean, variance):
    return norm.rvs(mean, (variance) ** (1/2))

def Get_Variance (Pri_a, Pri_b, data):
    Post_a = Pri_a + 1/2
    Post_b = Pri_b + ((data - mu) ** 2)/2
    return [Post_a, Post_b]

def Draw_InvGamma (a, b):
    return invgamma.rvs(a, b)

for i in range(len(Daily_return)):
    mean = Get_Mean(mu_mean, mu_var, Daily_return[i])
    mu_mean = mean[0]
    mu_var = mean[1]
    mu = Draw_Normal(mu_mean, mu_var)
    variance = Get_Variance(a, b, Daily_return[i])
    a = variance[0]
    b = variance[1]
    sigma = Draw_InvGamma(a, b)
print(mean)
print("Mean: " + str(mu * 100) + "%, Variance: " + str(sigma))    



