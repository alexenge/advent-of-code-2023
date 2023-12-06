import re


def update_list_from_dict(l, d):
    return [d[x] if x in d else x for x in l]


dsts, srcs, rans = [], [], []
with open("data/day_05.txt") as file:
    for line in file:
        nums = [int(num) for num in re.findall(r"(\d+)", line)]
        if "seeds" in line:
            seeds = []
            for ix in range(0, len(nums), 2):
                seeds += list(range(nums[ix], nums[ix] + nums[ix + 1]))
                print(seeds)
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
