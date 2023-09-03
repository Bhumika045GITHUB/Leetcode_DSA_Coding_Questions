class Solution:
    def interpret(self, command: str) -> str:

        map={"G":"G","()":"o","(al)":"al"}
        temp =""
        res=""
        for i in range(len(command)):
            temp+=command[i]
            if(temp in map):
                res+=map[temp]
                temp=""
        return res
