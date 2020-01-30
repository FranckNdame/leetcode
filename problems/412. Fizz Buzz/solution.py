class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        for i in range(1, n+1):
            if not i % 15:
                result.append("FizzBuzz")
            elif not i % 5:
                result.append("Buzz")
            elif not i % 3:
                result.append("Fizz")
            else:
                result.append(str(i))

        return result
