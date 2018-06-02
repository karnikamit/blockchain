#! *-* coding: UTF-8 *-*
__author__ = "karnikamit"
from flask_app.block import Block


class BlockChain(object):
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.current_transactions = []

    @staticmethod
    def create_genesis_block():
        return Block(0, {"Genesis"}, "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, block):
        block.previous_hash = self.get_latest_block().hash
        block.hash = block.calculate_hash()
        self.chain.append(block)

    def is_blockchain_valid(self):
        for block in self.chain[1:]:    # 1st block is always the genesis
            previous_index = block.index - 1
            prev_block = self.chain[previous_index]
            if block.previous_hash != prev_block.hash:
                return False
        else:
            return True
