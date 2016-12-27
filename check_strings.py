from __future__ import division
from os.path import abspath, normpath, dirname, join, isfile
from babel.messages import pofile
import os

cwd = os.getcwd()
print (u'Running on : {}'.format(cwd))
locales = join(cwd, 'locales')

pot_path = join(locales, 'messages.pot')
es_path = join(locales, join('es_ES', join('LC_MESSAGES', 'messages.po')))

if not isfile(pot_path) or not isfile(es_path):
    exit(-1)

with open(pot_path, 'r') as pot:
    pot_file = pofile.read_po(pot)

with open(es_path, 'r') as po:
    es_file = pofile.read_po(po)

if not pot_file or not es_file:
    print (u'messages.pot or messages.po could not be readed')


strings = [s.id for s in pot_file]
strings = set(strings)
es_strings = []
t_strings = []
failed_strings = []
print (u'Checking for all strings to be translated...')
for s in es_file:
    es_strings.append(s.id)
    if not(s.id and s.string):
        failed_strings.append(s.id)
    else:
        t_strings.append(s.string)

print (u'Checking all strings in pot to be in po...')
es_strings = set(es_strings)
substr = strings - es_strings
if substr != set():
    print (u'There are {0} missing strings in the po file!\n{1}'.format(
        len(substr), list(substr)
    ))
    exit(-1)
    
print (u'\nTranslated strings: {0}/{1} ({2}%)\n'.format(
    len(t_strings), len(strings), len(t_strings)/len(strings) * 100
))
if failed_strings:
    print (u'There are strings not translated!\n{}'.format(failed_strings))
    exit(-1)

print (u'Success!')
