#!/bin/bash
echo "Copy local po file before merge"
cp locales/es_ES/LC_MESSAGES/messages.po messages.local.po
echo "Get remote po file from master before merge to avoid conflicts"
git checkout master -- locales/es_ES/LC_MESSAGES/messages.po
cp locales/es_ES/LC_MESSAGES/messages.po messages.remote.po
echo "Merging from master"
git merge origin/master
echo "Merging pofile using msgcat"
msgcat --use-first messages.local.po messages.remote.po -o locales/es_ES/LC_MESSAGES/messages.po
echo "Cleaning repository"
git add locales/es_ES/LC_MESSAGES/messages.po
rm messages.local.po
rm messages.remote.po
echo "DONE - use 'git commit' to end merging"

