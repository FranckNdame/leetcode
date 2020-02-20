# def poker(hands):
#     scores = [(i, score(hand.split())) for i, hand in enumerate(hands)]

#     print(scores)
#     winner = sorted(scores, key=lambda x: x[1])[-1][0]
#     print(hands, winner)
#     return hands[winner]


# def score(hand):
#     ranks = '23456789TJQKA'
#     rcounts = {ranks.find(r): ''.join(hand).count(r) for r, _ in hand}.items()
#     score, ranks = zip(*sorted((cnt, rank) for rank, cnt in rcounts)[::-1])
#     if len(score) == 5:
#         if ranks[0:2] == (12, 3):  # adjust if 5 high straight
#             ranks = (3, 2, 1, 0, -1)
#         straight = ranks[0] - ranks[4] == 4
#         flush = len({suit for _, suit in hand}) == 1
#         '''no pair, straight, flush, or straight flush'''
#         score = ([(1,), (3, 1, 1, 1)], [(3, 1, 1, 2), (5,)])[flush][straight]
#     return score, ranks


# print(poker(['AH QS 6S 5D 4C', 'AS KS QS JS TS',
#              '8C AD 8D AC 9C', '7C 5H 8D TD KS']))
# # 8C AD 8D AC 9C


a = [4, 7, 9, 11, 20]
b = [1, 3, 4, 10, 15, 21]


def mergeLists(a, b) -> [int]:
    result = []
    pA, pB = 0, 0

    while pA < len(a) and pB < len(b):
        if a[pA] <= b[pB]:
            result.append(a[pA])
            pA += 1
        else:
            result.append(b[pB])
            pB += 1
    if pA < len(a):
        result.extend(a[pA:])
    if pB < len(b):
        result.extend(b[pB:])

    return result


print(mergeLists(a, b))
