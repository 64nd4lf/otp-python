# otp-python
Implementing OTP encryption in Python along with performance evaluation.

Language used: Python
OS used: Arch Linux

File descriptions:
plaintext128.txt - Contains 128 bit plaintext to be encrypted
ciphertext128.txt - Contains 128 bit cipher text output from encrypting 128 bit plaintext
key128.txt - Contains 128 bit encryption key
result128.txt - Contains the decrypted 128 bit message
newkey.txt - Key generated using keygen is stored here
plaintext.txt - contains the default plaintext, "bear" in it
result.txt - Contains the decrypted message
ciphertext.txt - Contains the encrypted message in binary
key.txt - Contains the default key
key_dist.py - Generates 5000 keys of length 3 and prints frequencies of each key
otp.py - Simulates OTP encryption
otp_timer - Similar to otp but imports timeit library to measure execution time. Used with a 128 bit key to measure encryption time.

How to use:

1. Encryption
python otp enc /path/to/key.txt /path/to/plaintext.txt /path/to/ciphertext.txt
2. Decryption
python otp dec /path/to/key.txt /path/to/ciphertext.txt /path/to/result.txt
3. KeyGen
python otp keygen <length> /path/to/newkey.txt

Example runs:

To encrypt
[root@archel src]# python otp.py enc /root/Documents/otp_12499347/data/key.txt /root/Documents/otp_12499347/data/plaintext.txt /root/Documents/otp_12499347/data/ciphertext.txt
00110111110011111001000101111101
[root@archel src]# 

To decrypt
[root@archel src]# python otp.py dec /root/Documents/otp_12499347/data/key.txt /root/Documents/otp_12499347/data/ciphertext.txt /root/Documents/otp_12499347/data/result.txt
bear
[root@archel src]# 

KeyGen
[root@archel src]# python otp.py keygen 3 /root/Documents/otp_12499347/data/newkey.txt
[root@archel src]# 

Key Distribution exercise:

To generate and see the keys and their frequencies run 
python key_dist.py

To measure the encryption time, run
python otp_timer.py enc /path/to/key128.txt /path/to/plaintext128.txt /path/to/ciphertext128.txt

Example runs:

Key distribution:
[root@archel src]# python key_dist.py
000 606
111 616
101 617
001 647
011 597
110 655
010 623
100 639
[root@archel src]# 

Run time measurement (encryption, run 3 times):
[root@archel src]# python otp_timer.py enc /root/Documents/otp_12499347/data/key128.txt /root/Documents/otp_12499347/data/plaintext128.txt /root/Documents/otp_12499347/data/ciphertext128.txt
00110001110010111000010001101110001001101100111110010011011110100010011111011010100000100110011000100011110010111001001101110110
0.0006769129977328703
[root@archel src]# python otp_timer.py enc /root/Documents/otp_12499347/data/key128.txt /root/Documents/otp_12499347/data/plaintext128.txt /root/Documents/otp_12499347/data/ciphertext128.txt
00110001110010111000010001101110001001101100111110010011011110100010011111011010100000100110011000100011110010111001001101110110
0.0006305269998847507
[root@archel src]# python otp_timer.py enc /root/Documents/otp_12499347/data/key128.txt /root/Documents/otp_12499347/data/plaintext128.txt /root/Documents/otp_12499347/data/ciphertext128.txt
00110001110010111000010001101110001001101100111110010011011110100010011111011010100000100110011000100011110010111001001101110110
0.0006695629999740049
[root@archel src]# 
