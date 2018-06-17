import spacy
from spacy.tokens import Span
from spacy_arguing_lexicon import ArguingLexiconParser


EN_EXAMPLE = """
A changing society should not cling to traditional family models. 
Society is changing, and the traditional idea of the nuclear family with married mother and father 
is no longer the only acceptable alternative. 
The reason that many countries are beginning to award legal rights to gay couples 
is because the stability of such relationships is now recognised. 
There is no reason, therefore, why such couples cannot provide a stable and loving upbringing for children.
"""

NL_EXAMPLE = """
Een maatschappij zou zich niet moeten vasthouden aan traditionele familie modellen.
De maatschappij veranderd, en het traditionele idea van een kern gezin met getrouwde vader en moeder 
is niet langer het enige acceptable alternatief.
De reden dat veel landen beginnen aan het toekennen van rechten aan homo koppels
is dat de stabiliteit van zulke relaties nu erkent wordt.
Daarom is er geen reden waarom zulke stellen geen stabiele en liefdevolle opvoeding aan kinderen kunnen geven. omdat"""


nlp = spacy.load('en')
nlp.add_pipe(ArguingLexiconParser(lang=nlp.lang))
test_doc = nlp(EN_EXAMPLE)
argument_spans = list(test_doc._.arguments.get_argument_spans())

assert len(argument_spans) == 3, "Extension yielded {} instead of {} Spans".format(len(argument_spans), 3)

should_span, therefore_span, because_span = argument_spans

assert isinstance(should_span, Span)
assert should_span.text == "should"
assert should_span.label_ == "necessity"

assert isinstance(therefore_span, Span)
assert therefore_span.text == "therefore,"
assert therefore_span.label_ == "causation"

assert isinstance(because_span, Span)
assert because_span.text == "because"
assert because_span.label_ == "causation"

print("Tests passed!")
