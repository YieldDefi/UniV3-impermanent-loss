
#!/usr/bin/env python3
import math
from random import random
#Standard Normal variate using Box-Muller transform.
def random_bm(mu, sigma):
    u = 0
    v = 0
    while(u == 0): 
        u = random() #Converting [0,1) to (0,1)
    while(v == 0): 
        v = random()
    mag = sigma * math.sqrt( -2.0 * math.log( u ) )
    return mag * math.cos( 2.0 * math.pi * v ) + mu
def calcImpLoss(lowerLimit, upperLimit, px):
    r = math.sqrt(upperLimit/lowerLimit)
    a1 = (math.sqrt(r) - px)
    a2 = (math.sqrt(r) / (math.sqrt(r) - 1)) * (2*math.sqrt(px) - (px + 1))
    a3 = (math.sqrt(r) * px - 1)
    if(px < 1/r):
        return a3
    elif(px > r): 
        return a1
    
    return a2;
def calcExpImpLoss(rangePerc, mu, sigma) :
    upperPx = 1 + rangePerc
    lowerPx = 1 / upperPx
    Vhsum = 0
    impLossSum = 0
    iterations = 10000
    for i in range(iterations) :
        t = 1
        W = random_bm(0, 1) * math.sqrt(t-0)
        X = (math.log(1 + mu) - 0.5 * math.pow(math.log(1 + sigma), 2)) * t + math.log(1 + sigma) * W
        _px = math.exp(X)
        Vhsum += 1 + _px
        impLossSum += calcImpLoss(lowerPx, upperPx, _px)
    
    return (impLossSum/iterations)/(Vhsum/iterations)

rangePerc = 0.1 #the percentage of price range for which you want to calcultae the IL
#example:  if you want to calculate the impermanent loss for a price
#range that goes from 90% to 110% of the initial price, rangePerc should be set to 0.1 (or 10%).
mu = math.log(1) #the expected return of the pair of tokens. This is the logarithm 
#of the ratio between the final and initial prices of the pair. For example, 
#if the initial price is 1 and the final price is 1.1 (i.e., a 10% increase),
# mu should be set to math.log(1.1).
sigma = 0.2 # the volatility of the pair of tokens. 
#This is the standard deviation of the logarithmic returns of the pair.
# For example, if the logarithmic returns of the pair follow a normal distribution
# with a standard deviation of 0.3, sigma should be set to 0.3.
expected_imp_loss = calcExpImpLoss(rangePerc, mu, sigma)
print(expected_imp_loss)