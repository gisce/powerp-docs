from __future__ import division, print_function, unicode_literals
from os.path import abspath, normpath, dirname, join, isfile
import yaml
import os
import argparse


red = "\033[0;31m"
green = "\033[0;32m"
endcl = "\033[0m"
cross = u"\U00002717"
check = u"\U00002713"


def get_pages(root):
    all_pages = []
    for section in root:
        for name, pages in section.items():
            if isinstance(pages, list):
                all_pages.append('')
                for page in get_pages(pages):
                    all_pages.append(page)
            else:
                all_pages.append(pages)

    return all_pages


with open('mkdocs.yml', 'r') as mkdocs_conf:
    ca_conf = yaml.load_all(mkdocs_conf)
    ca_pages = []
    for conf in ca_conf:
        ca_pages = get_pages(conf['pages'])

with open('mkdocs_es.yml', 'r') as mkdocs_conf:
    es_conf = yaml.load_all(mkdocs_conf)
    es_pages = []
    for conf in es_conf:
        es_pages = get_pages(conf['pages'])

missing_pages = set(es_pages) - set(ca_pages)
if missing_pages:
    print('{red}{cross} There are pages missing in the original config file!'
          '{endcl}'.format(**locals()))
    print(list(missing_pages))
    exit(-1)
missing_pages = set(ca_pages) - set(es_pages)
if missing_pages:
    print('{red}{cross} There are pages missing in the es_ES config file!'
          '{endcl}'.format(**locals()))
    print(list(missing_pages))
    exit(-1)
print('{green}{check} Both config files have the same pages'
      ' references{endcl}'.format(**locals()))


