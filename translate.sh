#!/bin/bash
echo "Erasing old pot file (local cache)..."
`rm locales/messages.pot`
echo "Building docs to get new pot file..."
`mkdocs build -f mkdocs_es.yml --clean`
echo "Merging pofiles..."
`msgmerge -U locales/es_ES/LC_MESSAGES/messages.po locales/messages.pot`
echo "Opening updated pofile with poedit..."
`poedit locales/es_ES/LC_MESSAGES/messages.po`
python check_strings.py

