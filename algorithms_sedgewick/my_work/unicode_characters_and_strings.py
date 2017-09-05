import socket


"""
 What computers understand is numbers, and so we had to come up with a mapping between letters and numbers.

I. ASCII => the most common mapping of the 1980s
- each no. is represented by a no [0,265] stored in 8 bits(1 byte) of memory (e.g. capital H has numerical value: 72)
- problem: can't put every character into a 0 through 128 => come up with a function ordinal:   >> print(ord('H'))
- What is the actual value for the letter H? What's the ordinal? What is the number corresponding to H?   -> 72

DEC  HEX  OCT     BIN  CHAR
72  0x48  110  1001000   H


II. UNICODE
- universal code for hundreds of millions of different characters and hundreds of different character sets


III. UTF-16, UTF-32 and UTF-8
- are basically ways of representing a larger set of characters.
- UTF-32: fixed length, 32 bits = 4 bytes. It's 4 times as much data for a single character => a lot of data =>
- UTF-16: fixed length - 16 bits = 2 bytes per character - can only handle 4 billion characters
- UTF-8: 1-4 bytes => 4 bytes per character => not so efficient

UTF-8
- it's either going to be 1/2/3/4 characters & there's little marks that tell it when to go from 1 to 4
- is the best; overlaps with ASCII; best practice for encoding data moving between systems.

Files, strings are inside the computer, but network connections and databases are not


Decode operation:
- When we talk to an external resource we get a byte array back like the socket gives us an array of bytes which are
characters. But they need to be decoded so we know, if it could be UTF-8/UTF-16/ASCII => use the function that's part of 
byte arrays, so data.decode says figure this thing out (character set is set by default UTF-8/ASCII); because ASCII and 
UTF-8 are upwards compatible with one another. (if it's old data -> probably getting ASCII if newer data -> UTF-8).

An HTTP Request in Python:

---------------         -----------------    
Your          |         | www.py4e.com  |
program       |         |   web pages   |
   |------------        |      .        |
   | socket  |S|----------     .        |
   | connect |O| Port 80 |     .        |
   | send    |C|----------              |
   | recv    |K|         |              |
                         ----------------
   |         |E|
   |         |T|
   |------------
              |
---------------

String Unicode -> encode() -> Bytes UTF-8 -> send() -> Socket
Socket -> recv() -> Bytes UTF-8 -> decode() -> String Unicode   
"""

# ASCII
# uppercase letters are < lowercase letters
print(ord('H'))
print(ord('i'))
print(ord('e'))
print(ord('\n'))

print(ord('G'))
ascii_list = [108, 105, 115, 116]
for i in ascii_list:
    print(chr(i))


# In Python3 all strings internally are Unicode
# regular string and unicode string are the same
# bytes is different than regular string, bytes = raw, uneconded, might be UTF-8, ASCII
x = '中華人民民主共和國'
print(type('x'))
x = u'中華人民民主共和國'
print(type('x'))
x = b'abc'
print(type('x'))


# An HTTP request in Python
# String Unicode -> encode() -> Bytes UTF-8 -> send() -> Socket
# Socket -> recv() -> Bytes UTF-8 -> decode() ->String Unicode
my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/rome.txt HTTP/1.0\n\n'.encode()  # => bytes, encode() assumes encode('UTF-8')
my_sock.send(cmd)


# Decode operation
def decode():
    while True:
        # data is bytes
        data = my_sock.recv(512)
        if len(data) < 1:
            break
        # decode goes from bytes to unicode
        my_string = data.decode()
        print(my_string)