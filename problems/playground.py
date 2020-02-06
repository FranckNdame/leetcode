def isSimilar(wordOne, wordTwo):
    wordOne, wordTwo = list(wordOne), list(wordTwo)
    for i in range(len(wordTwo)):
        for j in range(i, len(wordTwo)):
            wordTwo[i], wordTwo[j] = wordTwo[j], wordTwo[i]
            if wordOne == wordTwo:
                return True
            wordTwo[i], wordTwo[j] = wordTwo[j], wordTwo[i]
    return False


print(isSimilar("arts", "tars"))
