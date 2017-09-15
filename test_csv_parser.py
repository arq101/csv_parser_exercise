#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from csv_parser import CsvParser
import custom_exceptions as ex


class TestCsvParser(unittest.TestCase):

    def test_check_file_exists(self):
        parser = CsvParser('./test_data/separate_days.csv')
        self.assertTrue(parser.check_file_exists())

    def test_file_not_exists(self):
        parser = CsvParser('./test_data/foobar.csv')
        with self.assertRaises(ex.FileCannotBeFound):
            parser.check_file_exists()

    def test_parse_csv_for_single_day_data(self):
        """
        Given a csv file that contains data for each day,
        compile and parse its data fields.
        """
        parser = CsvParser('./test_data/separate_days.csv')
        output = parser.parse_csv_file()
        self.assertEqual(output[0]['day'], 'mon')
        self.assertEqual(output[0]['value'], '7')
        self.assertEqual(output[0]['description'], 'hydrogen 7')
        self.assertEqual(output[0]['square'], 49)

    def test_parse_csv_day_range_data_mon_to_thu(self):
        """
        The data for mon to thu is collective, while fri is separate.
        """
        parser = CsvParser('./test_data/day_range_mon_to_thu.csv')
        output = parser.parse_csv_file()
        self.assertEqual(output[0]['value'], '8')
        self.assertEqual(output[1]['value'], '8')
        self.assertEqual(output[2]['value'], '8')
        self.assertEqual(output[3]['value'], '8')
        self.assertEqual(output[4]['value'], '3')

    def test_parse_csv_day_range_mon_to_tue_and_wed_to_thu(self):
        """
        The data for mon to tue is collective, so is wed to thu,
        while fri is separate.
        """
        parser = CsvParser('./test_data/day_range_mon_to_tue_and_wed_to_thu.csv')
        output = parser.parse_csv_file()
        self.assertEqual(output[0]['value'], '5')
        self.assertEqual(output[1]['value'], '5')
        self.assertEqual(output[2]['value'], '7')
        self.assertEqual(output[3]['value'], '7')
        self.assertEqual(output[4]['value'], '11')

    def test_unexpected_day_range(self):
        """
        When an unexpected day range has been specified in a csv file,
        then we have nothing to process.
        """
        parser = CsvParser('./test_data/unexpected_day_range.csv')
        output = parser.parse_csv_file()
        self.assertEqual(output, None)


if __name__ == '__main__':
    unittest.main(verbosity=2)
