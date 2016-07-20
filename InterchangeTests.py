import unittest
from data_interchange.interchange import FileWrapper, TextBroker


class TestFileWrapperMethods(unittest.TestCase):

    def setUp(self):
        self.fw = FileWrapper()
        self.contacts = [
            {"first_name": "John", "last_name": "Doe", "phone": "999-867-5309"},
            {"first_name": "Jane", "last_name": "Doe", "phone": "999-867-5309"},
            {"first_name": "Jamie", "last_name": "Doe", "phone": "999-867-5309"}
        ]
        self.test_string1 = "The quick brown fox jumps over the lazy dog"
        self.test_string2 = "Sphinx of black quartz, judge my vow"
        self.test_string3 = "Pack my box with five dozen liquor jugs"
        self.test_string4 = "first_name,last_name,role\nJohn,Doe,Cat\nJane,Doe,Cat"
        self.string_list = [self.test_string1, self.test_string2, self.test_string3]
        self.list_test = ['first_name,last_name,role\n', 'John,Doe,Cat\n', 'Jane,Doe,Cat']
        self.csv_sample = "sample.csv"
        self.json_sample = "sample.json"
        self.xml_sample = "sample.xml"
        self.yaml_sample = "sample.yaml"
        self.test_export_file = "test.txt"

    def test_plaintext_to_string(self):
        # arrange
        test_fixture = self.test_string4
        # act
        string_from_text = self.fw.plaintext_to_string(self.csv_sample)
        # assert
        self.assertEqual(string_from_text, test_fixture)

    def test_string_to_plaintext(self):
        # arrange
        test_fixture = self.test_string4
        # act
        filename = self.fw.string_to_plaintext(test_fixture, self.test_export_file)
        string_from_text = self.fw.plaintext_to_string(filename)
        # assert
        self.assertEqual(self.test_export_file, filename)
        self.assertEqual(string_from_text, test_fixture)

    def test_plaintext_to_string_list(self):
        # arrange
        test_fixture = self.list_test
        # act
        string_list = self.fw.plaintext_to_string_list(self.csv_sample)
        # assert
        self.assertEqual(string_list, test_fixture)

    def test_string_list_to_plaintext(self):
        # arrange
        test_fixture = self.test_string4
        # act
        filename = self.fw.string_list_to_plaintext(self.list_test, self.test_export_file)
        string_from_text = self.fw.plaintext_to_string(filename)
        # assert
        self.assertEqual(self.test_export_file, filename)
        self.assertEqual(string_from_text, test_fixture)

    def test_update_date_stamp(self):
        # arrange
        test_fixture = self.fw.date_stamp
        # act
        new_date_stamp = self.fw.update_date_stamp()
        # assert
        self.assertNotEqual(new_date_stamp, test_fixture)


class TestTextBrokerMethods(unittest.TestCase):

    def setUp(self):
        self.tb = TextBroker()
        self.csv_sample = "sample.csv"
        self.json_sample = "sample.json"
        self.json_sample_dict = {'gender': {'type': 'male'},
                                 'firstName': 'John',
                                 'address': {'city': 'New York', 'streetAddress': '21 2nd Street', 'state': 'NY',
                                             'postalCode': '10021'},
                                 'lastName': 'Smith',
                                 'age': 25,
                                 'phoneNumber': [{'number': '212 555-1234', 'type': 'home'},
                                                 {'number': '646 555-4567', 'type': 'fax'}]
                                 }
        self.xml_sample = "sample.xml"
        self.xml_sample_dict = {'person':
                                    {'age': '25',
                                     'lastName': 'Smith',
                                     'address': {'city': 'New York', 'state': 'NY', 'streetAddress': '21 2nd Street', 'postalCode': '10021'},
                                     'gender': {'type': 'male'},
                                     'firstName': 'John',
                                     'phoneNumbers': {'phoneNumber': [{'type': 'home', 'number': '212 555-1234'}, {'type': 'fax', 'number': '646 555-4567'}]}
                                     }
                                }
        self.yaml_sample = "sample.yaml"
        self.yaml_sample_dict = {'firstName': 'John',
                                 'address': {'streetAddress': '21 2nd Street', 'postalCode': 10021, 'state': 'NY', 'city': 'New York'},
                                 'lastName': 'Smith',
                                 'age': 25,
                                 'gender': {'type': 'male'},
                                 'phoneNumber': [{'type': 'home', 'number': '212 555-1234'}, {'type': 'fax', 'number': '646 555-4567'}]}
        self.test_export_file = "test.txt"
        self.contacts = [
            {"first_name": "John", "last_name": "Doe", "phone": "999-867-5309"},
            {"first_name": "Jane", "last_name": "Doe", "phone": "999-867-5309"},
            {"first_name": "Jamie", "last_name": "Doe", "phone": "999-867-5309"}
        ]
        self.names_list = [
            {'role': 'Cat', 'first_name': 'John', 'last_name': 'Doe'},
            {'role': 'Cat', 'first_name': 'Jane', 'last_name': 'Doe'},
        ]
        self.test_string4 = "first_name,last_name,role\nJohn,Doe,Cat\nJane,Doe,Cat\n"
        self.col_names = ["first_name", "last_name", "role"]

    def test_csv_to_dictionary(self):
        # arrange
        test_fixture = self.names_list
        # act
        list_of_dictionaries = self.tb.csv_to_dictionary(self.csv_sample)
        # assert
        self.assertEqual(list_of_dictionaries, test_fixture)

    def test_dictionary_to_csv(self):
        # arrange
        test_fixture = self.test_string4
        # act
        row_count = self.tb.dictionary_to_csv(self.names_list, self.test_export_file, self.col_names)
        string_from_text = self.tb.plaintext_to_string(self.test_export_file)

        # assert
        self.assertEqual(len(self.names_list), row_count)
        self.assertEqual(string_from_text, test_fixture)

    def test_json_to_dictionary(self):
        # arrange
        test_fixture = self.json_sample_dict
        # act
        dictionary = self.tb.json_to_dictionary(self.json_sample)
        # assert
        self.assertEqual(dictionary, test_fixture)

    def test_dictionary_to_json(self):
        # arrange
        test_fixture = self.json_sample_dict
        json_file = self.json_sample
        # act
        self.tb.dictionary_to_json(test_fixture, json_file)
        dictionary = self.tb.json_to_dictionary(json_file)
        # assert
        self.assertEqual(dictionary, test_fixture)

    def test_yaml_to_dictionary(self):
        # arrange
        test_fixture = self.yaml_sample_dict
        # act
        dictionary = self.tb.yaml_to_dictionary(self.yaml_sample)
        # assert
        self.assertEqual(dictionary, test_fixture)

    def test_dictionary_to_yaml(self):
        # arrange
        test_fixture = self.yaml_sample_dict
        yaml_file = self.yaml_sample
        # act
        self.tb.dictionary_to_yaml(test_fixture, yaml_file)
        dictionary = self.tb.yaml_to_dictionary(yaml_file)
        # assert
        self.assertEqual(dictionary, test_fixture)

    def test_xml_to_dictionary(self):
        # arrange
        test_fixture = self.xml_sample_dict
        # act
        dictionary = self.tb.xml_to_dictionary(self.xml_sample)
        # assert
        self.assertEqual(dictionary, test_fixture)

    def test_dictionary_to_xml(self):
        # arrange
        test_fixture = self.xml_sample_dict
        xml_file = self.xml_sample
        # act
        self.tb.dictionary_to_xml(test_fixture, filename=xml_file, write_to_file=True)
        dictionary = self.tb.xml_to_dictionary(xml_file)
        # assert
        self.assertEqual(dictionary, test_fixture)

file_wrapper_test_suite = unittest.TestLoader().loadTestsFromTestCase(TestFileWrapperMethods)
unittest.TextTestRunner(verbosity=2).run(file_wrapper_test_suite)

text_broker_test_suite = unittest.TestLoader().loadTestsFromTestCase(TestTextBrokerMethods)
unittest.TextTestRunner(verbosity=2).run(text_broker_test_suite)
