# Exercise demonstrating a CSV file parser that prints to the terminal the results of parsing 3 different types of csv files

The parser class is designed to handle a csv file that may specify its 'day' column as each day or a range of days.

        eg. mon, tue, wed, thu, fri, mon-tue, mon-thu, etc


## Execute the script

Designed to run with Python 3.5 using standard Python libraries.
```
eg.
python3 ./main.py -d ./sample_data


python3 ./main.py -h
usage: main.py [-h] -d DIR

Parses data from CSV files

optional arguments:
  -h, --help  show this help message and exit
  -d DIR      specify path to csv file(s) directory

```

## Tests

Unit-tests can be run as:
```
python3 test_csv_parser.py
```
or
```
python3 -m unittest test_csv_parser.TestCsvParser
```
