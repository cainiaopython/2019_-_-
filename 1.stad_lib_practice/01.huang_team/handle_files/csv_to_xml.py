from xml.etree.ElementTree import Element,ElementTree
from module.file import File
import csv
import os


class CvsToXml:
    def __init__(self, out_path='output', csv_file_name='movie.csv'):
        '''
        Handle change the csv file to xml file
        :param out_path: output file dir
        :param csv_file_name: csv file
        '''
        self.out_path = out_path
        self.path = os.path.join(File.get_dir_path(), out_path)
        self.file = '{}/{}'.format(self.path, csv_file_name)


    def csv_to_xml(self, out_xml_file='movie.xml'):
        '''
        read the csv file content and convert it to xml file
        :param out_xml_file: 
        :return: 
        '''
        if not File.verify_file(self.file):
            print ('Read failed,file {} not exist!'.format(self.file))
        else:
            with open(self.file,'rt') as rf:
                reader=csv.reader(rf)
                if self.write_xml(reader, out_xml_file):
                    print ('csv {} to xml {} ok!'.format(self.file, out_xml_file))

                else:
                    print ('csv {} to xml {} failed!'.format(self.file, out_xml_file))

    def write_xml(self,csv_reader,out_file):
        '''
        write the data to xml file
        :param csv_reader: file handler
        :param out_file: out file
        :return: 
        '''

        try:
            # reader header
            headers = csv_reader.__next__()

            root = Element('Data')
            for index, row in enumerate(csv_reader):
                if index == 0:
                    continue

                eRow = Element('Row')
                root.append(eRow)
                for tag, text in zip(headers, row):
                    e = Element(tag)
                    e.text = text
                    eRow.append(e)

            et=ElementTree(root)
            out_xml_file='{}/{}'.format(self.path, out_file)
            et.write(out_xml_file)
            return True
        except Exception as e:
            print (e)
            return False


if __name__=='__main__':
    csvToXml=CvsToXml(csv_file_name='movie.csv')
    csvToXml.csv_to_xml(out_xml_file='movie.xml')

