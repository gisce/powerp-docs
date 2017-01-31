# PowERP documentation

[Build of our documentation](http://builds.gisce.net/powerp-docs/master/)

**Table Of Contents**

- [Environment](#setting-up-your-environment)
    - [Recommended editors](#recommended-editors)
- [Translations](#translations)
- [Display Documentation](#display-documentation)
- [Project Structure](#project-structure)
- [Testing](#testing)

## Setting up your environment

```shell
$ mkvirtualenv powerp-docs
$ git clone git@github.com:gisce/powerp-docs.git
$ cd powerp-docs
$ pip install -r requirements.txt
$ export PYTHONPATH=$PWD/sitecustomize
```

### Recommended Editors

#### Edit documentation files: 

**Atom**    
_With the extensions:_

- [markdown-toc](https://atom.io/packages/markdown-toc)
    - Automatically creates TableOfContents. 
    - Can be easily configured.
    - Can't parse special characters.
- [markdown-writer](https://atom.io/packages/markdown-writer)
    - Hotkeys to markdown formats
    - Can be extended
    - Does not have config set, but you can set the default config...
- [markdown-preview](https://atom.io/packages/markdown-preview)
    - Prints the file built to html on a paralel workspace
 
#### Translate docs:

**Poedit**
_([Check the following translations section](#translations))_

_Merge Translations files_

- For _.po file_, use 'msgcat' command with '--use-first' parameter. I.e.:

```shell
git merge <branch_name_remote>
cd locales/<lang>/LC_MESSAGES
cp messages.po messages.po.loc
git checkout <branch_name_remote>
cp messages.po messages.po.rem
git checkout <branch_name_local>
msgcat --use-first messages.po.loc messages.po.rem -o messages.po
```

- Open .po file with poedit to update _.mo file_ and _modified date_
- Messages.pot will be automatically updated with build, so there is no need to merge
- Remember to commit after changes are applied

## Translations

Add your titles in all '*.yml'. They must be translated manually

There must be one '.yml' file for each language (mkdocs.yml, mkdocs_es.yml...)

Translatable strings can be found on "/locales" inside _messages.pot_

*Every mkdocs build using a '.yml' file updates the _message.pot_ file*
_except the default one_

*Easy Mode*: run ./translate.sh

Steps to translate your new documentation:

1. Write your docs in the default lang (ca_ES)
2. Local build your version with:

```shell
    mkdocs build -f mkdocs_es.yml
# OR
    mkdocs serve -f mkdocs_es.yml
```

3. Combine the new strings in the .pot with the old .po using:`
    
```shell
    sudo apt install gettext
    msgmerge -U locales/lang/LC_MESSAGES/messages.po locales/messages.pot
```
    
4. Generate the new translations from the updated .po using *poedit*

```shell
    sudo apt install poedit
    poedit locales/lang/LC_MESSAGES/messages.po
```
    
**Always commit the translated and updated .po and the compiled .mo**

## Display documentation

```shell
$ mkdocs serve
$ mkdocs serve -f mkdocs_es.yml
```

With this a webserver is started locally reloading automatically when is needed.
With the second command, we specify the config file to be used.

- [Markdown Reference](https://pythonhosted.org/Markdown/index.html)
- [MKDocs Reference](http://www.mkdocs.org/)

Markdown extensions:

* [Tables](https://pythonhosted.org/Markdown/extensions/tables.html) (and [grid_tables](https://github.com/smartboyathome/Markdown-GridTables))
* [Admonition](https://pythonhosted.org/Markdown/extensions/admonition.html)
* [markdown_i18n](https://github.com/gisce/markdown-i18n)

## Project structure

We have 4 categories:

- **base**: Base components: used in distri & comer
- **distri**: Distri components
- **comer**: Comer components
- **facturacio**: Base invoicing components used in distri & comer

For images we use `_static` folder with a subfolder with the same name as Markdown file. eg:

For `distri/atr.md` we have `distri/_static/atr/image1.png`

# Testing

Our travis testing includes:

- mkdocs build -f mkdocs.yml
- mkdocs build -f mkdocs_es.yml
- Check for all strings translated in the .po
- Check for all the strings in the .pot (after build) to be in the .po

