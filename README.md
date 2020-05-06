# Python task. Sort CSV file by the parent-child relationship column

Given a CSV file with parent-child relationship column, this task sort the rows. Optionaly it creates a new column with the depth tree.

## Input file

| plid    | layoutId | parentLayoutId | name  | priority |
|---------|----------|----------------|-------|----------|
| 7004446 | 74       | 1              | Lorem | 15       |
| 8152170 | 205      | 1              | Ipsum | 10       |
| 6724205 | 1        | 0              | Amet  | 0        |
| 8152195 | 206      | 205            | Dolor | 0        |
| 8220383 | 222      | 205            | Sit   | 1        |

## Output file

| plid    | layoutId | parentLayoutId | name  | priority | __ auto_generated_depth_col __ |
|---------|----------|----------------|-------|----------|--------------------------------|
| 6724205 | 1        | 0              | Amet  | 0        | 0                              |
| 8152170 | 205      | 1              | Ipsum | 10       | 1                              |
| 8152195 | 206      | 205            | Dolor | 0        | 2                              |
| 8220383 | 222      | 205            | Sit   | 1        | 2                              |
| 7004446 | 74       | 1              | Lorem | 15       | 1                              |

## Arguments

| Argument          | Value   | Requited | Description                                            |
|-------------------|---------|----------|--------------------------------------------------------|
| -h, --help        |         | False    | Show help message and exit.                            |
| --inputfile       | String  | True     | Input file name.                                       |
| --outputfile      | String  | False    | Output file name.                                      |
| --childcol        | Integer | False    | Child column number (default value 0: first column).   |
| --parentcol       | Integer | False    | Parent column number (default value 1: second column). |
| --prioritycol     | Integer | False    | Priority column number.                                |
| --parentrootid    | Integer | False    | Parent root ID (default value 0).                      |
| --ignoreheaderrow |         | False    | Ignore first row (header).                             |
| --adddepthcol     |         | False    | Add new column with tree depth.                        |

### Example

> py main.py --inputfile example/pages.csv --childcol 1 --parentcol 2 --prioritycol 4 --ignoreheaderrow --adddepthcol