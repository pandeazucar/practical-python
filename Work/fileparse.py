# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=True):
    """
    Pase a CSV file into a list of records
    """

    with open(filename, 'rt') as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file header
        headers = next(rows) if has_headers else []

        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for rowno, row in enumerate(rows, start=1):
            if not row:  # Skip rows with no data
                continue

            # Filter the row if specific columns were selected
            if indices:
                row = [row[index] for index in indices]

            # Optional type conversion for the returned data
            if types:
                # Watch out for ValueErrors and exceptions in general
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    # Make sure the user can set whether errors are printed
                    # to the screen or not
                    if not silence_errors:
                        print(f"Row {rowno} Couldn't convert {row}")
                        print(f"Row {rowno} Reason {e}")
                    else:
                        continue

            # Make a dictionary if there are headers
            # else just return tuples
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)

            records.append(record)

    return records
