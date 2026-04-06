class Solution:
    def decodeString(self, s: str) -> str:
        st_stack = []
        cnt_stack = []
        k = 0
        curr = ""

        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[" :
                st_stack.append(curr)
                cnt_stack.append(k)
                k = 0
                curr = ""
            elif c == "]":
                tmp = curr
                curr = st_stack.pop()
                count = cnt_stack.pop()
                curr += tmp * count
            else:
                curr += c
        
        return curr