# PowERP documentation
We've got this :) or not? nooooo :'(
:S
TT
[Build of our documentation](http://builds.gisce.net/powerp-docs/powerp/)

## Setting up your environment

```shell
$ mkvirtualenv powerp-docs
$ git clone git@github.com:gisce/powerp-docs.git
$ cd powerp-docs
$ pip install -r requirements.txt
$ export PYTHONPATH=$PWD/sitecustomize
```

## Translations

Titles on .yml must be translated manually
There must be one .yml file for each lang

Translatable strings can be found on "/locales" inside _messages.pot_
Every mkdocs build updates the _message.pot_ file

Steps to translate your new documentation:

1.- Write your docs in the default lang (ca_ES)
2.- Local build your version (with _build_ or _serve_)
3.- Combine the new strings in the .pot with the old .po using:
    msgmerge -U locales/lang/LC_MESSAGES/messages.po locales/messages.pot
4.- Generate the new translations from the updated .po using *poedit*
    poedit locales/lang/LC_MESSAGES/messages.po

## Start documenting

```shell
$ mkdocs serve
$ mkdocs serve -f mkdocs_es.yml
```

With this a webserver is started reloading automatically when is needed.
With the second command, we specify the config file to be used.

- [Markdown Reference](https://pythonhosted.org/Markdown/index.html)
- [MKDocs Reference](http://www.mkdocs.org/)

Markdown extensions:

* Tables
* Admonition

## Project structure

We have 4 categories:

- **base**: Base components: used in distri & comer
- **distri**: Distri components
- **comer**: Comer components
- **facturacio**: Base invoicing components used in distri & comer

For images we use `_static` folder with a subfolder with the same name as Markdown file. eg:

for `distri/atr.md` we have `distri/_static/atr/image1.png`

# Testing

Our travis testing includes:

- mkdocs build -f mkdocs.yml
- mkdocs build -f mkdocs_es.yml
- Check for all strings translated in the .po
- Check for all the strings in the .pot (after build) to be in the .po

