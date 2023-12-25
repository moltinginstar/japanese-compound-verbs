FRONT_TEMPLATE = """\
<p class="verb"><ruby>{{Verb}}<rt>{{Verb (Hiragana)}}</rt></ruby> ({{Verb (Romaji)}})</p>

<p class="stems">= <ruby>{{V1}}<rt>{{V1 (Hiragana)}}</rt></ruby> + <ruby>{{V2}}<rt>{{V2 (Hiragana)}}</rt></ruby></p>

<br />

<div class="meaning">{{Meaning}}</div>
"""

BACK_TEMPLATE = """\
{{FrontSide}}

<hr />

<div class="meaning">{{Meaning (English)}}</div>
"""

TEMPLATE = {
  "name": "Japanese → English",
  "qfmt": FRONT_TEMPLATE,
  "afmt": BACK_TEMPLATE,
}
