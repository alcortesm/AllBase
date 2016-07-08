.. image:: https://travis-ci.org/alcortesm/AllBase.svg?branch=master
    :target: https://travis-ci.org/alcortesm/AllBase
.. image:: https://codecov.io/gh/alcortesm/AllBase/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/alcortesm/AllBase

AllBase
=======

AllBase is a python 3 script to show numbers in different bases (binary, octal,
decimal and hexadecimal).

Its main purpose is to be used as a quick CLI command to help during hacking
sessions.  This is also a good excuse for me to learn Python.

Examples
--------

Here is how to print 42 in decimal, hexadecimal, octal and binary:

::

    ; python3 -m allbase 42
    42 0x2a 0o52 0b101010

The **-f** optional argument ("format") allows you to select the order
and format of the output using a string containing the followin
characters:

- **d** for decimal
- **h** for hexadecimal
- **o** for octal
- **b** for binary.

If the "-b" argument is not present the default format is **dhob**:

::

    ; python3 -m allbase 42 -f d
    42
    ; python3 -m allbase 42 -f o
    0o52
    ; python3 -m allbase 42 -f booh
    0b101010 0o52 0o52 0x2a


You can also ask for several numbers at once, the columns will align nicely:

::

    ; python3 -m allbase -f dob 1 7 248
      1 0o001 0b00000001
      7 0o007 0b00000111
    248 0o370 0b11111000


Installation
------------

TODO.

Tests
-----

Run the test with:

::

    ; make test
    python3 -m unittest
    ....
    ----------------------------------------------------------------------
    Ran 4 tests in 0.004s
    
    OK


Check code coverage with:

::

    ; make coverage 
    nosetests3 --with-coverage --cover-package=allbase --cover-erase --cover-tests --cover-inclusive --cover-html --cover-branches
    ....
    Name             Stmts   Miss Branch BrMiss  Cover   Missing
    ------------------------------------------------------------
    allbase              0      0      0      0   100%   
    allbase.args        37      0     14      0   100%   
    allbase.base        29      0     14      0   100%   
    allbase.tobase       9      0      8      0   100%   
    ------------------------------------------------------------
    TOTAL               75      0     36      0   100%   
    ----------------------------------------------------------------------
    Ran 4 tests in 0.028s
    
    OK

Authors
-------

- Alberto Cortés <alcortesm@gmail.com>.

License
-------

This project is licensed under the MIT License - see the LICENSE
file for details.

