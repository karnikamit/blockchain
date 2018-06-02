#! *-* coding: UTF-8 *-*
__author__ = "karnikamit"
import hashlib
from datetime import datetime
creation_time = datetime.now()


class Block(object):
    def __init__(self, index, data, previous_hash=''):
        self.index = index
        self.timestamp = creation_time
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256()
