#! *-* coding: utf-8 *-*
__author__ = "karnikamit"
from flask import Flask
from flask_app.blockchain import BlockChain
import logging

logging.basicConfig(format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

blockchain = BlockChain()
app = Flask(__author__)
