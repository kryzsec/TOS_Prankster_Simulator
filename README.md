# TOS_Prankster_Simulator
A suggested TOS role of prankster would be super overpowered.


# Running

This project requires python 3 and takes no command line arguments. This file does not use a config file and thus all edits must occur in the source itself.

# Role Explanation

Each night you visit a person, then you have a 75% chance of pranking them and a 25% chance of killing them. If you successfully prank 3 people you win. [here is the reddit thread](https://www.reddit.com/r/TownofSalemgame/comments/ca8o4d/i_hope_no_one_has_made_a_similar_role_idea_if/)

# Example Output of 1,000,000 tests:

```
Day 3: 422036 | 42.20%
Day 4: 316154 | 31.62%
Day 5: 158277 | 15.83%
Day 6: 65840 | 6.58%
Day 7: 24857 | 2.49%
Day 8: 8724 | 0.87%
Day 9+ 4112 | 0.41%
```

# Example Output of 100,000,000 tests:

```
Day 3: 42177507 | 42.18%
Day 4: 31642741 | 31.64%
Day 5: 15824082 | 15.82%
Day 6: 6595952 | 6.60%
Day 7: 2473345 | 2.47%
Day 8: 864593 | 0.86%
Day 9+ 421780 | 0.42%
```

# Theoretical Values
```
Day 3: 42.19%
Day 4: 42.19%
Day 5: 26.37%
Day 6: 13.18%
Day 7:  5.77%
Day 8:  2.31%
Day 9:  0.87%
```

Note that the theoretical values do not match up with the simulated values, that is because they are each a measure of something slightly different but both descrie the same thing. The product of the theoretical values multiplied by the test population will result in approximately the simulated test population values. 

# Formula for calcualting theoretical values
<b><i>P(y) = nCy×p<sup>y</sup>q<sup>n-y</sup></i></b>

Where: 
```
n = the number of attempts
y = the number of successes (3)
p = the probability of a success (0.75)
q = the probability of a failure (0.25)
```


# Probabilistic Comparison to the pirate

```
p(n) = 1 − ((2/3)^(n−1))(2/3+n/3) where p(n) is the probability given a number of attempts
Day     Chance    Rate        Cumulative
Day 2: 	11%       11.00%      11%
Day 3: 	26%       23.14%      34.14%
Day 4: 	40%       26.34%      60.48%
Day 5: 	54%       21.33%      81.81%
Day 6: 	65%       11.80%      93.61%
Day 7: 	74%        4.71%      98.32%
Day 8: 	80%        1.32%      99.64%
```

The pirate is the most similar role to the suggested prankster, though it is slightly more complicated. The chance is the total percentage of winning on that given attempt, the rate is the percentage of people expected to win on said chance... The cumulative column says the total percentage of players that would have been expected to theoretically win by a given day, meaning by day 5 (or rather attempt 5) 81% of pirate players are expected to have already won, and the prankster is at 89.63% by day 5.
