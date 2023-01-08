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
        print("too few args")
        return 1
    # if argc > 4 and "true" == sys.argv[4]:
    #     dictionary = dict_list[0]

    available_letters = sys.argv[1].upper()
    required_letter = sys.argv[2].upper()
    min_size = sys.argv[3]
    max_size = len(available_letters)

    debug = False

    if argc >= 5:
        debug = True

    if debug:
        print(available_letters, required_letter, min_size)

    if len(required_letter) != 1:
        print("required must be one")
        return 1
    try:
        min_size = int(min_size)
    except:
        print("cannot make min size an int")
        return 1
    
    # start program
    
    with open(dictionary) as f:
        all_words = json.load(f)
        if debug:
            all_words["hello"]
        
    def validate(word):
        if not required_letter in word:
            return False
        if not word in all_words:
            return False
        return True

    valid = []
    for i in range(min_size, max_size+1):
        i_perms = list(itertools.permutations(available_letters, i))
        i_perms = list(set(map(lambda x : x.lower(), list(filter(validate, map(lambda x : "".join(x), i_perms))))))
        valid.extend(i_perms)

        print(i,":",i_perms)

    # valid = sorted(list(set(filter(validate, map(lambda x : "".join(x), perms)))), key=len)

    print(len(valid), "Words Found")
    # print(list(map(lambda x : x.lower(), valid)))

main()
# LETTERS = "grievpeil"
# REQUIRED = 'l'
