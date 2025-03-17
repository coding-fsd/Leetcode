class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False

        dict1 ={}
        dict2 ={}
        for i in range(len(word1)):
            if word1[i] not in dict1.keys():
                dict1[word1[i]] = 1
            else : 
                x = dict1.get(word1[i])
                x += 1
                dict1.update({word1[i] : x})

        for i in range(len(word2)):
            if word2[i] not in dict2.keys():
                dict2[word2[i]] = 1
            else : 
                x = dict2.get(word2[i])
                x += 1
                dict2.update({word2[i] : x})

        return sorted(dict1.values()) == sorted(dict2.values())

        #Hash map/ dict to put in words and their occurance check them against the target string
