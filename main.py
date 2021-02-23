from ReferenceManual import createReferenceManual
from ReferenceManual import printReferenceManual
import ColorPair_test_data as td

MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

if __name__ == '__main__':
  td.test_functionalities()
  print('Reference Manual')
  printReferenceManual(createReferenceManual())  
  print('Done :)')
