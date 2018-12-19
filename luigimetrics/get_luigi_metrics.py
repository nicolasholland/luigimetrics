import os
from selenium import webdriver
import time
import yaml



def get_task_and_number(element):
    """
    Get task name and number of tasks from WebElement.

    Parameters
    ----------
    element : selenium.webdriver.remote.webelement.WebElement

    Returns
    -------
    name : string
    number : int
    """
    name = element.find_element_by_class_name('info-box-text').text
    number = element.find_element_by_class_name('info-box-number').text

    return name, int(number)


def read_luigi_scheduler(url, buffertime, path_to_driver=None):
    """ load webpage and scrape task info

    Parameters
    ----------
    url : string
        e.g. http://localhost:8082/static/visualiser/index.html#
    buffertime: int
        time to load luigi server.
    path_to_driver : string, default None
        e.g. /srv/phantomjs-2.1.1-linux-x86_64/bin/phantomjs

    Returns
    -------
    retval : dict
        e.g. {'PENDING TASKS': 67, 'RUNNING TASKS': 3, ... }
    """
    if path_to_driver is not None:
        driver = webdriver.PhantomJS(path_to_driver)
    else:
        driver = webdriver.PhantomJS()

    driver.get(url)
    time.sleep(buffertime)

    info_boxes = driver.find_elements_by_class_name('info-box-content')
    retval = dict(get_task_and_number(e) for e in info_boxes)
    return retval


def create_metrics(task_dict):
    """ Turns task dictionary into hostable string """
    retval = "\n".join(['luigi_tasks{code="%s"} %d'
                        % (key.lower().replace(' ', '_'), task_dict[key])
                        for key in task_dict.keys()])
    return retval



