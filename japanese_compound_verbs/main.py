import pandas as pd

from genanki import Deck
from pathlib import Path

from notetypes import make_japanese_compound_verb_note
from datatypes import Record


INPUT_PATH = Path("data/deck.csv")
OUTPUT_PATH = Path("build/Japanese Compound Verbs.apkg")

DECK_ID = 1654621019598
DECK_NAME = "Japanese Compound Verbs"

if __name__ == "__main__":
  data = pd.read_csv(
    INPUT_PATH,
    na_filter=False,
    converters={
      "structure": str.split,
    },
  )

  deck = Deck(DECK_ID, DECK_NAME)

  record: Record
  for record in data.itertuples(index=False, name="Record"):
    note = make_japanese_compound_verb_note(record)
    deck.add_note(note)

  OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

  deck.write_to_file(OUTPUT_PATH)
