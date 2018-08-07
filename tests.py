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
arguments = list(test_doc._.arguments.get_argument_spans_and_matches())

assert len(arguments) == 3, "Extension yielded {} instead of {} Spans".format(len(arguments), 3)

should_argument, therefore_argument, because_argument = arguments

should_span, should_match = should_argument
assert isinstance(should_span, Span)
assert should_span.text == "should"
assert should_span.label_ == "necessity"
assert should_match is not None
assert should_match.group() == "should"

therefore_span, therefore_match = therefore_argument
assert isinstance(therefore_span, Span)
assert therefore_span.text == "therefore,"
assert therefore_span.label_ == "causation"
assert therefore_match is not None
assert therefore_match.group() == "therefore"

because_span, because_match = because_argument
assert isinstance(because_span, Span)
assert because_span.text == "because"
assert because_span.label_ == "causation"
assert because_match is not None
assert because_match.group() == "because"

# Init the parser again. Should not recreate extensions.
parser = ArguingLexiconParser(lang=nlp.lang)

# Get all possible words used in the lexicon
lexicon_vocabulary = parser.get_lexicon_vocabulary()
assert isinstance(lexicon_vocabulary, set)
assert len(lexicon_vocabulary) == 317

print("Tests passed!")
