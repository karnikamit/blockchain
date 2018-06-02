#! *-* coding: UTF-8 *-*
__author__ = "karnikamit"
import hashlib
from datetime import datetime
import json


class Block(object):
    def __init__(self, index, data, previous_hash=''):
        self.index = index
        self.timestamp = "{:%B %d, %Y}".format(datetime.now())
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash_obj = hashlib.sha256(self.index.__str__().encode('utf-8') + self.timestamp.__str__().encode('utf-8') +
                                  self.previous_hash.__str__().encode('utf-8'))
        return hash_obj.hexdigest()

    # def ____(self):
    #     return {"index": self.index, "timestamp": self.timestamp,
    #             "previous_hash": self.previous_hash, "hash": self.hash,
    #             "data": self.data}
