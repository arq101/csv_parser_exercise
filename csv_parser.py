# -*- coding: utf-8 -*-

import csv
import os
from collections import OrderedDict

import exceptions as ex


class CsvParser(object):
    """
    Parses data from different CSV files, where each file may have data for each day,
    or a range of days.

        eg. mon, tue, wed, thu, fri, mon-tue, mon-thu, etc

    """

    def __init__(self, filename):
        self.file_name = filename

    def check_file_exists(self):
        if os.path.isfile(self.file_name):
            return True
        else:
            raise ex.FileNotFound("File '{}' not found!".format(self.file_name))

    def parse_csv_file(self):
        """
        Given a csv file, this method parses the data for each day by checking the format
        of the day columns.
        """
        self.check_file_exists()
        parsed_data = None
        with open(self.file_name) as csv_fh:
            reader = csv.DictReader(csv_fh)
            for row in reader:

                # check if csv file contains data for each separate working week day
                if len([day for day in ('mon', 'tue', 'wed', 'thu', 'fri') if day in row.keys()]) == 5:
                    parsed_data = self._single_day_data(row)
                elif 'mon-thu' in row.keys() and 'fri' in row.keys():
                    parsed_data = self._day_range_data_mon_to_thu(row)
                elif 'mon-tue' in row.keys() and 'wed-thu' in row.keys() and 'fri' in row.keys():
                    parsed_data = self._day_range_data_mon_to_tue_and_wed_to_thu(row)
                else:
                    print('Error: unknown day range specified in csv file!')

        return parsed_data

    def _single_day_data(self, row):
        """
        The row of data from the csv file contains data for each day: mon to fri.
        Therefore retrieve data for each day.
        """
        results = list()
        results.append(self._process_mon_tues_wed('mon', row['description'], row['mon']))
        results.append(self._process_mon_tues_wed('tue', row['description'], row['tue']))
        results.append(self._process_mon_tues_wed('wed', row['description'], row['wed']))
        results.append(self._process_thu_fri('thu', row['description'], row['thu']))
        results.append(self._process_thu_fri('fri', row['description'], row['fri']))
        return results

    def _day_range_data_mon_to_thu(self, row):
        """
        The row of data from the csv file contains collective data for mon to thu,
        and fri is separate.
        """
        results = list()
        results.append(self._process_mon_tues_wed('mon', row['description'], row['mon-thu']))
        results.append(self._process_mon_tues_wed('tue', row['description'], row['mon-thu']))
        results.append(self._process_mon_tues_wed('wed', row['description'], row['mon-thu']))
        results.append(self._process_thu_fri('thu', row['description'], row['mon-thu']))
        results.append(self._process_thu_fri('fri', row['description'], row['fri']))
        return results

    def _day_range_data_mon_to_tue_and_wed_to_thu(self, row):
        """
        The row of data from the csv file contains collective data for mon to tue,
        and wed to thu, and fri separate.
        """
        results = list()
        results.append(self._process_mon_tues_wed('mon', row['description'], row['mon-tue']))
        results.append(self._process_mon_tues_wed('tue', row['description'], row['mon-tue']))
        results.append(self._process_mon_tues_wed('wed', row['description'], row['wed-thu']))
        results.append(self._process_thu_fri('thu', row['description'], row['wed-thu']))
        results.append(self._process_thu_fri('fri', row['description'], row['fri']))
        return results


    def _process_mon_tues_wed(self, day, description, value):
        """
        For days; mon, tue & wed, process data fields for value and description.
        In addition, add a field that squares the value.
        """
        return OrderedDict(
            [
                ('day', day),
                ('description', description + ' %s' % value),
                ('square', int(value) ** 2),
                ('value', value)
            ]
        )

    def _process_thu_fri(self, day, description, value):
        """
        For days; thu & fri, process data fields for value and description.
        In addition, add a field that doubles the value.
        """

        return OrderedDict(
            [
                ('day', day),
                ('description', description + ' %s' % value),
                ('double', int(value) * 2),
                ('value', value)
            ]
        )
