To test the program, simply run "SC.py" with python3. 
The test data is auto-generated through DataCreation.py and is already provided in the folder as data.csv. The default size of test data is from length 1 to 26. You can change the maximum length and regenerate the data in DataCreation.py. The suggested length is from 25 to 30 since the algorithm would take sigificant amount of time when the length gets larger. 

The estimated time complexity for this algorithm is O(2^n). Since there are always 2^n-1 possible combinations for a string consisting of n unique characters, O(2^n) is the lowest time complexity that can be achieved when there are no other constraints (e.g. repeat letters). 

The idea of this algorithm: (e.g. ABABA)

1) count the total number of each idividual letter (there are 3 As and 2 Bs in the example string)
2) group same letters together and reorder them as a dictionary, where the key is the letter and the value is the number of times it appears in the string (new dict: A: 3, B: 2)
3) label the keys with integers(0, 1, 2, ...) so that each key has a unique numbered label (A: 0, B: 1)
4) create an empty output list that has the length of the original string. (len = 5 in this example)
5) create a pivot for the output list and set it to 0 as default.
6) print the output list with range(0, pivot).
7) recursively go through each key by order; if the value is greater than 0, write down the key in output[pivot], minus the value by 1 and revisit step 6 and 7 with (pivot + 1). The value needs to be added back right after. If the value is 0, quit the current loop and proceed to the next key. The keys with lower numbers won't be visited again after the higher ones. 
8) The output of this example is:
A
AA
AAA
AAAB
AAABB
AAB
AABB
AB
ABB
B
BB

SC.py also provides a visulization method that shows the exponential time complexity of the algorithm. It outputs both the data points and a curve fit function. If the graph is not correctly shown, please run "python -m pip install -U matplotlib" to install the matplotlib library. 
*When the maximum data length is below 25, the noise might be too large and the curve fit function may fail. Please  ensure the max data length is between 25 to 30 for best performance. 

