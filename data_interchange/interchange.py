import datetime
import csv
import json
import xmltodict
import yaml
# import h5py
# import pickle

__author__ = 'jmategk0'
__version__ = '0.0.1'
__license__ = 'MIT'


class FileWrapper(object):

    def __init__(self):
        self.date_stamp = datetime.datetime.now()

    def plaintext_to_string_list(self, filename, read_mode='r'):

        with open(filename, read_mode) as text_file:
            text_data = text_file.readlines()
        return text_data

    def string_list_to_plaintext(self, string_list, filename, write_mode='w'):

        with open(filename, write_mode) as text_file:
            text_file.writelines(string_list)
        return filename

    def plaintext_to_string(self, filename, read_mode='r'):

        with open(filename, read_mode) as text_file:
            text_data = text_file.read()
        return text_data

    def string_to_plaintext(self, string_value, filename, write_mode='w'):

        with open(filename, write_mode) as text_file:
            text_file.write(string_value)
        return filename

    def update_date_stamp(self):
        
        self.date_stamp = datetime.datetime.now()
        return self.date_stamp


class TextBroker(FileWrapper):

    def csv_to_dictionary(self, filename, delimiter=",", read_mode='r'):

        csv_data = []
        with open(filename, read_mode) as csv_file:
            reader = csv.DictReader(csv_file, delimiter=delimiter)
            for row in reader:
                csv_data.append(row)
        return csv_data

    def dictionary_to_csv(self, list_of_dictionaries, filename, field_names, delimiter=",", write_mode='w'):

        with open(filename, write_mode) as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=field_names, delimiter=delimiter)
            writer.writeheader()
            for row in list_of_dictionaries:
                writer.writerow(row)
            return len(list_of_dictionaries)

    def json_to_dictionary(self, filename):

        with open(filename) as json_file:
            json_data = json.load(json_file)
        return json_data

    def dictionary_to_json(self, dictionary, write_to_file=False, filename=" ", write_mode='w'):
        if write_to_file:
            with open(filename, write_mode) as json_file:
                json_data = json.dump(dictionary, json_file, indent=4)
        else:
            json_data = json.dumps(dictionary, indent=4)
        return json_data

    def yaml_to_dictionary(self, filename, read_mode='r'):

        with open(filename, read_mode) as yaml_file:
            yaml_data = yaml.load(yaml_file)
        return yaml_data

    def dictionary_to_yaml(self, dictionary, write_to_file=False, filename=" ", write_mode='w'):

        if write_to_file:
            with open(filename, write_mode) as yaml_file:
                yaml_data = yaml.dump(dictionary, yaml_file)
        else:
            yaml_data = yaml.dump(dictionary)
        return yaml_data

    def xml_to_dictionary(self, filename, read_mode='r'):

        with open(filename, read_mode) as xml_file:
            xml_data = xmltodict.parse(xml_file.read(), dict_constructor=dict)
        return xml_data

    def dictionary_to_xml(self, dictionary, write_to_file=False, filename=" ", write_mode='w'):
        xml_data = xmltodict.unparse(dictionary, pretty=True)
        if write_to_file:
            with open(filename, write_mode) as xml_file:
                    xml_data = xml_file.write(xml_data)
        return xml_data


class BinaryBroker(FileWrapper):
    pass
    # support h5py and pickle later


class ComplexBroker(FileWrapper):
    pass
    # support xlsx and open doc later
