CSV
===
See <https://docs.python.org/3/library/csv.html>


`my_data.csv`:

first_name | last_name | position
-----------|-----------|---------
Theodore   | Crisp     | Senior Vice-President Research and Development
Linda      | Zwordling | testing
Philip     | Myman     | scientist
Lem        | Hewitt    | scientist



`reader` and `writer` objects read and write streams, `DictReader` and `DictWriter` classes work with dictionaries.

`read_csv_list.py`:

```Python
import csv

# note, it is important that we override the default newline argument so that newlines embedded within quoted fields are handled
# correctly: <https://docs.python.org/3/library/csv.html#id3>
with open('my_data.csv', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',') # ',' is the default for delimited, included only for illustration
    rows = list(csv_reader) # convert the csv_reader object into a list of rows
    for row in rows:
        print(row)
```

`write_csv_list.py`:

`read_csv_dict.py`:

```Python
import csv

with open('my_data.csv', newline-'') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    rows = list(csv_reader)
    for row in rows:
        print(row['first_name'])
```

`write_csv_dict.py`:

```Python
import csv

with open('my_data.csv', 'a') as csv_file:
    fieldnames = ['name',
                  'class']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    csv_writer.writeheader()
    csv_writer.writerow({
        'name': 'Jekyll',
        'classs': 'Assassin',
    })
```


`my_data.json`:
