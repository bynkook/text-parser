# text-parser
simple parser for text file, split at space and comma in pythonic way, not relying on RegEx.

-input:
*header, title=text parser
  a,   b,   c,   d,
  e    f    g    h
1  3  9  7
0 0.3456 9.9991
   -1.234 567.9, 34.111,

-output:
return a list containing elements as shown below.

*header title=text parser
a b c d
e f g h
1 3 9 7
0 0.3456 9.9991
-1.234 567.9 34.111
