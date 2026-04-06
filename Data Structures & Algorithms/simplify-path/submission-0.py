class Solution:
    def simplifyPath(self, path: str) -> str:
        pathsplit = path.split("/")
        stack = []
        for paths in pathsplit:
            if paths == "..":
                if stack:
                    stack.pop()
            elif paths != "" and paths != ".":
                stack.append(paths)
        return "/" + "/".join(stack)
            
        