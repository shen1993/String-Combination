import random
import string


class DataCreation:

    def __init__(self, max_length):
        self.generate_data(max_length)

    # generate random Capitalized letters for test
    def generate_data(self, max_length):
        with open('data.csv', 'w') as f:
            for i in range(1, max_length + 1):
                letters = string.ascii_uppercase
                f.write(''.join(random.choice(letters) for i in range(i)) + '\n')


dc = DataCreation(26) # suggest length of data: from 25 to 30

