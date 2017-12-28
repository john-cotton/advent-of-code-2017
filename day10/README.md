# Day 10: Knot Hash

https://adventofcode.com/2017/day/10

## Part 1

> Compute a hash that simulates tying a knot in a circle of string
> with 256 marks on it. To do this:
>
>     1. Start with:
>         - a circular list of 256 items (0-255)
>         - a current position of 0
>         - a skip size of 0
>         - your puzzle input: a sequence of lengths
>     2. For each length:
>         - Reverse the order of that length of elements in the list,
>           starting with the element at the current position.
>         - Move the current position forward by that length plus the
>           skip size.
>         - Increase the skip size by one.
>
> After tying all the knots, what is the result of multiplying the
> first two numbers in the list?

## Part 2

> 
