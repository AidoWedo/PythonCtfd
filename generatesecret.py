# Generate Secret for Secret Key value in Ctfd docker_compose.yml
# Either run this from a python cmd prompt or run the file
import os, binascii
binascii.hexlify(os.urandom(24))
