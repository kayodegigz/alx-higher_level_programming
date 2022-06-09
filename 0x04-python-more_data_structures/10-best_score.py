#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        for k, v in a_dictionary.items():
            if v == max(a_dictionary.values()):
                return k
    else:
        return None
