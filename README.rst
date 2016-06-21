Allbase
=======

Allbase is a python 3 script to show numbers in different bases (binary, octal,
decimal and hexadecimal).

Its main purpose is to be used as a quick CLI command to help during hacking
sessions.  This is also a good excuse to learn Python.

Installation
------------

TODO.

Run the command
---------------

::
    ; python3 -m allbase 12
    12 0xC 0o014 0b1100

Run the tests
-------------

::
    ; pushd allbase ; python3 -m unittest ; popd allbase

Examples
--------

::
    ; python3 allbase.py 0
     0 0x0 0o000 0b0000
    ; python3 allbase.py 1
     1 0x1 0o001 0b0001

::
    ; python3 allbase.py 42
     42 0x2A 0o052 0b00101010
    ; python3 allbase.py 42
     43 0x2B 0o053 0b00101011

::
    ; python3 allbase.py 1234
     1234 0x04D2 0o002322 0b0000010011010010
    ; python3 allbase.py 1235
     1235 0x04D3 0o002323 0b0000010011010011

::
    ; fish
    ; for n in (seq 0 1000) ; python3 allbase.py $n; end
     0 0x0 0o000 0b0000
     1 0x1 0o001 0b0001
    [...]
    14 0xE 0o016 0b1110
    15 0xF 0o017 0b1111
     16 0x10 0o020 0b00010000
     17 0x11 0o021 0b00010001
    [...]
    254 0xFE 0o376 0b11111110
    255 0xFF 0o377 0b11111111
      256 0x0100 0o000400 0b0000000100000000
      257 0x0101 0o000401 0b0000000100000001
    [...]
      999 0x03E7 0o001747 0b0000001111100111
     1000 0x03E8 0o001750 0b0000001111101000

Authors
-------

- Alberto Cortés <alcortesm@gmail.com>.

License
-------

This project is licensed under the MIT License - see the LICENSE
file for details.

