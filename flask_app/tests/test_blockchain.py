#! *-* coding: UTF-8 *-*
__author__ = "karnikamit"
import unittest
from flask_app.blockchain import BlockChain
from flask_app.block import Block


class TestBlockChain(unittest.TestCase):
    def test_blockchain(self):
        block_chain = BlockChain()
        assert block_chain.chain.__len__() == 1  # blockchain must be initialized with a genesis block

    def test_blockchain_block(self):
        block_chain = BlockChain()
        block = block_chain.chain[0]
        assert isinstance(block, Block)

    def test_add_block(self):
        block1 = Block(1, {"sender": "Amit", "receiver": "Karnik", "amount": 100})
        block2 = Block(2, {"sender": "Amit", "receiver": "Karnik", "amount": 100})
        blockchain = BlockChain()
        blockchain.add_block(block1)
        blockchain.add_block(block2)
        assert blockchain.is_blockchain_valid()

    def test_add_block_negetive(self):
        block1 = Block(1, {"sender": "Amit", "receiver": "Karnik", "amount": 100})
        block2 = Block(3, {"sender": "Amit", "receiver": "Karnik", "amount": 100})
        blockchain = BlockChain()
        blockchain.add_block(block1)
        blockchain.add_block(block2)
        assert not blockchain.is_blockchain_valid()
