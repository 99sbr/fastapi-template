import re
import nltk
import pickle
from application.main.config import settings


class QuestionIdentification(object):

    def __init__(self):
        self.classifier = pickle.load(open(settings.APP_CONFIG.CLASSIFICATION_MODEL, 'rb'))

    def dialogue_act_features(self, question: str):
        features = {}
        for word in nltk.word_tokenize(question):
            features['contains({})'.format(word.lower())] = True
        return features

    def identify_questions_type(self, question: str) -> str:
        return self.classifier.classify(self.dialogue_act_features(question))


class QuestionClassificationService(object):

    def __init__(self) -> None:
        self.question_classification_model = settings.APP_CONFIG.CLASSIFICATION_MODEL

    @staticmethod
    def data_cleaning(input_text: str) -> str:
        # function to remove non-ascii characters
        def _removeNonAscii(s): return "".join(i for i in s if ord(i) < 128)
        clean_text = _removeNonAscii(input_text)
        # remove url
        clean_text = re.sub(r'http\S+', '', clean_text)
        # replace special chars
        clean_text = clean_text.replace("[^a-zA-Z0-9]", " ")
        return clean_text

    @staticmethod
    def classify(input_text: str) -> str:
        cleaned_text = QuestionClassificationService.data_cleaning(input_text)
        return QuestionIdentification().identify_questions_type(cleaned_text)
