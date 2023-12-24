from typing import Literal, NamedTuple


class Record(NamedTuple):
  guid: str
  verb: str
  verb_hiragana: str
  verb_romaji: str
  verb_1: str
  verb_1_hiragana: str
  verb_1_romaji: str
  verb_2: str
  verb_2_hiragana: str
  verb_2_romaji: str
  transitivity: Literal["自", "自（意志）／他", "他", "自（意志）／自", "自／他", "自（意志）", "自／自（意志）", "他／自", "他／自（意志）"]
  pattern: str
  meaning: str
  meaning_en: str
  meaning_ko: str
  nlb_link: str
  structure: list[Literal["Vs", "VV", "pV", "V", "backformation"]]
