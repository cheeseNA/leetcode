class Solution:
    def getCharFromUnitPos(self, s: str, numRows: int, unitIndex: int, position: int) -> str | None:
        assert numRows >= 2
        numChars = 2 * numRows - 2
        assert position < numChars
        if len(s) <= numChars * unitIndex + position:
            return None
        return s[numChars * unitIndex + position]

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        numChars = 2 * numRows - 2
        numUnits = (len(s) + numChars - 1) // numChars
        answer = ""
        for i in range(numUnits):
            char = self.getCharFromUnitPos(s, numRows, i, 0) 
            if char is not None:
                answer += char
        for row in range(1, numRows - 1):
            for i in range(numUnits):
                char = self.getCharFromUnitPos(s, numRows, i, row)
                if char is not None:
                    answer += char
                char = self.getCharFromUnitPos(s, numRows, i, numChars - row)
                if char is not None:
                    answer += char
        for i in range(numUnits):
            char = self.getCharFromUnitPos(s, numRows, i, numRows - 1)
            if char is not None:
                answer += char
        return answer
                
                