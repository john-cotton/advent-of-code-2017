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

> The above represents one *round*.

> Instead of list of numbers, your input is a byte_string. Convert it
> to ASCII codes, and then append the standard suffix:
> [17, 31, 73, 47, 23].
>
> Perform 64 rounds, using the same sequence of lengths each time, but
> preserving the position and skip across rounds.
>
> The result is the *sparse hash*, a 256-element list (with the
> numbers from 0 to 255 in some order!)  consisting of 16 *blocks* of
> 16 elements each. Convert it to a *dense hash* by XOR'ing all
> elements of a block together, to produce a list of 16 elements.
>
> Finally, represent the *Knot Hash* as a single 32-character
> hexadecimal string, by concatenating each of the 16 elements in the
> dense hash as 2-character hex (0-f) values.
>
> What is the Knot Hash of your puzzle input?
