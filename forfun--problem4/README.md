This problem goal is find the longest `0` between `1`

so we convert the number to the binary and cut 2 char off (0b)
from this method we gonna get the number that start with `1`
so we loop check the char in this binary if we found `0` we add the `current_gap` for 1
if we found `1` we check that `current_gap` is the biggest or not if not set the `current_gap` to 0 , if yes set `max_gap` to `current_gap` , run the loop until run out off char in binary
and return the `max_gap` 

to use the program , the user can run it through terminal by this command `python -m unittest binaryGap.py` or using the VSCode
