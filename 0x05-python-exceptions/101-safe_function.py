#!/usr/bin/python3

def safe_function(fct, *args):
    func_ret = fct
    try:
        return func_ret
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
