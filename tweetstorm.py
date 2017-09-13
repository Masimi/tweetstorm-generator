import re
from nltk.tokenize import WhitespaceTokenizer


class TStorm(object):
    """This class create a tweetstorm from a file"""

    tweetList = list()
    file_name = None
    size = 140
    data = None

    def __init__(self, file_name):
        """Constructor"""
        self.file_name = file_name

    def TweetStorm(self):
        """This main method responsable convert from text to tweetstorm"""

        with open(self.file_name, "r", encoding="utf-8") as text:
            self.data = text.read().replace("\n", " ")

        self.splitTweet(self.data)
        return self.tweetList

    def splitTweet(self, text):
        """This method tokenize the text"""

        token = WhitespaceTokenizer().tokenize(text)
        word = ''
        rest = ''
        
        if len(text) <= self.size:
            self.tweetList.append(text)
            return
        
        for i in token:
            word = word + " " + i
            word = word.strip()
            if len(word) > self.size:
                word = word.replace(i, "")
                self.tweetList.append(" ".join(word.split(" ")[:-1]))
                word = i
            else:
                rest = word

        self.tweetList.append(rest)

        return self.tweetList