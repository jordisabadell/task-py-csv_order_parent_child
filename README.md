# Order CSV file by parent-child relationship

Given a CSV file (delimited by tabulates) with parent-child relationship column, this task sort the rows. Optionaly it creates a new column with the depth tree.

I use it, for example, to sort Liferay Layout table content (version CE 6.1).

```sql
select groupId, name from lportal.Group_ where name like '%{__site name__}%';  
select plid, layoutId, parentLayoutId, name, hidden_, friendlyURL, priority from lportal.Layout where groupId={__group_id__};
```

## Arguments

| Parameter         | Type    | Description                     | Required | Default value     |
|-------------------|---------|---------------------------------|----------|-------------------|
| --help (or -h)    |         | Show help message and exit      | False    |                   |
| --inputfile       | String  | Input file name.                | True     |                   |
| --outputfile      | String  | Output file name.               | False    |                   |
| --childcol        | Integer | Child column number.            | False    | 0 (first column)  |
| --parentcol       | Integer | Parent column number.           | False    | 1 (second column) |
| --prioritycol     | Integer | Priority column number.         | False    |                   |
| --parentrootid    | Integer | Parent root ID.                 | False    | 0                 |
| --ignoreheaderrow |         | Ignore first row (header).      | False    |                   |
| --adddepthcol     |         | Add new column with tree depth. | False    |                   |

## Example

### Call

> py main.py --inputfile example/pages.csv --childcol 1 --parentcol 2 --prioritycol 4 --ignoreheaderrow --adddepthcol

### Input file example

| plid    | layoutId | parentLayoutId | name  | priority |
|---------|----------|----------------|-------|----------|
| 7004446 | 74       | 1              | Lorem | 15       |
| 8152170 | 205      | 1              | Ipsum | 10       |
| 6724205 | 1        | 0              | Amet  | 0        |
| 8152195 | 206      | 205            | Dolor | 0        |
| 8220383 | 222      | 205            | Sit   | 1        |

### Output file

| plid    | layoutId | parentLayoutId | name  | priority | __ auto_generated_depth_col __ |
|---------|----------|----------------|-------|----------|--------------------------------|
| 6724205 | 1        | 0              | Amet  | 0        | 0                              |
| 8152170 | 205      | 1              | Ipsum | 10       | 1                              |
| 8152195 | 206      | 205            | Dolor | 0        | 2                              |
| 8220383 | 222      | 205            | Sit   | 1        | 2                              |
| 7004446 | 74       | 1              | Lorem | 15       | 1                              |

## Next steps

- Add possibility to indicate CSV delimiter by call parameter.
