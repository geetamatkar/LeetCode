class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        print(words)
        print(type(words))
        #reversed=words.reverse()
        reversed=words[::-1]
        print(reversed)
        return ' '.join(reversed)
        