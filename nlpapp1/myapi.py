import nlpcloud

class API:

    def __init__(self):
        self.client = nlpcloud.Client("gpt-oss-120b", "0e8537908e5be6b8613e386ef6bbff2b31886338", gpu=True) #set your own key

    def sentiment_analysis(self,text):
        return self.client.sentiment(text)
    
    def ner_analysis(self,text,searched_entity):
        return self.client.entities(text,searched_entity)
    
    def language_detection(self,text):
        return self.client.langdetection(text)