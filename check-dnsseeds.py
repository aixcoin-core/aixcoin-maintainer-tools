#!/usr/bin/env python3
'''
Simple script to check the status of all Aixcoin Core DNS seeds.
Seeds are available from https://github.com/aixcoin/aixcoin/blob/master/src/kernel/chainparams.cpp
'''
import subprocess

SEEDS_PER_NETWORK={
    'mainnet': [
        "seed.aixcoin.sipa.be",
        "dnsseed.bluematt.me",
        "seed.aixcoin.jonasschnelli.ch",
        "seed.aix.petertodd.net",
        "seed.aixcoin.sprovoost.nl",
        "dnsseed.emzy.de",
        "seed.aixcoin.wiz.biz",
        "seed.mainnet.achownodes.xyz",
    ],
    'testnet': [
        "testnet-seed.aixcoin.jonasschnelli.ch",
        "seed.taix.petertodd.net",
        "testnet-seed.bluematt.me",
        "seed.testnet.aixcoin.sprovoost.nl",
        "seed.testnet.achownodes.xyz",
    ],
    'testnet4': [
        "seed.testnet4.aixcoin.sprovoost.nl",
        "seed.testnet4.wiz.biz",
    ],
    'signet': [
        "seed.signet.aixcoin.sprovoost.nl",
        "seed.signet.achownodes.xyz"
    ],
}

def check_seed(x):
    p = subprocess.run(["host",x], capture_output=True, universal_newlines=True)
    out = p.stdout

    # Parse matching lines
    addresses = []
    for line in out.splitlines():
        if "has address" in line or "has IPv6 address" in line:
            addresses.append(line)

    if addresses:
        print(f"\x1b[94mOK\x1b[0m   {x} ({len(addresses)} results)")
    else:
        print(f"\x1b[91mFAIL\x1b[0m {x}")

if __name__ == '__main__':
    for (network, seeds) in SEEDS_PER_NETWORK.items():
        print(f"\x1b[90m* \x1b[97m{network}\x1b[0m")

        for hostname in seeds:
            check_seed(hostname)

        print()
