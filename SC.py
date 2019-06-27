import timeit
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


class SC:

    test_mode = False
    output_size = 6
    data_list = []
    runtime_list = []

    def __init__(self, test_mode = False, output_size = 6):

        self.test_mode = test_mode
        self.output_size = output_size
        print("Test mode: {}".format(test_mode))
        self.load_data()
        for i in range(len(self.data_list)):
            char_dict, char_pivot = self.count_chars(self.data_list[i])
            self.sc_algorithm(self.data_list[i], char_dict, char_pivot)
        self.visualization()

    # load test data from data.csv
    def load_data(self):
        with open('data.csv', 'r') as f:
            for line in f:
                self.data_list.append(line.strip('\n'))
            if self.test_mode:
                print("Data list: {}".format(self.data_list))

    # count the number of distinct chars in the string
    def count_chars(self, s):

        char_dict = {}
        for char in s:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        if self.test_mode:
            print("Count chars: {}".format(char_dict))
        char_pivot = list(char_dict)
        return char_dict, char_pivot

    # the string combination algorithm
    def sc_algorithm(self, s, char_dict, char_pivot):

        output = [None] * len(s)

        if len(char_pivot) < self.output_size:
            print("String combinations of {}:".format(s))
        else:
            print("String combinations of {}: "
                  "\nOutput omitted for strings longer than {}; "
                  "to output results of longer strings, please reset output_size".format(s, self.output_size - 1))
        start = timeit.default_timer()
        self.search_combination(char_dict, char_pivot, 0, output, 0)
        stop = timeit.default_timer()
        self.runtime_list.append(stop - start)
        print("String length: {};  Run time: {}(s)".format(len(s), stop - start))

    # the recursive method for sc algorithm
    def search_combination(self, char_dict, char_pivot, start_point, output, curr_pivot):

        if len(char_pivot) < self.output_size and curr_pivot != 0:
            print("".join(output[0:curr_pivot]))

        for i in range(start_point, len(char_pivot)):
            if char_dict[char_pivot[i]] == 0:
                continue
            output[curr_pivot] = char_pivot[i]
            char_dict[char_pivot[i]] -= 1
            self.search_combination(char_dict, char_pivot, i, output, curr_pivot + 1)
            char_dict[char_pivot[i]] += 1

    # a visualization graph showing the time complexity of the algorithm
    def visualization(self):

        # The estimated time complexity is exponential (2^n)
        def func(x, a, b, c):
            return a * np.exp(b * x) + c

        x_data = np.arange(1, len(self.runtime_list) + 1)
        y_data = self.runtime_list
        plt.scatter(x_data, y_data, s=5, color = 'b')
        plt.plot(x_data, y_data, 'b', label='data')

        # popt: the optimal parameters
        popt, pcov = curve_fit(func, x_data, y_data)
        plt.plot(x_data, func(x_data, *popt), 'r', label='fit')
        plt.xlabel('String length')
        plt.ylabel('Time (in seconds)')
        plt.legend()
        plt.title('Time Complexity Visualization')
        plt.show()

# The first argument is for test mode purpose;
# The second argument is for output purpose. It determines the maximum output size.
sc = SC(False, 6)
