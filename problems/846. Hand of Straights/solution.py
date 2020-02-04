class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W:
            return False
        cards = collections.Counter(hand)
        while cards:
            card = min(cards)
            for i in range(W):
                curr = card + i
                if curr not in cards:
                    return False
                if cards[curr] > 1:
                    cards[curr] -= 1
                else:
                    del cards[curr]
        return True
