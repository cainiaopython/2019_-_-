from pprint import pprint
from module.file import File
import json
import os


class HandleJson():
    def __init__(self,out_path='output'):
        path=os.path.join(File.get_dir_path(),out_path)
        self.file='{}/movie.json'.format(path)

    def write_json(self,data):
        """
        write the data as json file
        :param data: list data
        """
        try:
            with open(self.file,'w') as wf:
                json.dump(data,wf)
                print ('Save Json file :{} ok!'.format(self.file))
        except Exception as e:
            print ('Wirte json file failed .{}'.format(e))
            return None

    def read_json(self):
        if not File.verify_file(self.file):
            print ('Read failed,file {} not exist!'.format(self.file))
        try:
            with open(self.file,'rt') as rf:
                return json.load(rf)

        except Exception as e:
            print ('Read json failed,error:{}'.format(e))


if __name__=='__main__':
    handleJson=HandleJson()
    r=handleJson.read_json()
    pprint(r)
