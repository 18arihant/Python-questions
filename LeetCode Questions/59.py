# 

class Solution():
    def checkIfPangram(self, sentence):
        if len(set(sentence))==26:
            return True
        else:
            return False
