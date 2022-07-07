class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        words = s.split()
        reversed_string = ""
        
        number_of_words = len(words)
        
        for i in range(0, number_of_words):

            each_word = words[i]

            temp = 0
            each_word = list(each_word)

            for j in range(0, len(each_word)//2):
                temp = each_word[j]
                each_word[j] = each_word[len(each_word)-1-j]
                each_word[len(each_word)-1-j] = temp

            str1 = ""
            str1 = str1.join(each_word)
            
            if i == number_of_words-1:
                reversed_string = reversed_string + str1
            else:
                reversed_string = reversed_string + str1 + " "
            
        return reversed_string
        
        
        