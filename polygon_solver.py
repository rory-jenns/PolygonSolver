import itertools
import json
import sys

dict_list = ["dictionary1.json", "dictionary2.json"]

DICTIONARY = 1

## COMMAND LINE FORMAT
# python polygon_solver.py (str) available_letters (char) required_letter (int) min_size

def main():

    # error command line arguments
    argc = len(sys.argv)

    dictionary = dict_list[DICTIONARY]

    if argc <= 3:
        return 1
    # if argc > 4 and "true" == sys.argv[4]:
    #     dictionary = dict_list[0]

    available_letters = sys.argv[1]
    required_letter = sys.argv[2]
    min_size = sys.argv[3]
    max_size = len(available_letters)

    if len(required_letter) != 1:
        return 1
    try:
        min_size = int(min)
    except:
        return 1
    
    # start program
    
    with open(dictionary) as f:
        all_words = json.load(f)

    perms = []
    for i in range(min_size, max_size+1):
        perms = perms + list(itertools.permutations(available_letters, i))

    def validate(word):
        if not required_letter in word:
            return False
        if not word in all_words:
            return False
        return True

    valid = sorted(list(set(filter(validate, map(lambda x : "".join(x), perms)))), key=len)

    print(len(valid))
    print(valid)

main()
# LETTERS = "grievpeil"
# REQUIRED = 'l'
