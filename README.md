# Advent of Code 2022
Alexander Enge
2023-12-01

- [Day 1: Trebuchet?! :rocket:](#day-1-trebuchet-rocket)

Hi! :wave:

This repository contains my solutions for the [2023
edition](https://adventofcode.com/2023) of [Advent of
Code](https://adventofcode.com).

From the Advent of Code website:

> **Advent of Code** is an [Advent
> calendar](https://en.wikipedia.org/wiki/Advent_calendar) of small
> programming puzzles for a variety of skill sets and skill levels that
> can be solved in any programming language you like. People use them as
> interview prep, company training, university coursework, practice
> problems, a speed contest, or to challenge each other.

I’ll be using a mix of [Python](https://www.python.org), [Base
R](https://www.r-project.org), and [tidyverse-style
R](https://www.tidyverse.org).

## Day 1: Trebuchet?! :rocket:

### Part one (Python)

``` python
from string import digits

res = 0
with open("data/day_01.txt") as file:
    for line in file:
        digs = [char for char in line if char in digits]
        res += int(digs[0] + digs[-1])

print(res)
```

    56506

### Part two (Python)

``` python
digit_dict = {digit: digit for digit in digits}

number_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for ix, word in enumerate(number_words):
    digit_dict[word] = str(ix + 1)

res = 0
with open("data/day_01.txt") as file:
    for line in file:
        ixs = []
        values = []
        for digit, value in digit_dict.items():
            if digit in line:
                ixs += [line.find(digit), line.rfind(digit)]
                values += [value] * 2
        values = [value for ix, value in sorted(zip(ixs, values))]
        res += int(values[0] + values[-1])

print(res)
```

    56017
