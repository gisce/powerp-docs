#!/bin/bash
echo "Copy local po file before merge"
cp locales/es_ES/LC_MESSAGES/messages.po messages.local.po
echo "Get remote po file from master before merge to avoid conflicts"
git checkout origin/master -- locales/es_ES/LC_MESSAGES/messages.po
cp locales/es_ES/LC_MESSAGES/messages.po messages.remote.po
echo "Reset po file from local branch"
git reset HEAD locales/es_ES/LC_MESSAGES/messages.po
git checkout -- locales/es_ES/LC_MESSAGES/messages.po
echo "Merging from master"
git fetch
git merge origin/master
echo "Are there any conflicts (not the po file)? [y/N]"
read input
if [[ $input == 'y' || $input == 'Y' ]]; then 
  abort=1
  echo "Solve the conflicts from another terminal"
  echo "Can we continue? Or should we (A)bort?"
  read input
  if [[ $input == 'A' ]]; then
    git merge --abort
    exit 
  fi
fi
echo "Merging pofile using msgcat"
msgcat --use-first messages.local.po messages.remote.po -o messages.merge.po
mv messages.merge.po locales/es_ES/LC_MESSAGES/messages.po
echo "Cleaning repository"
rm messages.local.po
rm messages.remote.po
echo "Updating python versions"
pip install -r requirements.txt
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
