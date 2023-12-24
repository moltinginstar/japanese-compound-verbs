# The Japanese Compound Verbs deck

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

This repo contains the data and code to build the [Japanese Compound Verbs](https://ankiweb.net/shared/info/921752699) deck, a comprehensive list of over 2700 compound verbs in Japanese, complete with parallel definitions, usage notes, and example sentences in Japanese, English, and Korean.

## Contributing

If you find any mistakes that may have slipped through, or if you have any suggestinos for improvements (such as new note types), you’re more than welcome to create an issue or—better yet—a pull request. If you choose to contribute, these will come in handy:

- https://docs.ankiweb.net/getting-started.html
- https://github.com/kerrickstaley/genanki

## Repository structure

```
.
├── build/
│   └── [Japanese Compound Verbs.apkg] the final packaged deck
├── data/
│   └── data.csv                       the contents of the deck
└── japanese_compound_verbs/
    ├── datatypes/
    │   └── data_record.py             type hints for data.csv
    ├── notetypes/
    │   └── <notetype>/
    │       ├── cards/
    │       │   └── <template>.py      front and back templates for a card style
    │       ├── definition.py          notetype ID, name, and fields 
    │       └── utils.py               functions for creating a note, etc.
    └── main.py                        script for building the deck
```

## License

The contents of this repository (including the data) are licensed under the [GNU GPL v3](https://choosealicense.com/licenses/gpl-3.0/) license.

## Credit

National Institute for Japanese Language and Linguistics. (2015) *The Compound Verb Lexicon* [Original Data]. (https://vvlexicon.ninjal.ac.jp/)
