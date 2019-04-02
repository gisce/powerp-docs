#!/bin/bash

function build_failure {
   echo "Failed to build, check mkdocs build!"
   exit -1
}

pip install -r requirements.txt
if [ -f locales/messages.pot ]; then
    echo "Erasing old pot file (local cache)..."
    rm locales/messages.pot
fi
echo "Building docs to get new pot file..."
mkdocs build -f mkdocs_es.yml --clean || build_failure
echo "Merging pofiles..."
msgmerge -U locales/es_ES/LC_MESSAGES/messages.po locales/messages.pot
echo "Opening updated pofile with poedit..."
poedit locales/es_ES/LC_MESSAGES/messages.po
python tests/check_strings.py
