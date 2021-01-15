import hashlib
import json
from time import time

class Blockchain(object):
    def __int__(self):
        self.chain = []
        self.pending_transactions = []
        