# Day 9: Stream Processing

https://adventofcode.com/2017/day/9

## Part 1

> A stream of characters contains {}-delimited groups with zero or
> more comma-separated items, either another group or <>-delimited
> garbage. That is, groups can be nested, and both braces and angle
> brackets have no special meaning within garbage.
>
> Inside garbage, any character immediately after '!' should be
> ignored.
>
> The first group scores 1. After that, a group's score is one more
> than the score of the group that contains it.
>
> What is the total score for all groups in your input?

## Part 2

> Also, count all of the characters within the garbage. The leading
> and trailing < and > don't count, nor do any canceled characters or
> the ! doing the canceling.
>
> How many non-canceled characters are within the garbage in your
> puzzle input?
