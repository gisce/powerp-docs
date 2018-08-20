from __future__ import division, print_function, unicode_literals
from os.path import abspath, normpath, dirname, join, isfile
import yaml
import os


red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
endcl = "\033[0m"
cross = u"\U00002717"
check = u"\U00002713"

alt_configs = [
    'es'
]

NOT_CHECK = [
    'nav', 'language', 'markdown_i18n', 'google_analytics'
]

anyerr = 0
err = 0

with open('mkdocs.yml', 'r') as mkdocs_conf:
    default_conf = [data for data in yaml.load_all(mkdocs_conf)][0]
    for key in NOT_CHECK:
        if default_conf.get(key):
            default_conf.pop(key)


def check_conf(key, src, dest):
    if key in NOT_CHECK:
        return {str(src[key]): 0}
    if key not in src:
        return {str(src[key]): -1}
    if key not in dest:
        return {str(src[key]): -2}
    if isinstance(src[key], dict):
        errs = 0
        for k in src[key].keys():
            errs = check_conf(k, src[key], dest[key])
            if errs < 0:
                return errs
    elif isinstance(src[key], str):
        if src[key] != dest[key]:
            return {str(src[key]): -2}
    elif isinstance(src[key], (tuple, list)):
        errs = 0
        for elem in src[key]:
            if len(dest[key])-1 < src[key].index(elem):
                return {str(src[key]): -2}
            elem2 = dest[key][src[key].index(elem)]
            if isinstance(elem, dict):
                for k in elem.keys():
                    errs = check_conf(k, elem, elem2)
                    if errs < 0:
                        return errs
            elif isinstance(elem, str):
                if elem != elem2:
                    return {str(src[key]): -2}
    return {str(src[key]): 0}


for suffix in alt_configs:
    with open('mkdocs_{}.yml'.format(suffix)) as mkdocs_conf:
        alt_conf = [data for data in yaml.load_all(mkdocs_conf)][0]
    for conf, value in default_conf.items():
        if conf not in alt_conf.keys():
            print('{red}{cross} [mkdocs_{suffix}.yml] Conf missing:'
                  ' {conf}{endcl}'.format(**locals()))
            err += 1
        if conf in NOT_CHECK:
            continue
        errs = {
            k: v for k, v in check_conf(conf, default_conf, alt_conf).items()
            if v < 0
        }
        if errs:
            print('{red}{cross} [mkdocs_{suffix}.yml] Conf missmatch:'
                  ' {conf}{endcl}'.format(**locals()))
            for k in errs.keys():
                print('{red}\t- {{{k}}}{endcl}'.format(**locals()))
            err += 1
    if not err:
        print('{green}{check} "mkdocs_{suffix}.yml" passed!{endcl}'
              ''.format(**locals()))
    anyerr += err
    err = 0

if NOT_CHECK:
    print('{yellow}(IGNORED):\t{NOT_CHECK}{endcl}'.format(**locals()))
exit(anyerr)
