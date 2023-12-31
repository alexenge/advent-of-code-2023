# Advent of Code 2023

- [Day 1: Trebuchet?! :rocket:](#day-1-trebuchet-rocket)
- [Day 2: Cube Conundrum :ice_cube:](#day-2-cube-conundrum-ice_cube)
- [Day 3: Gear Ratios :gear:](#day-3-gear-ratios-gear)
- [Day 4: Scratchcards :tickets:](#day-4-scratchcards-tickets)
- [Day 5: Day 5: If You Give A Seed A Fertilizer
  :seedling:](#day-5-day-5-if-you-give-a-seed-a-fertilizer-seedling)

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
R](https://www.r-project.org), and [Tidyverse-style
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

## Day 2: Cube Conundrum :ice_cube:

### Part one (Python)

``` python
import re

ns_max = {"red": 12, "green": 13, "blue": 14}

res = 0
with open("data/day_02.txt") as file:
    for line in file:
        game = re.findall(r"Game (\d+):", line)[0]
        for color, n_max in ns_max.items():
            ns = re.findall(rf"(\d+)\s{color}", line)
            if max(int(n) for n in ns) > n_max:
                game = 0
        res += int(game)

print(res)
```

    2683

### Part two (Python)

``` python
import re

res = 0
with open("data/day_02.txt") as file:
    for line in file:
        prod = 1
        for color in ["red", "green", "blue"]:
            ns = re.findall(rf"(\d+)\s{color}", line)
            prod *= max(int(n) for n in ns)
        res += prod

print(res)
```

    49710

## Day 3: Gear Ratios :gear:

### Part one (Python)

``` python
import re

nums = []
nums_ixs = []
symbs = []
symb_ixs = []
with open("data/day_03.txt") as file:
    for row_ix, line in enumerate(file):
        for match in re.finditer(r"(\d+)", line):
            num = int(match.group())
            nums.append(num)
            col_ixs = range(*match.span())
            nums_ixs.append([(row_ix, col_ix) for col_ix in col_ixs])

        for match in re.finditer(r"[^\w\s\d\.]", line):
            symbs.append(match.group())
            col_ix = match.start()
            symb_ixs.append((row_ix, col_ix))

res = 0
for num, num_ixs in zip(nums, nums_ixs):
    add = 0
    for ixs in num_ixs:
        for row_neighbor in [-1, 0, 1]:
            for col_neighbor in [-1, 0, 1]:
                neighbor_ixs = (ixs[0] + row_neighbor, ixs[1] + col_neighbor)
                if neighbor_ixs in symb_ixs:
                    add = num
    res += add

print(res)
```

    560670

### Part two (Python)

``` python
from math import prod

asterisk_ixs = [ixs for symb, ixs in zip(symbs, symb_ixs) if symb == "*"]
res = 0
for ixs in asterisk_ixs:
    neighbor_nums = set()
    for row_neighbor in [-1, 0, 1]:
        for col_neighbor in [-1, 0, 1]:
            neighbor_ixs = (ixs[0] + row_neighbor, ixs[1] + col_neighbor)
            for num, num_ixs in zip(nums, nums_ixs):
                if neighbor_ixs in num_ixs:
                    neighbor_nums.add(num)
    if len(neighbor_nums) == 2:
        res += prod(neighbor_nums)

print(res)
```

    91622824

## Day 4: Scratchcards :tickets:

### Part one (Python)

``` python
res = 0
ns_wins = []  # Relevant for part two
with open("data/day_04.txt") as file:
    for line in file:
        winning_nums = line.split(":")[1].split("|")[0].split()
        my_nums = line.split(":")[1].split("|")[1].split()
        n_wins = len(set(winning_nums) & set(my_nums))
        ns_wins.append(n_wins)
        if n_wins > 0:
            res += 2 ** (n_wins - 1)

print(res)
```

    19135

### Part two (Python)

``` python
ns_cards = [1] * len(ns_wins)
for ix, (n_cards, n_wins) in enumerate(zip(ns_cards, ns_wins)):
    next_ixs = slice(ix + 1, ix + n_wins + 1)
    for _ in range(n_cards):
        ns_cards[next_ixs] = [n + 1 for n in ns_cards[next_ixs]]

print(sum(ns_cards))
```

    5704953

## Day 5: Day 5: If You Give A Seed A Fertilizer :seedling:

### Part one (Python)

``` python
import re


def update_list_from_dict(l, d):
    return [d[x] if x in d else x for x in l]


dsts, srcs, rans = [], [], []
with open("data/day_05.txt") as file:
    for line in file:
        nums = [int(num) for num in re.findall(r"(\d+)", line)]
        if "seeds" in line:
            seeds = nums
        elif nums:
            dst, src, ran = nums
            dsts.append(dst)
            srcs.append(src)
            rans.append(ran)
        elif line == "\n":
            for ix, seed in enumerate(seeds):
                for dst, src, ran in zip(dsts, srcs, rans):
                    if seed >= src and seed < src + ran:
                        seeds[ix] = seed + dst - src
            dsts, srcs, rans = [], [], []

print(min(seeds))
```

    265018614

### Part two (Python)

``` python
# # Doesn't run as there are too many seeds :(
# dsts, srcs, rans = [], [], []
# with open("data/day_05.txt") as file:
#     for line in file:
#         nums = [int(num) for num in re.findall(r"(\d+)", line)]
#         if "seeds" in line:  # Only this part has changed
#             seeds = []
#             for ix in range(0, len(nums), 2):
#                 seeds += list(range(nums[ix], nums[ix] + nums[ix + 1]))
#             print(seeds)
#         elif nums:
#             dst, src, ran = nums
#             dsts.append(dst)
#             srcs.append(src)
#             rans.append(ran)
#         elif line == "\n":
#             for ix, seed in enumerate(seeds):
#                 for dst, src, ran in zip(dsts, srcs, rans):
#                     if seed >= src and seed < src + ran:
#                         seeds[ix] = seed + dst - src
#             dsts, srcs, rans = [], [], []
#
# print(min(seeds))
```
