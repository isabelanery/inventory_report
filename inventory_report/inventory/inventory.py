import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def read_file(cls, path):
        if path.endswith('.csv'):
            return cls.read_csv(path)

        if path.endswith('.json'):
            return cls.read_json(path)

        if path.endswith('.xlm'):
            print('>>>>>>>>>>>XML', cls.read_xml(path))
            return cls.read_xml(path)

    @classmethod
    def import_data(cls, path, report_type):
        products_data = cls.read_file(path)

        if report_type == 'simples':
            return SimpleReport.generate(products_data)

        if report_type == 'completo':
            return CompleteReport.generate(products_data)

    @staticmethod
    def read_csv(path):
        with open(path) as file:
            return list(csv.DictReader(file))

    @staticmethod
    def read_json(path):
        with open(path) as file:
            return json.loads(file.read())

    @staticmethod
    def read_xml(path):
        with open(path) as file:
            return xmltodict.parse(file.read())["dataset"]["record"]
