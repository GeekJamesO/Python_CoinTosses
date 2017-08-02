# Assignment: Coin Tosses
# Write a function that simulates tossing a coin 5,000 times.
# Your function should print how many times the head/tail appears.
#
# Sample output should be like the following:
#
# Starting the program...
#  Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
#  Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
#  Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
#  Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
# ...
# Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
# Ending the program, thank you!
# Hint: Use the python built-in round function to convert that floating point number into an integer
import random
def CoinTosses(numOfTosses = 5000):
    SumOfHeads = 0.0;
    SumOfTails = 0.0;
    for aToss in range(1, numOfTosses + 1):
        x_rounded = round(random.random());
        if (x_rounded == 1):
            value = "head"
            SumOfHeads += 1
        else:
            value = "tail"
            SumOfTails += 1
        print "Attempt #{0}: Throwing a coin... It's a {1}! ... Got {2} head(s) so far and {3} tail(s) so far".format(aToss, value, SumOfHeads, SumOfTails)
    PercentOfHeads = ( SumOfHeads * 100 ) / (SumOfHeads + SumOfTails)
    print "Percent of heads = {0}".format(PercentOfHeads)
print "Function CoinToss"
CoinTosses()
