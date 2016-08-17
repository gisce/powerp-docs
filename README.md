# PowERP documentation

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

With this a webserver is started reloading automatically when is needed

[MKDocs Reference](http://www.mkdocs.org/)

Markdown extensions:

* Tables
* Admonition

## Project structure

We have 4 categories:

- **base**: Base components: used in distri & comer
- **distri**: Distri components
- **comer**: Comer components
- **facturacio**: Base invoicing compoents used in distr & comer

For images we use `_static` folder with a subfolder with the same name as Markdown file. eg:

for `distri/atr.md` we have `distri/_static/atr/image1.png`
