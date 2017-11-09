#include "keccakhash.h"
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <stdio.h>

#include "sha3/sph_blake.h"
#include "sha3/sph_bmw.h"
#include "sha3/sph_groestl.h"
#include "sha3/sph_jh.h"
#include "sha3/sph_keccak.h"
#include "sha3/sph_skein.h"
#include "sha3/sph_luffa.h"
#include "sha3/sph_cubehash.h"
#include "sha3/sph_shavite.h"
#include "sha3/sph_simd.h"
#include "sha3/sph_echo.h"


void keccak_hash(const char* input, char* output)
{
    sph_keccak256_context    ctx_keccak;

    
    //these uint512 in the c++ source of the client are backed by an array of uint32
    //uint32_t hashA[16], hashB[16];
    
    uint256_t hashA[16], hashB[16];

    sph_keccak256_init(&ctx_keccak);
    sph_keccak256 (&ctx_keccak, hashA, 64);
    sph_keccak256_close(&ctx_keccak, hashB);

    memcpy(output, hashA, 32);

}

