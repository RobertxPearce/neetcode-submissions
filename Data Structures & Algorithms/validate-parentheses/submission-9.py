class Solution:
    def isValid(self, s: str) -> bool:
        tmp_stack = []

        if len(s) <= 1:
            return False

        for curr in s:
            if curr == "(" or curr == "{" or curr == "[":
                tmp_stack.append(curr)
            elif curr == ")":
                if len(tmp_stack) == 0:
                    return False
                last_paren = tmp_stack.pop()
                if last_paren != "(":
                    return False
            elif curr == "}":
                if len(tmp_stack) == 0:
                    return False
                last_paren = tmp_stack.pop()
                if last_paren != "{":
                    return False
            elif curr == "]":
                if len(tmp_stack) == 0:
                    return False
                last_paren = tmp_stack.pop()
                if last_paren != "[":
                    return False

        if len(tmp_stack) > 0:
            return False

        return True