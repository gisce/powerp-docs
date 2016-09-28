# PowERP documentation

[Build of our documentation](http://builds.gisce.net/powerp-docs/powerp/)

## Setting up your environment

```shell
$ mkvirtualenv powerp-docs
$ git clone git@github.com:gisce/powerp-docs.git
$ cd powerp-docs
$ pip install -r requirements.txt
```

## Start documenting

```shell
$ mkdocs serve
```

With this a webserver is started reloading automatically when is needed.

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
