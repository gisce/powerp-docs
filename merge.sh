#!/bin/bash
if [ $# -gt 0 ]
then
  if [ $1 == "-t" ]
  then
    testing=1
  fi
else
  testing=0
fi
if [ $testing -eq 1 ]
then
  base="test_scripts/locales"
else
  base="locales"
fi
echo "Copy local po file before merge"
cp $base/es_ES/LC_MESSAGES/messages.po messages.local.po
echo "Get remote po file from master before merge to avoid conflicts"
if [ $testing -eq 0 ]
then
  git checkout origin/master -- locales/es_ES/LC_MESSAGES/messages.po
else
  cp $base/messages.remote.po $base/es_ES/LC_MESSAGES/messages.po
fi
cp $base/es_ES/LC_MESSAGES/messages.po messages.remote.po
if [ $testing -eq 0 ]
then
  echo "Reset po file from local branch"
  git reset HEAD locales/es_ES/LC_MESSAGES/messages.po
  git checkout -- locales/es_ES/LC_MESSAGES/messages.po
  echo "Merging from master"
  git merge origin/master
fi
echo "Merging pofile using msgcat"
msgcat --use-first messages.local.po messages.remote.po -o messages.merge.po
mv messages.merge.po $base/es_ES/LC_MESSAGES/messages.po
echo "Cleaning repository"
rm messages.local.po
rm messages.remote.po
if [ $testing -eq 0 ]
then
  echo "Updating pot file to check strings after merge..."
  if [ -f locales/messages.pot ];
  then
    echo "Erasing old pot file (local cache)..."
    rm locales/messages.pot
  fi
  echo "Building docs to get new pot file..."
  mkdocs build -f mkdocs_es.yml --clean
  echo "Merging pofiles..."
  msgmerge -U locales/es_ES/LC_MESSAGES/messages.po locales/messages.pot
  git add locales/es_ES/LC_MESSAGES/messages.po
  if python check_strings.py;
  then
    echo "DONE - remember to 'git commit' to end merging"
  else
    echo "Test failed, update the strings with poedit"
    echo "DONE - use 'git commit' to end merging."
  fi
fi
echo "DONE"
