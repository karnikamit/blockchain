#! *-* coding: UTF-8 *-*
__author__ = "karnikamit"
from flask_app.block import Block


class BlockChain(object):
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.current_transactions = []

    def create_genesis_block(self):
        return Block(0, {"Genesis"}, "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, block):
        block.previous_hash = self.get_latest_block().hash
        block.hash = block.calculate_hash()
        self.chain.insert(block.index, block)
