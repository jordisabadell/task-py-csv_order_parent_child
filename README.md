# Python task. Sort CSV file by the parent-child relationship column

Given a CSV file with parent-child relationship column, this task sort the rows. Optional it creates a new column with tree format.

## Format of input file

- Type of file CSV.
- By defalult separaded with tabulates (you can change it).
- First row reserved by header.
- Child and Parent columns are required. Priority and content columns are optional.

### Input file

| Child ID | Parent ID | Priority   | Col X      | Col Y    | Col Z      |
|----------|-----------|------------|------------|----------|------------|
| 1        | 3         | 0          | Lorem      | Ipsum    | dolor      |
| 2        | 3         | 1          | sit        | amet     | consetetur |
| 3        | 4         | 0          | sadipscing | elitr    | sed        |
| 4        | 0         | 0          | diam       | nonumy   | eirmod     |
| 5        | 1         | 0          | tempor     | invidunt | ut         |

### Output file

| Child ID | Parent ID | Priority   | Col X      | Col Y    | Col Z      | New col       |
|----------|-----------|------------|----------|------------|------------|---------------|
| 4        | 0         | 0          | diam       | nonumy   | eirmod     | diam          |
| 3        | 4         | 0          | sadipscing | elitr    | sed        | -- sadipscing |
| 2        | 3         | 1          | sit        | amet     | consetetur | ---- sit      |
| 1        | 3         | 0          | Lorem      | Ipsum    | dolor      | ---- Lorem    |
| 5        | 1         | 0          | tempor     | invidunt | ut         | ------ tempor |

## Arguments

### Required

- **Input file name**. Type STRING. If path is not current path, you must specify it.
- **Child column name**. Type STRING.
- **Parent column name**. Type STRNG.

### Optional

- **Parent root ID**. Type STRING. Default 0.
- **Priority column name**. Type STRING. Default 'empty' equals not sorted by priority column.
- **New column with tree format**. Type boolean. Default 'false'.
- **Output file name**. Type STRING. Default it takes input file name and concatenates '_sorted' before extension.
