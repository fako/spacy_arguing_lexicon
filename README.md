# SpaCy Arguing Lexicon

A [spaCy](https://spacy.io/) extension that wraps around the [arguing lexicon by MPQA](http://mpqa.cs.pitt.edu/lexicons/arg_lexicon/). 
It allows easy programmatic access to labeled sentences containing arguing lexicon. Using spaCy you can then apply the latest machine learning technologies with little effort. 

Use the arguing lexicon extension for instance for deep argument mining. It is available in English and Dutch. 

## Getting started

You can install the spaCy extension through pip. It requires spaCy 2.

```bash
pip install spacy_arguing_lexicon
python -m spacy download en  # optional, downloads a spaCy language model if you haven't downloaded one already
```

Then enable the extension by adding the arguing lexicon parser to the spaCy pipeline.

```python
import spacy
from spacy_arguing_lexicon import ArguingLexiconParser

nlp = spacy.load("en")
nlp.add_pipe(ArguingLexiconParser(lang=nlp.lang))
```

Now you can load any document and access the parts of that document which contain arguments. 
You access the arguments through the ```doc._.arguments``` attribute, which gets added by this extension.

```python
doc = nlp("""
    A changing society should not cling to traditional family models. 
    Society is changing, and the traditional idea of the nuclear family 
    with married mother and father 
    is no longer the only acceptable alternative.
""")

argument_span = next(doc._.arguments.get_argument_spans())
print("Argument lexicon:", argument_span.text)
print("Label of lexicon:", argument_span.label_)
print("Sentence where lexicon occurs:", argument_span.sent.text.strip())
```

The above will output

```
Argument lexicon: should
Label of lexicon: necessity
Sentence where lexicon occurs: A changing society should not cling to traditional family models.
```

As ```get_argument_spans``` yields [spaCy Spans](https://spacy.io/api/span) 
it is trivial to retrieve things like average word embeddings for sentences that contain arguing lexicon.
These average embeddings can serve as input for your deep learning models.


You can for example access the built-in spaCy vectors for a sentence containing argument lexicon with

```python
print("Vector type:", type(argument_span.sent.vector))
print("Vector shape:", argument_span.sent.vector.shape)
``` 

Which will output

```
Vector type: <class 'numpy.ndarray'>
Vector shape: (384,)
```


## How it works

The MPQA arguing lexicon is made available under the GNU General Public License.
It is a set of about 200 regular expressions with macros divided into 17 categories.
For more information about how the lexicon was created we refer to the [arguing lexicon homepage](http://mpqa.cs.pitt.edu/lexicons/arg_lexicon/).

The Dutch arguing lexicon is a translation of the English lexicon and is available only through this extension.

Under the hood this extension parses the regular expressions and unpacks any macros inside of them. 
The ```doc._.arguments.get_argument_spans``` method tries to match any lexicon regular expression against the text of the input [spaCy Doc](https://spacy.io/api/doc).
When a match is found the match gets transformed into a [spaCy Span](https://spacy.io/api/span) before it gets yielded.

```doc._.arguments.get_argument_spans``` is the only recommended way of using this extension at the moment.

As the MPQA arguing lexicon is made available as a list of regular expressions we side stepped the [spaCy Matcher](https://spacy.io/api/matcher), 
but we think that loading the lexicon as a set of matchers might improve the performance.


## Citation

Please cite the following when using this software:

```
Swapna Somasundaran, Josef Ruppenhofer and Janyce Wiebe (2007) Detecting Arguing and Sentiment in Meetings, 
SIGdial Workshop on Discourse and Dialogue, Antwerp, Belgium, September 2007 (SIGdial Workshop 2007)
```
