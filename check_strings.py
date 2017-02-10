from __future__ import division, print_function, unicode_literals
from os.path import abspath, normpath, dirname, join, isfile
from babel.messages import pofile
import os
import argparse

parser = argparse.ArgumentParser(description='Check the strings translated.',
                                 usage='%(prog)s [options]')
parser.add_argument(
    '--list', '-l',
    nargs='?', const=True, default=False,
    help='Print a list of missing strings'
)
parser.add_argument(
    '--verbose', '-v',
    nargs='?', const=True, default=False,
    help='Show more status messages'
)
args = parser.parse_args()

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
endcl = "\033[0m"

cwd = os.getcwd()
if args.verbose:
    print ('Running on : {}'.format(cwd))
locales = join(cwd, 'locales')

pot_path = join(locales, 'messages.pot')
es_path = join(locales, join('es_ES', join('LC_MESSAGES', 'messages.po')))

if not isfile(pot_path) or not isfile(es_path):
    print (
        '{}Missing "locales/messages.pot" or '
        '"locales/es_ES/LC_MESSAGES/messages.po" files{}'.format(
            red, endcl
        )
    )
    exit(-1)

with open(pot_path, 'r') as pot:
    pot_file = pofile.read_po(pot)

with open(es_path, 'r') as po:
    es_file = pofile.read_po(po)

if not pot_file or not es_file:
    print ('{}messages.pot or messages.po could not be readed{}'.format(
        red, endcl
    ))

strings = [s.id for s in pot_file]
strings.remove("")
strings = set(strings)
es_strings = []
t_strings = []
failed_strings = []
fuzz_strings = []
if args.verbose:
    print ('Checking for all strings to be translated...', end="")
for s in es_file:
    es_strings.append(s.id)
    if s.id == "":
        es_strings.remove("")
    elif not(s.id and s.string) or s.fuzzy:
        failed_strings.append(s.id)
        if s.fuzzy:
            fuzz_strings.append(s.id)
    else:
        t_strings.append(s.string)

if not failed_strings and args.verbose:
    print('{}OK{}'.format(green, endcl))
elif args.verbose:
    if len(failed_strings) >= 1:
        print ('\n\t{}There are strings not translated!{}'.format(
            red, endcl
        ))
    if len(fuzz_strings) >= 1:
        print (
            '\t{}There are fuzzy strings!{}'.format(
                yellow, endcl
            )
        )

if args.verbose:
    print ('Checking all strings in pot to be in po...', end="")
es_strings = set(es_strings)
substr = strings - es_strings
if substr != set() and args.verbose:
    print ('\n\t{0}There are {1} missing strings in the po file!\n{2}'.format(
        red, len(substr), endcl
    ))
elif args.verbose:
    print ('{}OK{}'.format(green, endcl))

lenstr = len(strings) + len(substr)

print ("\nStrings' translated test briefing:\n")
print ('\t\t{}Translated strings:\t{}{}\t({}%)'.format(
    green, len(t_strings), endcl,
    len(t_strings)/lenstr * 100
))
print ('\t\t{}Fuzzy strings:\t\t{}{}\t({}%)'.format(
    yellow, len(fuzz_strings), endcl, 
    len(fuzz_strings)/lenstr * 100
))
print ('(No Fuzzy)\t{}Untranslated strings:\t{}{}\t({}%)'.format(
    red, len(failed_strings)-len(fuzz_strings), endcl,
    (len(failed_strings)-len(fuzz_strings))/lenstr * 100
))
print ('\t\t{}Missing strings:\t{}{}\t({}%)'.format(
    red, len(substr), endcl, len(substr)/lenstr * 100
))

print ('\t----------------------------------------------------')
print ('\t\tTotal Strings:\t\t{}\n'.format(
    lenstr
))
if substr != set():
    if args.list:
        print ('Missing strings:\n{}'.format(
            substr
        ))
    exit(-1)
if failed_strings:
    if args.list:
        print ('Missing strings:\n{}'.format(
            failed_strings
        ))
    exit(-1)
if len(t_strings) != lenstr:
    print('There are more strings in po than in pot after build!')
    print('Try running "./translate.sh" again...\n')
    exit(-1)
print ('{}Success!{}'.format(green, endcl))

