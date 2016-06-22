Allbase
=======

Allbase is a python 3 script to show numbers in different bases (binary, octal,
decimal and hexadecimal).

Its main purpose is to be used as a quick CLI command to help during hacking
sessions.  This is also a good excuse to learn Python.

Here is an example of use:

::

    ; python3 -m allbase 42
    42 0x2a 0o52 0b101010

Installation
------------

TODO.

Tests
-----

Run the test with:::

    ; make test
    python3 -m unittest
    ....
    ----------------------------------------------------------------------
    Ran 4 tests in 0.004s
    
    OK


Check code coverage with:::

    ; make coverage
    nosetests3 --with-coverage --cover-package=allbase --cover-erase --cover-tests --cover-inclusive --cover-html --cover-branches
    ....
    Name             Stmts   Miss Branch BrMiss  Cover   Missing
    ------------------------------------------------------------
    allbase              0      0      0      0   100%   
    allbase.args        27      1      8      1    94%   34
    allbase.base        28      0     16      0   100%   
    allbase.tobase       3      0      2      0   100%   
    ------------------------------------------------------------
    TOTAL               58      1     26      1    98%   
    ----------------------------------------------------------------------
    Ran 4 tests in 0.019s
    
    OK

Examples
--------

::

    ; python3 -m allbase 42
    42 0x2a 0o52 0b101010

::

    ; python3 -m allbase -h
    usage: __main__.py [-h] [-b BASES] number
    
    Shows numbers in several bases (hex, oct...)
    
    positional arguments:
      number                the number you want to show
    
    optional arguments:
      -h, --help            show this help message and exit
      -b BASES, --bases BASES
                            one or more output bases and their order. Use 'h' for
                            hex, 'd' for decimal, 'o' for octal and 'b' for
                            binary. Default: 'dhob'.

::

    ; python3 -m allbase 42 -b d
    42

::

    ; python3 -m allbase 42 -b booh
    0b101010 0o52 0o52 0x2a


Authors
-------

- Alberto Cortés <alcortesm@gmail.com>.

License
-------

This project is licensed under the MIT License - see the LICENSE
file for details.

