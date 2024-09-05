class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []

        keyboard = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
        }

        result = []
        n = len(digits)

        def backtrack(i,stack):

            if i == n :
                # if len(stack) == n:
                result.append(''.join(stack))
                return

            for ch in keyboard[digits[i]]:
                stack.append(ch)
                backtrack(i+1,stack)
                stack.pop()
                # backtrack(i+1,stack)
            
        backtrack(0,[])

        return result


                