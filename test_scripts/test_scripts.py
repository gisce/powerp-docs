from shutil import copyfile
from subprocess import Popen, PIPE
from os import system

msgdir = "locales/es_ES/LC_MESSAGES/"
pofile = "{}messages.po".format(msgdir)
potfile = "locales/messages.pot"

translate_cases = {}

merge_cases = {
    '0': {
        'descr': "No changes",
        'local': "{}test0.po".format(msgdir),
        'remote': "{}test0.po".format(msgdir)
    },
    # '1': {
    #     'descr': "String added on local po",
    #     'local': "{}test0.po",
    #     'remote': "{}test0.po"
    # },
    # '2': {
    #     'descr': "String added on remote po",
    #     'local': "{}test0.po",
    #     'remote': "{}test0.po"
    # }
}

print ("Testing Merge")
merge_ok = 0
for key in merge_cases.keys():
    remotepo = "messages.remote.po"
    case = merge_cases.get(key)
    print ("Case {}: {}".format(key, case['descr']))
    print ("\t Using local file: {}".format(case['local']))
    copyfile(case['local'], pofile)
    print ("\t Using remote file: {}".format(case['remote']))
    copyfile(case['remote'], remotepo)
    try:
        # Run merge script
        merge_test = Popen(
            "../merge.sh -t".split(),
            stderr=PIPE,
            stdout=PIPE
        )
        out, err = merge_test.communicate()
        print ("Resolved as:")
        print ("\tReturn Code: {}".format(merge_test.returncode))
        print ("\tOutput:\n{}".format(out))
    except Exception as ex:
        print ("Got an exception running merge!\n{}".format(ex))
    try:
        # Run Check Strings test on test-strings
        string_res = system("python ../check_strings.py -v")
        print ("Returned: {}".format(string_res))
        if string_res == 0:
            merge_ok += 1
    except Exception as ex:
        print ("Got an exception running check_strings!\n{}".format(ex))

print ("Merging tests: {}/{}".format(merge_ok, len(merge_cases)))
