import keccak_hash
from binascii import unhexlify, hexlify

import unittest

# smartcash block #1
# rc125@ubuntu:~/.smartcash$ smartcashd getblockhash 1
# 00000009c4e61bee0e8d6236f847bb1dd23f4c61ca5240b74852184c9bf98c30
# rc125@ubuntu:~/.smartcash$ smartcashd getblock 00000009c4e61bee0e8d6236f847bb1dd23f4c61ca5240b74852184c9bf98c30
# {
#   "hash": "00000009c4e61bee0e8d6236f847bb1dd23f4c61ca5240b74852184c9bf98c30",
#   "confirmations": 172736,
#   "strippedsize": 356,
#   "size": 356,
#   "weight": 1424,
#   "height": 1,
#   "version": 2,
#   "versionHex": "00000002",
#   "merkleroot": "a68bf0e348915b09d7da1d8dae05fb04d9016d06d5d964c4cc85dab8f6b032e9",
#   "tx": [
#    "a68bf0e348915b09d7da1d8dae05fb04d9016d06d5d964c4cc85dab8f6b032e9"
#   ],
#   "time": 1499790268,
#   "mediantime": 1499790268,
#   "nonce": 146506294,
#   "bits": "1e0ffff0",
#   "difficulty": 0.000244140625,
#   "chainwork": "0000000000000000000000000000000000000000000000000000000000200020",
#   "previousblockhash": "000007acc6970b812948d14ea5a0a13db0fdd07d5047c7e69101fa8b361e05a4",
#   "nextblockhash": "00000001d83bf07ff4faddf97a5e68e760f012d6526126b2668aea29bd23bd09"
# }

# header_hex = ("version" +
#    "prevBlockHash" +
#    "rootHash"
#    "time" +
#    "bits" + 
#    "nonce")


header_hex = ("02000000" +
    "a4051e368bfa0191e6c747507dd0fdb03da1a0a54ed14829810b97c6ac070000" +
    "09bd23bd29ea8a66b2266152d612f060e7685e7af9ddfaf47ff03bd801000000"
    "BCFB6459" +
    "f0ff0f1e" + 
    "3682BB08")



best_hash = '308cf99b4c185248b74052ca614c3fd21dbb47f836628d0eee1be6c409000000'

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex)
        self.best_hash = best_hash

    def test_keccak_hash(self):
        self.pow_hash = hexlify(keccak_hash.getPoWHash(self.block_header))
        self.assertEqual(self.pow_hash, self.best_hash)


if __name__ == '__main__':
    unittest.main()

