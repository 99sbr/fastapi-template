import spacy
from typing import List
from nltk.corpus import stopwords

from application.initializer import LoggerInstance
from application.main.config import settings

logger = LoggerInstance().get_logger(__name__)
stop_words = stopwords.words('english')

try:
    nlp = spacy.load(settings.SPACY_MODEL_IN_USE, disable=['parser', 'ner'])
except Exception as e:
    logger.info("Falling back to spacy 'en' model.")
    nlp = spacy.load("en", disable=['parser', 'ner'])
    logger.error(str(e), exc_info=True)


class TextPreprocessing(object):

    @staticmethod
    def spacy_text_cleanup(text: str) -> List[str]:
        removal = ['ADV', 'PRON', 'CCONJ',
                   'PUNCT', 'PART', 'DET', 'ADP', 'SPACE']
        text_out = []
        doc = nlp(text)
        for token in doc:
            if (token.is_stop is False) and token.is_alpha and len(token) > 2 and token.pos_ not in removal:
                lemma = token.lemma_
                text_out.append(lemma)
        return text_out

    @staticmethod
    def fix_contractions(text: str) -> str:
        """
        Fix contraction words like don't => do not and more
        """
        import contractions
        fixed_input_text = [contractions.fix(
                str(word)) for word in text.split()]
        fixed_input_text = " ".join(fixed_input_text)
        return fixed_input_text

    @staticmethod
    def fix_merged_words(text: str) -> str:
        """
        Fixes words like #baclklivesmatter => black lives matter.
        might be helpful when dealing with tweet data.
        """
        import wordninja
        wordninja_fixed_text = wordninja.split(text)
        wordninja_fixed_text = " ".join(wordninja_fixed_text)
        return wordninja_fixed_text
