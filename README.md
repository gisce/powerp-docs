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

For more detailed info, [check the wiki].

Set all file titles in the mkdocs.yml files.
For each language, there should be a translation.

To translate the text use:

```shell
./translate.sh
```

To merge with master, you'll probably have conflicts with the pofile. There's
quite a story behind, [you can learn more on the wiki].

Just use the following:

```shell
./merge.sh
```

**Remember to commit after changes are applied**

## Display documentation

You should [check the wiki] to learn more about this.

The essential commands are:

* Serve - to build a webserver that auto-updates with changes in the docs.
  (Does not update with the translations files)
* Build - to build the html from the docs into a folder.

With this a webserver is started locally reloading automatically when is needed.
With the "-f" argument, we specify the config file to be used.

i.e.:

```shell
$ mkdocs serve  
$ mkdocs serve -f mkdocs_es.yml
$ mkdocs build
$ mkdocs build -f mkdocs_es.yml
```

# Coding references

- [Markdown Reference](https://pythonhosted.org/Markdown/index.html)
- [MKDocs Reference](http://www.mkdocs.org/)

Markdown extensions:

* [Tables](https://pythonhosted.org/Markdown/extensions/tables.html) (and [grid_tables](https://github.com/smartboyathome/Markdown-GridTables))
* [Admonition](https://pythonhosted.org/Markdown/extensions/admonition.html)
* [markdown_i18n](https://github.com/gisce/markdown-i18n)

## Project structure

We have 5 categories:

- **base**: Base components: used in distri & comer
- **distri**: Distri components
- **comer**: Comer components
- **facturacio**: Base invoicing components used in distri & comer
- **gis**: GIS components

For images we use `_static` folder inside the category with a subfolder for the
same name as Markdown file of the Section.

i.e.:

For `distri/atr.md` we have `distri/_static/atr/image1.png`

# Testing

Our travis testing includes:

- mkdocs build -f mkdocs.yml
- mkdocs build -f mkdocs_es.yml
- Check for all strings translated in the .po
- Check for all the strings in the .pot (after build) to be in the .po
