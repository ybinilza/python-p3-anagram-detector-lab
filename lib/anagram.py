class Anagram:
    def __init__(self,word):
        self.word=word;
    
    def match(self,word_list):
        a=[];
        print(a)
        for item in word_list:
            if sorted(item) == sorted(self.word):
                a.append(item);
        return(a)

listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))