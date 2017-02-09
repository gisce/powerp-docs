from __future__ import division, print_function
from os.path import abspath, normpath, dirname, join, isfile
from babel.messages import pofile
from sys import argv
import os

def usage():
    print ('Usage:')
    print ('\tpython check_strings [options]\n')
    print ('\t"-h" or "--help" to print usage and close')
    print ('\t"-v" or "--verbose" to print more output')
    print ('\t"-l" or "--list" to print the missing/failed strings list')

if len(argv) > 4:
    print ('Too many arguments!!')
    print ('use "check_strings.py --help" for usage description')
    exit(-1)
else:
    verb = False
    build = False
    use_list = False
    for i in range(1,len(argv)):
        if argv[i] == '-h' or argv[i] == '--help':
            usage()
            exit(-1)
        if (argv[i] == '-v') or (argv[i] == '--verbose'):
            verb = True
        elif (argv[i] == '-l') or (argv[i] == '--list'):
            use_list = True
        else:
            print ('Ignoring unknown argument "{}"...')
            print ('Use "-h" or "--help" to print usage')


green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
endcl = "\033[0m"

cwd = os.getcwd()
locales = join(cwd, 'locales')
if verb:
    print (u'Running on : {}'.format(cwd))

pot_path = join(locales, 'messages.pot')
es_path = join(locales, 'es_ES', 'LC_MESSAGES', 'messages.po')

if not isfile(pot_path) or not isfile(es_path):
    print (
        u'{}Missing "locales/messages.pot" or '
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
    print (u'{}messages.pot or messages.po could not be readed{}'.format(
        red, endcl
    ))
    exit(-1)

strings = [s.id for s in pot_file]
strings.remove("")
strings = set(strings)
es_strings = []
t_strings = []
failed_strings = []
fuzz_strings = []
if verb:
    print (u'Checking for all strings to be translated...', end="")
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

if not failed_strings and verb:
    print (u'{}OK{}'.format(green, endcl))
elif verb:
    if len(failed_strings) >= 1:
        print (u'\n\t{}There are strings not translated!{}'.format(
            red, endcl
        ))
    if len(fuzz_strings) >= 1:
        print (
            u'\t{}There are fuzzy strings!{}'.format(
                yellow, endcl
            )
        )
if verb:
    print (u'Checking all strings in pot to be in po...', end="")
es_strings = set(es_strings)
substr = strings - es_strings
if substr != set() and verb:
    print (u'\n\t{0}There are {1} missing strings in the po file!\n{2}'.format(
        red, len(substr), endcl
    ))
elif verb:
    print ('{}OK{}'.format(green, endcl))

lenstr = len(strings) + len(substr)
if verb:
    print ("\nStrings' translated test briefing:\n")
print (u'\t\t{}Translated strings:\t{}{}\t({}%)'.format(
    green, len(t_strings), endcl,
    len(t_strings)/lenstr * 100
))
print (u'\t\t{}Fuzzy strings:\t\t{}{}\t({}%)'.format(
    yellow, len(fuzz_strings), endcl, 
    len(fuzz_strings)/lenstr * 100
))
print (u'(No Fuzzy)\t{}Untranslated strings:\t{}{}\t({}%)'.format(
    red, len(failed_strings)-len(fuzz_strings), endcl,
    (len(failed_strings)-len(fuzz_strings))/lenstr * 100
))
print (u'\t\t{}Missing strings:\t{}{}\t({}%)'.format(
    red, len(substr), endcl, len(substr)/lenstr * 100
))

print (u'\t----------------------------------------------------')
print (u'\t\tTotal Strings:\t\t{}\n'.format(
    lenstr
))
if substr != set():
    if use_list:
        print (u'Missing strings:\n{}'.format(
            substr
        ))
    exit(-1)
if failed_strings:
    if use_list:
        print (u'Missing strings:\n{}'.format(
            failed_strings
        ))
    exit(-1)
if len(t_strings) != lenstr:
    print (u'There are more strings in po than in pot after build!')
    print (u'Try running "./translate.sh" again...\n')
    exit(-1)
print (u'{}Success!{}'.format(green, endcl))

