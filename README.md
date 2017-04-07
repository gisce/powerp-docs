# PowERP documentation

Our docs are available in: [manuals.gisce.net](http://manuals.gisce.net/)

**Table Of Contents**

- [Environment](#setting-up-your-environment)
    - [Recommended editors](#recommended-editors)
- [Translations](#translate-docs)
- [Display Documentation](#display-documentation)
- [Project Structure](#project-structure)
- [Coding references](#coding-references)
- [Testing](#testing)

## Setting up your environment

```shell
$ mkvirtualenv powerp-docs
$ git clone git@github.com:gisce/powerp-docs.git
$ cd powerp-docs
$ pip install -r requirements.txt
$ apt-get install gettext
$ apt-get install poedit
```

### Recommended Editors

#### Edit documentation files:

**Atom**    
_With the extensions:_

- [markdown-toc](https://atom.io/packages/markdown-toc)
    - Automatically creates TableOfContents.
    - Can be easily configured.
    - Can't parse special characters.
    - Use only if ToC is needed in the docs you are writing.
- [markdown-writer](https://atom.io/packages/markdown-writer)
    - Hotkeys to markdown formats
    - Can be extended
    - Does not have config set, but you can set the default config...
- [markdown-preview](https://atom.io/packages/markdown-preview)
    - Prints the file built to html on a paralel workspace

#### Translate docs:

For more detailed info, [check the wiki](https://github.com/gisce/powerp-docs/wiki/Translate!----build-your-docs-on-any-language).

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

You should [check the wiki](https://github.com/gisce/powerp-docs/wiki/Build!---Displaying-the-Docs) to learn more about this.

The essential commands are:

* Serve - to build a webserver that auto-updates with changes in the docs.
    - Does not update with the translations files
    - **RECOMMENDED** While writting the docs
* Build - to build the html from the docs into a folder.

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

_**NOTE**_: All filenames and directories should be in Spanish

We have 5 categories:

- **base**: Base components: used in distri & comer
- **distri**: Distri components
- **comer**: Comer components
- **facturacion**: Base invoicing components used in distri & comer
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

# Possible Upgrades

## Images with CSS

Using alt text (or the source) to find the images.

Add your own css in the `docs/extra/css/images.css` directory.

The _css_ may have the format:

```
img[alt="TextFromAlt"]{}
img[src="TextFromSrc"]{}
```

And the _markdown_ image should be like:

```
![TextFromAlt](TextFromSrc)
```

If using alt as a _CSS class_, remember to use an image-defining name and also
translate it. (i.e. alt="icon" [icon->icona / icon->icono])

## Footnotes

We are not using them, but we can add footnotes.

To add footnotes, first it's needed to add footnotes extension to config.yml:
```
vim mkdocs.yml
```
Then append the extension:
```
markdown_extensions:
  - footnotes
```

Use it in any _.md_ document as in [footnotes docs](https://pythonhosted.org/Markdown/extensions/footnotes.html):
```
Footnotes[^1] have a label[^@#$%] and the footnote's content.

[^1]: This is a footnote content.
[^@#$%]: A footnote on the label: "@#$%".

[^1]:
    The first paragraph of the definition.

    Paragraph two of the definition.

    > A blockquote with
    > multiple lines.

        a code block

    A final paragraph.
```
