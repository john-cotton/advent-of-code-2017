# Day 3: Spiral Memory

https://adventofcode.com/2017/day/3

## Part 1

> How many steps are required to carry the data from the square
> identified in your puzzle input all the way [back to at square 1]?
>
>     17  16  15  14  13
>     18   5   4   3  12
>     19   6   1   2  11
>     20   7   8   9  10
>     21  22  23---> ...

Translation:

*What is the Manhattan (i.e. rectilinear, taxicab, city block)
 distance from 1 to any integer, i, on an Ulam spiral?*

- https://en.wiktionary.org/wiki/Manhattan_distance
- https://en.wikipedia.org/wiki/Ulam_spiral

I've ignored the quadratic polynomials of the form ```4n^2 + bn + c```
that could help determine ```(x, y)``` of any value on the spiral,
thereby allowing:

    taxicab = |x| + |y|

But they are fun to see visually:

- http://primorial-sieve.com/3_Ulam%20spiral%20functions.php

## Part 2

> Store value 1 in square 1. Then, in the same allocation order as
> shown above [for an Ulam spiral], store in each square the sum of
> the values in all adjacent squares, including diagonals. Once a
> square is written, its value does not change.
>
>     147  142  133  122   59
>     304    5    4    2   57
>     330   10    1    1   54
>     351   11   23   25   26
>     362  747  806--->   ...
