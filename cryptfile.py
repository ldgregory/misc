#! /usr/bin/env python3

"""
Leif Gregory <leif@devtek.org>
cryptfile.py v1.0
Tested to Python v3.10.7

Description:
Encrypt or Decrypt a file using AES-256 CBC

Changelog:
20190420 -  Initial code

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import argparse
import pyAesCrypt
from os import path, remove, stat


def main():
    parser = argparse.ArgumentParser(description='Encrypt/Decrypt file using AES-256 CBC')
    parser.add_argument('-d', help='decrypt file', action='store_true', dest='decrypt')
    parser.add_argument('-e', help='encrypt file', action='store_true', dest='encrypt')
    parser.add_argument('-r', help='remove input file', action='store_true', dest='remove')
    parser.add_argument('-i', type=str, required=True, help='input filename', dest='infile')
    parser.add_argument('-p', type=str, required=True, help='decryption/encryption password', dest='password')
    parser.add_argument('-o', type=str, required=True, help='output filename', dest='outfile')
    parser.add_argument('-v', action='version', version='%(prog)s 1.0', dest='version')
    args = parser.parse_args()

    if args.decrypt or args.encrypt:
        if path.isfile(args.infile):
            encFileSize = stat(args.infile).st_size
            bufferSize = 64 * 1024

            if args.decrypt:  # Decrypt
                with open(args.infile, 'rb') as fIn:
                    with open(args.outfile, 'wb') as fOut:
                        try:
                            pyAesCrypt.decryptStream(fIn, fOut, args.password, bufferSize, encFileSize)
                            print(f"{args.infile} successfully decrypted to {args.outfile}")
                        except ValueError:
                            print(f"Incorrect decryption password for {args.infile}")
                            remove(args.outfile)

            elif args.encrypt:  # Encrypt
                with open(args.infile, 'rb') as fIn:
                    with open(args.outfile, 'wb') as fOut:
                        try:
                            pyAesCrypt.encryptStream(fIn, fOut, args.password, bufferSize)
                            if args.remove:
                                remove(args.infile)
                            print(f"{args.infile} successfully encrypted to {args.outfile}")
                        except ValueError:
                            print(f"Failed to encrypt {args.infile}.")
        else:
            print(f"Error: input file {args.infile} does not exist.")
    else:
        print(f"You must enter either -d (to decrypt) or -e (to encrypt)")


if __name__ == '__main__':
    main()
