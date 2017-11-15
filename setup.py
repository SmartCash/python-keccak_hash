from distutils.core import setup, Extension

keccak_hash_module = Extension('keccak_hash',
                                 sources = ['keccakmodule.c',
                                            'keccakhash.c',
                                            'sha3/keccak.c'],
                               include_dirs=['.', './sha3'])

setup (name = 'keccak_hash',
       version = '1.4',
       author = 'rc125',
  	   author_email = 'rc125@protonmail.com',
  	   url = 'https://github.com/rc125/python-keccak_hash',
       description = 'Binding for keccak proof of work hashing.',
       ext_modules = [keccak_hash_module])
