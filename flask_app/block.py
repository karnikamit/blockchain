#! *-* coding: UTF-8 *-*
__author__ = "karnikamit"
import hashlib
from datetime import datetime


class Block(object):
    def __init__(self, index, data, previous_hash=''):
        self.index = index
        self.timestamp = datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash = hashlib.sha256(self.index.__str__().encode('utf-8') + self.timestamp.__str__().encode('utf-8') +
                              self.previous_hash.__str__().encode('utf-8'))
        return hash.hexdigest()
