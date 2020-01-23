class Solution:

    # String Manipulation Approach
    def validUtf8(self, data: List[int]) -> bool:
        bytes_count = 0

        for num in data:
            byte = format(num, "#010b")[-8:]

            if not bytes_count:
                for bit in byte:
                    if bit == "0":
                        break
                    bytes_count += 1

                if bytes_count == 0:
                    continue

                if bytes_count == 1 or bytes_count > 4:
                    return False

            else:
                if f"{byte[0]}{byte[1]}" != "10":
                    return False

            bytes_count -= 1

        return bytes_count == 0
