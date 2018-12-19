import os
import yaml
from flask import Flask, render_template
from luigimetrics.get_luigi_metrics import read_luigi_scheduler, create_metrics

YMLFILE = open(os.path.join(os.path.dirname(__file__), "config.yml"), 'r')
CFG = yaml.load(YMLFILE)

URL = CFG['luigi_url']
PATH_TO_DRIVER = CFG['path_to_driver']
BUFFERTIME = CFG['buffertime']

app = Flask(__name__)

@app.route("/metrics")
def metrics():
    """ Create luigi metrics page """
    task_dict = read_luigi_scheduler(URL, BUFFERTIME, PATH_TO_DRIVER)
    metrics = create_metrics(task_dict)
    return render_template('template.html', content=metrics)


