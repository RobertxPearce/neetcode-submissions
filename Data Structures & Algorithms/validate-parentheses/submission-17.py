class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        track = []
        valid_parens = {")": "(", "}": "{", "]": "["}
        for paren in s:
            if paren == "(" or paren == "{" or paren == "[":
                track.append(paren)
            elif paren == ")" or paren == "}" or paren == "]":
                try:
                    top_paren = track.pop()
                    if top_paren != valid_parens[paren]:
                        return False
                except:
                    return False
        if len(track) != 0:
            return False
        return True