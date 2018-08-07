from spacy.tokens import Span


class ArgumentTexts(object):

    def __init__(self, parser):
        self.parser = parser

    def __call__(self, doc):
        self.doc = doc
        return self

    def get_label_hash(self, label):
        # When dealing with languages other than English the label might not exist yet
        if label not in self.doc.vocab.strings:
            self.doc.vocab.strings.add(label)
        return self.doc.vocab.strings[label]

    def create_span_from_match(self, match, label):
        token_end = -1
        start_token_index = None
        end_token_index = None
        start_char_index = match.start()
        end_char_index = match.end() if self.doc.text[-1].isspace() else match.end() - 1
        for token in self.doc:
            token_end += len(token.text_with_ws)
            if start_token_index is None and start_char_index < token_end:
                start_token_index = token.i
            if end_token_index is None and end_char_index <= token_end:
                end_token_index = token.i + 1
                break
        else:
            raise Exception(
                "Could not create Span for match {}:{} indexed as {}:{} in following document:\n\n{}".format(
                    start_char_index, end_char_index,
                    start_token_index, end_token_index,
                    self.doc.text
                )
            )
        return Span(self.doc, start_token_index, end_token_index, self.get_label_hash(label))

    def get_argument_spans_and_matches(self):
        for argument_label, argument_match in self.parser.get_arguing_matches(self.doc):
            span = self.create_span_from_match(argument_match, argument_label)
            if not span:
                continue
            yield span, argument_match

    def get_argument_spans(self):
        return (span for span, match in self.get_argument_spans_and_matches())
