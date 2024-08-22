#!/usr/bin/env python38
if __name__ == "__main__":
    import hidden_4
    i = len(dir(hidden_4))
    for j in range(i):
        if dir(hidden_4)[j][0] == '_' and dir(hidden_4)[j][1] == '_':
            continue
        else:
            print("{}".format(dir(hidden_4)[j]))
