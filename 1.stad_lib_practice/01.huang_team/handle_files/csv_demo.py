from xml.etree.ElementTree import Element,ElementTree
from xml.etree.ElementTree import tostring
from pprint import pprint
import csv


'''
<Data>
    <Student>
        <Age> 18 </Age>
        <Sex> man </Sex>
    </Student>
</Data>

'''

def demo():
    #创建父element
    e=Element('Data')

    #创建子element
    e2=Element('Student')

    #创建孙子element
    e3=Element('Age')
    e3.text='18'

    #创建孙子element
    e4=Element('Sex')
    e4.text='man'

    #链接父-子-孙
    e2.append(e3)
    e2.append(e4)
    e.append(e2)

    pprint(tostring(e))

    #创建根节点,输出xml
    et=ElementTree(e)
    et.write('demo.xml')

if __name__=='__main__':
    demo()