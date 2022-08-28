name = "spacy_arguing_lexicon"

from spacy.language import Language

from .arguments import ArgumentTexts
from .parsers import ArguingLexiconParser


@Language.factory("arguments")
def _factory(nlp, name):
    return ArguingLexiconParser(lang=nlp.lang)
