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

red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
purple = "\033[0;35m"
endcl = "\033[0m"

cwd = os.getcwd()
if args.verbose:
    print ('Running on : {}'.format(cwd))
locales = join(cwd, 'locales')

pot_path = join(locales, 'messages.pot')
es_path = join(locales, 'es_ES', 'LC_MESSAGES', 'messages.po')

if not isfile(pot_path) or not isfile(es_path):
    print (
        '{}Missing "locales/messages.pot" or '
        '"locales/es_ES/LC_MESSAGES/messages.po" files{}'.format(
            red, endcl
        )
    )
    exit(-1)

# Read POT and PO Files

with open(pot_path, 'r') as pot:
    pot_file = pofile.read_po(pot)

with open(es_path, 'r') as po:
    es_file = pofile.read_po(po)

if not pot_file or not es_file:
    print ('{}messages.pot or messages.po could not be readed{}'.format(
        red, endcl
    ))

# Get Strings from pot file (generated strings)

generated_strings = [s.id for s in pot_file]
generated_strings.remove("")
generated_strings = set(generated_strings)

# Initialize strings lists

es_strings = []
t_strings = []
failed_strings = []
fuzz_strings = []
es_images_strings = []
if args.verbose:
    print ('Checking for all strings to be translated...', end="")

# Check strings in PO file

for s in es_file:
    es_strings.append(s.id)
    if s.id == "":
        es_strings.remove("")
    elif not s.string or s.fuzzy:
        failed_strings.append(s.id)
        if s.fuzzy:
            fuzz_strings.append(s.id)
    else:
        if s.id.startswith('<img src="data:image/png;base64,', 0):
            es_images_strings.append(s.id)
            es_strings.remove(s.id)
        else:
            t_strings.append(s.string)

# Output results

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

# Blockdiag images check

generated_images_strings = []

for s in generated_strings:
    if s.startswith('<img src="data:image/png;base64,', 0):
        generated_images_strings.append(s)

[generated_strings.remove(s) for s in generated_images_strings]

if args.verbose:
    print ('Checking number of images strings to match...', end="")
    if len(generated_images_strings) != len(es_images_strings):
        print ('{}FAIL{}'.format(red, endcl))
    else:
        print ('{}OK{}'.format(green, endcl))
    print('\tGenerated {} images in pot file'.format(
        len(generated_images_strings)
    ))
    print('\tFound {} images in po file'.format(
        len(es_images_strings)
    ))

# Get difference from generated (pot) and translated (po) strings

if args.verbose:
    print ('Checking all strings in pot to be in po...', end="")

es_strings = set(es_strings)
substr = generated_strings - es_strings
if substr != set() and args.verbose:
    print ('\n\t{0}There are {1} missing strings in the po file!\n{2}'.format(
        red, len(substr), endcl
    ))
            
elif args.verbose:
    print ('{}OK{}'.format(green, endcl))

# Get length of 'total' strings from generated (pot) strings

lenstr = len(generated_strings)

# Print test briefing

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
    purple, len(substr), endcl, len(substr)/lenstr * 100
))
print ('\t\t{}Images strings:\t\t{}/{}{}\t[found/generated]'.format(
    blue, len(es_images_strings), len(generated_images_strings), endcl
))

print ('\t----------------------------------------------------')
print ('\t\tTotal Strings:\t\t{}\n'.format(
    lenstr
))

# Print Test lists and exit if FAIL

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
if len(generated_images_strings) != len(es_images_strings):
    print ('Number of blockdiag images does not match!')
    exit(-1)
if len(t_strings) != lenstr:
    print('There are more strings in po than in pot after build!')
    print('Try running "./translate.sh" again...\n')
print ('{}Success!{}'.format(green, endcl))

