from module.file import File
from pprint import pprint
import csv
import os

class HandleCSV():
    def __init__(self,out_path='output',file_name='movie.csv'):
        path=os.path.join(File.get_dir_path(),out_path)
        self.file='{}/{}'.format(path,file_name)

    def write_csv(self,data):
        try:
            with open(self.file,'w',encoding='utf-8') as csvfile:
                csv_writer=csv.writer(csvfile)

                if len(data)<1:
                    print ('data error!')
                    return

                if len(data)==1 and isinstance(data,dict):
                    header=data.keys()
                else:
                    header=data[0].keys()

                csv_writer.writerow(header)

                for item in data:
                    row=item.values()
                    csv_writer.writerow(row)

        except Exception as e:
            print ('Write CSV file failed.Error:{}'.format(e))
            return None

    def wirte_csv_dict(self,rows):
        try:
            with open(self.file,'w',encoding='utf-8') as csvfile:
                if len(rows)<1:
                    return

                header=rows[0].keys() if len(rows)>1 else rows.keys()
                csv_write_dict = csv.DictWriter(csvfile, fieldnames=header)

                if len(rows)==1:
                    csv_write_dict.writerow(rows)
                elif len(rows)>1:
                    csv_write_dict.writerows(rows)

        except Exception as e:
            print('Write CSV file failed.Error:{}'.format(e))
            return None

    def read_csv(self):
        if not File.verify_file(self.file):
            print ('Read failed,file {} not exist!'.format(self.file))

        rows=[]
        try:
            with open(self.file,'r', encoding='utf-8') as csvfile:
                csv_reader=csv.reader(csvfile)
                for index,row in enumerate(csv_reader):
                    if index==0:
                        continue
                    rows.append(row)
                print ('Read CSV file :{} ok!'.format(self.file))
                return rows

        except Exception as e:
            print('Read CSV file failed.Error:{}'.format(e))
            return None


if __name__=='__main__':
    handleCSV=HandleCSV()
    data=handleCSV.read_csv()
    pprint(data)

