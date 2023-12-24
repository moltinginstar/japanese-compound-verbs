from genanki import Model

from .cards import JAPANESE_TO_ENGLISH_TEMPLATE


FIELDS = [
  {"name": "Verb"},
  {"name": "Verb (Hiragana)"},
  {"name": "Verb (Romaji)"},
  {"name": "V1"},
  {"name": "V1 (Hiragana)"},
  {"name": "V1 (Romaji)"},
  {"name": "V2"},
  {"name": "V2 (Hiragana)"},
  {"name": "V2 (Romaji)"},
  {"name": "Transitivity"},
  {"name": "Pattern"},
  {"name": "Meaning"},
  {"name": "Meaning (English)"},
  {"name": "Meaning (Korean)"},
  {"name": "NLB Link"},
]

CSS = """\
.card {
  font-family: Roboto, arial;
  font-size: 20px;
  color: black;
  background-color: white;
  text-align: center;
}

.verb {
}

.stems {
}

.meaning {
  text-align: start;
}
"""

MODEL_ID = 1654622297668
MODEL_NAME = "Japanese Compound Verb"

MODEL = Model(
  MODEL_ID,
  MODEL_NAME,
  fields=FIELDS,
  templates=[
    JAPANESE_TO_ENGLISH_TEMPLATE,
  ],
  css=CSS,
)
