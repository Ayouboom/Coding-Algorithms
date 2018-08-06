class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        ords = {}
        offset = ord('a')
        for char in string.ascii_lowercase:
            ords[char] = ord(char) - offset
        belongTo = [None]*26
        partitionsStack = []
        
        countPartition = 1
        for idx_char in range(len(S)):
            char = S[idx_char]
            index = ords[char]
            if belongTo[index] == None:
                partitionsStack.append(idx_char)
                belongTo[index] = countPartition
                countPartition += 1
            else:
                length = len(partitionsStack)
                while length > belongTo[index]:
                    partitionsStack.pop()
                    length -= 1
                    countPartition -= 1
                for c in range(partitionsStack[-1]+1, idx_char+1):
                    belongTo[ords[S[c]]] = length
                partitionsStack[-1] = idx_char
                
        res = []
        for i in range(len(partitionsStack)):
            if i == 0:
                start = -1
            else:
                start = partitionsStack[i-1]
            res.append(partitionsStack[i]-start)
            
        return res
