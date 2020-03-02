def rev(string):
    return rec(string[-1]+string[:-2])


def rec(string):
    if not string:
        return ""
    return rec(string[-1]+string[:-2])


print(rev("franck"))
