# Day 6: Memory Reallocation

https://adventofcode.com/2017/day/6

## Part 1

> Infinite loop detection.

> There are 16 memory *banks*; each memory bank can hold any number of
> *blocks*. The reallocation routine aims to balance the blocks
> between the memory banks, using the following redistribution
> algorithm in each *cycle*:

> - Pick the memory bank with the most blocks (ties to lowest bank).
> - Remove all N blocks from the bank
> - Distribute blocks via:
>     - moving to next block (by index)
>     - inserting 1 block of the N (until none remain)
>

> For the input, how many redistribution cycles can run before a
> (blocks-in-banks) distribution is seen again.

## Part 2

> How many cycles are in the infinite loop that arises from the
> configuration in your puzzle input?
