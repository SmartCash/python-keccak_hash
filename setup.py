from distutils.core import setup, Extension

keccak_hash_module = Extension('keccak_hash',
                                 sources = ['keccakmodule.c',
                                            'keccakhash.c',
                                            'sha3/blake.c',
                                            'sha3/bmw.c',
                                            'sha3/groestl.c',
                                            'sha3/jh.c',
                                            'sha3/keccak.c',
                                            'sha3/skein.c',
                                            'sha3/cubehash.c',
                                            'sha3/echo.c',
                                            'sha3/luffa.c',
                                            'sha3/simd.c',
                                            'sha3/shavite.c'],
                               include_dirs=['.', './sha3'])

setup (name = 'keccak_hash',
       version = '1.4',
       description = 'Binding for keccak proof of work hashing.',
       ext_modules = [keccak_hash_module])
