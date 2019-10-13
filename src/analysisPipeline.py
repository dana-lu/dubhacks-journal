from src.speechToText import STT
from src.textAnalysis import TextAnalysis
from src.storage import Storage

class AnalysisPipeline:
    def __init__(self):
        self.stt = STT()
        self.db = Storage()
        self.sadThreshold = 0.33
        self.happyThreshold = 0.66

    def getAndAnalyzeSpeech(self):
        input_text = self.stt.speech_to_text()

        ta = TextAnalysis(input_text)
        result = ta.analysis()

        for key in result:
            sentiment = result[key][0]
            words = result[key][1]
            increment = 0
            if sentiment <= self.sadThreshold:
                increment = -1
            elif sentiment >= self.happyThreshold:
                increment = 1
            for word in words:
                self.db.set_word(word, self.db.get_word(word) + increment)        







