from ReferenceManual import createReferenceManual
from ReferenceManual import printReferenceManual
import ColorPair_test_data as td

if __name__ == '__main__':
  td.test_functionalities()
  print('Reference Manual')
  printReferenceManual(createReferenceManual())  
  print('Done :)')
