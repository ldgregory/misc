# misc
Miscellaneous scripts that don't deserve a whole repository

## 8ball.py
Like the magic 8-Ball, returns a random response


## CryptFile.py
Encrypts and decrypts files with AES-256 CBC

### Input
* -d: Decrypt file
* -e: Encrypt file
* -i: File to encrypt
* -o: Output encrypted file
* -r: Remove input file after encryption

**Encrypt a file**
* cryptfile.py -e -i input.txt -o output.txt -p password

**Encrypt a file and remove the original after encryption**
* cryptfile.py -e -r -i input.txt -o output.txt -p password

**Decrypt a file**
* cryptfile.py -d -i input.txt -o output.txt -p password


## DieRoller.py
Rolls one or more die, one or more times, with or without modifiers and outputs the results.

### Input
Input rolls in form of 1d20, 5d12 etc.: **2d10+2, 1d20-1, 3d6**

This will roll a d10 two times and add two to each rolled result, roll a d20 one time and subtract 1 from the rolled result, roll a d6 three times with no modifier.

### Output
Rolls: d10+2: 9, d10+2: 8, d20-1: 6, d6: 6, d6: 2, d6: 6

Total: 37
