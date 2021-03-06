#coding:utf-8

import os
import logging
import logging.config
import ConfigParser

global logger

'''load logging file'''
def logging_conf():
    global logger
    logging.config.fileConfig('./conf/logging.conf')
    logger = logging.getLogger('general')

'''load configuration file'''
def get_config(section):
    logging_conf()
    config = ConfigParser.ConfigParser()
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    service_conf = os.path.join(cur_dir, './conf/config.ini')
    try:
        config.read(service_conf)
        conf_items = dict(config.items(section))
    except Exception as e:
        logging.error('load config file error, %s', e)
        conf_items = {}
    return conf_items

logging_conf()
logger.debug('123')
