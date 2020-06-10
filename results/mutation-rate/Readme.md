## Description

This file contains the results of a mutation rate experiment in which the genetic algorithm using values between 0.005-0.03 for this hyperparameter.
The experiment was performed on an Ubuntu Linux operating system with 160 frames per second in-game speed.

## Results

Full results can be found in `Log.[1-3].txt`.

### Summary

Average of three iteration. Marked in bold are results better that are the best in each generation.

**Legend:** gen = generation, mut = mutation rate

#### Average Player

| gen/mut |  0.005 | 0.01 | 0.015 | 0.02 |   0.025 | 0.03 |
| ------- | -----: | ---: | ----: | ---: | ------: | ---: |
| 1       |     21 |   21 |    21 |   21 |      21 |   21 |
| 2       | **31** |   30 |    30 |   29 |      29 |   29 |
| 3       | **57** |   36 |    36 |   43 |      43 |   35 |
| 4       | **86** |   61 |    58 |   56 |      80 |   40 |
| 5       |     56 |   56 |    56 |   59 | **155** |   53 |
| 6       |     56 |   56 |    58 |   72 | **142** |   43 |
| 7       |     56 |   79 |    70 |   58 | **402** |   62 |
| 8       |     56 |   56 |    56 |   74 | **278** |   56 |
| 9       |     99 |   83 |    77 |  130 | **455** |   68 |
| 10      |     56 |   56 |    56 |  303 | **377** |   58 |

#### Best Player

| gen/mut | 0.005 | 0.01 | 0.015 |    0.02 |   0.025 |   0.03 |
| ------- | ----: | ---: | ----: | ------: | ------: | -----: |
| 1       |    64 |   64 |    64 |      64 |      64 |     64 |
| 2       |    60 |   88 |    88 |      88 |      88 | **89** |
| 3       |    93 |   61 |    88 |     435 | **528** |     61 |
| 4       |    94 |   92 |    92 |     153 | **750** |     90 |
| 5       |    62 |   62 |    62 |     305 | **750** |     90 |
| 6       |    62 |   62 |    91 |     621 | **751** |     91 |
| 7       |    62 |   94 |    93 |     156 | **751** |     93 |
| 8       |    62 |   62 |    62 |     750 | **751** |     62 |
| 9       |   125 |   94 |    94 | **751** | **751** |     93 |
| 10      |    62 |   92 |    62 | **751** | **751** |     90 |
