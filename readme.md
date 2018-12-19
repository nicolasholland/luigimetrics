Luigimetrics
============

Package to scrape task infos from a luigid server to be used with prometheus.
We're using conda environments to install dependencies.

Luigi
-----

First you need luigi and a luigi server:

```
$ conda install luigi
$ luigid --background
```

More on luigi [here](https://luigi.readthedocs.io/en/stable/central_scheduler.html).


Luigimetrics
------------

Now you can start setting up luigimetrics by installing its dependencies:

```
$ conda install selenium
$ conda install pyyaml
$ conda install flask
```

In order to scrape the luigi server we use PhantomJS.
It can be either installed [here](http://phantomjs.org/download.html) or also using conda:

```
$ conda install -c conda-forge phantomjs
```

Configure luigimetrics by writing into the config.yml:

```
luigimetrics/config.yml
```

This is how it could look like:

```
---
luigi_url: 'http://localhost:8082/static/visualiser/index.html#'
buffertime: 3
path_to_driver:
```

Install luigimetrics e.g. using pip:

```
$ pip install -e .
```

Run luigimetrics:

```
$ export FLASK_APP=luigimetrics
$ flask run
```


Prometheus
----------

Install Prometheus [here](https://prometheus.io/docs/prometheus/latest/getting_started/)
There is a prometheus configuration in this package: prometheus.yml
Prometheus can be started like this:

```
$ prometheus --config.file=prometheus.yml
```

