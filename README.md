# UniV3-impermanent-loss
Python Code to simulate Univswap V3 Impermanent Loss 
Everything is taken from this gamma swap paper https://medium.com/gammaswap-labs/expected-impermanent-loss-in-uniswap-v2-v3-7fb81033bd81


Simply copy the Impermanent Loss UniV3.py

The input are expressed at the end of the code:

rangePerc is the percentage of price range for which you want to calcultae the IL
example:  if you want to calculate the impermanent loss for a price range that goes from 90% to 110% of the initial price, rangePerc should be set to 0.1 (or 10%).

mu is he expected return of the pair of tokens. This is the logarithm 
of the ratio between the final and initial prices of the pair. For example, if the initial price is 1 and the final price is 1.1 (i.e., a 10% increase), mu should be set to math.log(1.1).

sigma is the volatility of the pair
