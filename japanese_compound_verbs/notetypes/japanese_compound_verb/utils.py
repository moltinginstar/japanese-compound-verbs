from genanki import Note

from datatypes import Record
from .definition import MODEL


def extract_fields(record: Record):
  return [
    record.verb,
    record.verb_hiragana,
    record.verb_romaji,
    record.verb_1,
    record.verb_1_hiragana,
    record.verb_1_romaji,
    record.verb_2,
    record.verb_2_hiragana,
    record.verb_2_romaji,
    record.transitivity,
    record.pattern,
    record.meaning,
    record.meaning_en,
    record.meaning_ko,
    record.nlb_link,
  ]


def make_note(record: Record):
  return Note(
    model=MODEL,
    guid=record.guid,
    fields=extract_fields(record),
    tags=record.structure,
  )
