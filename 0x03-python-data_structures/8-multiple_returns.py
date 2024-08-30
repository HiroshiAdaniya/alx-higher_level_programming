#!/usr/bin/python3
def multiple_returns(sentence):
    turple_1 = ()
    if sentence is "":
        turple_1 = (0, None)
    else:
        turple_1 = (len(sentence), sentence[0])
    return turple_1
