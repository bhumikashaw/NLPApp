import nlpcloud

class API:

    def __init__(self):
        self.client = nlpcloud.Client("gpt-oss-120b", "#Enter your own api key", gpu=True) #set your own key

    def sentiment_analysis(self,text):
        return self.client.sentiment(text)
    
    def ner_analysis(self,text,searched_entity):
        return self.client.entities(text,searched_entity)
    
    def language_detection(self,text):

        return self.client.langdetection(text)
