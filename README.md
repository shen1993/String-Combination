To test the program, simply run "SC.py" with  python3. 

The estimated time complexity for this algorithm is O(2^n). Since there are always 2^n-1 possible combinations for a string consisting of n unique characters, O(2^n) is the lowest time complexity that can be achieved when there are no other constraints (e.g. repeat letters). 

The idea of this algorithm:

1) count the appearance times of each idividual letter
2) order the letters with integers
3) recursively go through each letter by order; the letters with lower numbers won't be visited again after the higher ones. 

SC.py also provides a visulization method that shows the exponential time complexity. If the graph is not correctly shown, please run "python -m pip install -U matplotlib" to install the matplotlib library. 


