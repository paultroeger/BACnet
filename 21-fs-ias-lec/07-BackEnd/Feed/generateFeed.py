import sys

# add the lib to the module folder
sys.path.append("./lib")

import os
import crypto
import feed

## Dependencies:
# - [cbort2](https://pypi.org/project/cbor2/)
# Run pip3 install cbor2

if not os.path.isdir("data"):
    os.mkdir("data")
    os.mkdir("data/alice")
    os.mkdir("data/bob")

# Generate a key pair

## Alice

name = sys.argv[1]
digestmod = "sha256"
h, signer = None, None

# Generate a Key if non exists
if not os.path.isfile("data/" + name + "/" + name + "-secret.key"):
    print("Create " + name + "'s key pair at data/" + name + "/" + name + "-secret.key")
    h = crypto.HMAC(alice_digestmod)
    h.create()
    with open("data/" + name + "/" + name + "-secret.key", "w") as f:
        f.write('{\n  ' + (',\n '.join(h.as_string().split(','))[1:-1]) + '\n}')
        signer = crypto.HMAC(digestmod, h.get_private_key())

print("Read " + name + "'s secret key.")
with open("data/" + name + "/" + name + "-secret.key", 'r') as f:
    key = eval(f.read())
    h = crypto.HMAC(digestmod, key["private"], key["feed_id"])
    signer = crypto.HMAC(digestmod, bytes.fromhex(h.get_private_key()))

print("Create or load" + name + "'s feed at data/" + name + "/" + name + "-feed.pcap")
myfeed = feed.FEED(fname="data/" + name + "/" + name + "-feed.pcap", fid=h.get_feed_id(), signer=signer,
                       create_if_notexisting=True, digestmod=digestmod)

## Bob
#bob_digestmod = "sha256"
#bob_h, bob_signer = None, None

#if not os.path.isfile("data/bob/bob-secret.key"):
#    print("Create Bob's key pair at data/bob/bob-secret.key")
#    bob_h = crypto.HMAC(bob_digestmod)
#    bob_h.create()
#    with open("data/bob/bob-secret.key", "w") as f:
#        f.write('{\n  ' + (',\n '.join(bob_h.as_string().split(','))[1:-1]) + '\n}')

#print("Read Bob's secret key.")
#with open("data/bob/bob-secret.key", 'r') as f:
#    key = eval(f.read())
#    bob_h = crypto.HMAC(bob_digestmod, key["private"], key["feed_id"])
#    bob_signer = crypto.HMAC(bob_digestmod, bytes.fromhex(bob_h.get_private_key()))

#print("Create or load Boby's feed at data/bob/bob-feed.pcap")
#bob_feed = feed.FEED(fname="data/bob/bob-feed.pcap", fid=bob_h.get_feed_id(), signer=bob_signer,
#                     create_if_notexisting=True, digestmod=bob_digestmod)
