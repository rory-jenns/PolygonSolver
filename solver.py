import itertools
import json

DICT1 = "dictionary1.json" # Bigger
DICT2 = "dictionary2.json" # Smaller

DICTIONARY = DICT2

LETTERS = input("All Letters: ")
REQUIRED = input("Required Letter: ")
  
with open(DICTIONARY) as f:
    all_words = json.load(f)

available_letters = LETTERS if DICTIONARY == DICT1 else LETTERS.upper()
required_letter = REQUIRED if DICTIONARY == DICT1 else REQUIRED.upper()
min_size = 4
max_size = len(available_letters)

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
input()

# LETTERS = "grievpeil"
# REQUIRED = 'l'
