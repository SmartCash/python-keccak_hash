import keccak_hash
from binascii import unhexlify, hexlify

import unittest

# smartcash block #1
# rc125@ubuntu:~/.smartcash$ smartcashd getblockhash 1
# 00000009c4e61bee0e8d6236f847bb1dd23f4c61ca5240b74852184c9bf98c30
# rc125@ubuntu:~/.smartcash$ smartcashd getblock 000007d91d1254d60e2dd1ae580383070a4ddffa4c64c2eeb4a2f9ecc0414343
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

# header_hex = ("version" + -> ok
#    "prevBlockHash" +
#    "rootHash"
#    "time" + -> ok
#    "bits" + 
#    "nonce") -> ok


header_hex = ("02000000" +
    "b67a40f3cd5804437a108f105533739c37e6229bc1adcab385140b59fd0f0000" +
    "a71c1aade44bf8425bec0deb611c20b16da3442818ef20489ca1e2512be43eef"
    "BCFB6459" +
    "f0ff0f1e" + 
    "3682BB08")



best_hash = '434341c0ecf9a2b4eec2644cfadf4d0a07830358aed12d0ed654121dd9070000'

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex)
        self.best_hash = best_hash

    def test_keccak_hash(self):
        self.pow_hash = hexlify(keccak_hash.getPoWHash(self.block_header))
        self.assertEqual(self.pow_hash, self.best_hash)


if __name__ == '__main__':
    unittest.main()

