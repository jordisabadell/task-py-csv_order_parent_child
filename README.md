# Python task. Sort CSV file by the parent-child relationship column

Given a CSV file with parent-child relationship column, this task sort the rows. Optional it creates a new column with tree format.

## Format of input file

- Type of file CSV.
- By defalult separaded with tabulates (you can change it).
- First row reserved by header.
- Child and Parent columns are required. Priority and content columns are optional.

### Input file

| Child ID | Parent ID | Col X      | Col Y    | Col Z      | Priority   |
|----------|-----------|------------|----------|------------|------------|
| 1        | 3         | Lorem      | Ipsum    | dolor      | 0          |
| 2        | 3         | sit        | amet     | consetetur | 1          |
| 3        | 4         | sadipscing | elitr    | sed        | 0          |
| 4        | 0         | diam       | nonumy   | eirmod     | 0          |
| 5        | 1         | tempor     | invidunt | ut         | 0          |

### Output file

| Child ID | Parent ID | Col X      | Col Y    | Col Z      | Priority   | New col       |
|----------|-----------|------------|----------|------------|------------|---------------|
| 4        | 0         | diam       | nonumy   | eirmod     | 0          | diam          |
| 3        | 4         | sadipscing | elitr    | sed        | 0          | -- sadipscing |
| 2        | 3         | sit        | amet     | consetetur | 1          | ---- sit      |
| 1        | 3         | Lorem      | Ipsum    | dolor      | 0          | ---- Lorem    |
| 5        | 1         | tempor     | invidunt | ut         | 0          | ------ tempor |

## Arguments

### Required

- **Input file name**. Especify path if it's not current. Type STRING.
- **Child column name**. Type STRING.
- **Parent column name**. Type STRNG.

### Optional

- **Parent root ID**. Type STRING. Default 0.
- **Priority column name**. Type STRING. Default 'empty' equals not sorted by priority column.
- **New column with tree format**. Type boolean. Default 'false'.
- **Output file name**. Type STRING. Default it takes input file name and concatenates '_sorted' before extension.
