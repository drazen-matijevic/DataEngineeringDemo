import unittest
import pandas as pd
from unittest import TestCase
from UnitTestPipeline import load_data, clean_data


class TestDataPipeline(TestCase):

    # Sink path
    output_path = 'c:\\demo\\landing_zone\\'

    # Setup test environment 
    def setUp(self):
        self.file_path  =   'c:\\demo\\landing_zone\\actor.csv'
        self.test_df    =   load_data(self.file_path)

    # Validate the row count
    def test_row_count(self):        
        expected_row_count  =   200
        actual_row_count    =   len(self.test_df)
        self.assertEqual(actual_row_count, expected_row_count, f"The actual row count {actual_row_count} does not match with the expected row count {expected_row_count}")

    # Validate data
    def test_clean_data(self):
        #test_df = pd.DataFrame({"first_name": ['PENELOPE', 'NICK', 'ED', None]})
        clean_df = clean_data(self.test_df)
        self.assertFalse(clean_df.isnull().values.any(), "Data has null values")
    
    # Validate for Null values
    def test_null_values_in_data(self):
        expected_null_count     =   4 
        actual_null_count       =   self.test_df.isnull().sum().sum()
        self.assertEqual(actual_null_count, expected_null_count, f"Data contains {actual_null_count} NULL values instead of {expected_null_count} NULL values")


if __name__=="__main__":
    unittest.main()