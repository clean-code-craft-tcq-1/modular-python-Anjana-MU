from ReferenceManual import *
import ColorPair_test_data as td

if __name__ == '__main__':
  td.test_functionalities()
  print('Reference Manual')
  createReferenceManual = ReferenceManual.createReferenceManual()
  printReferenceManual(createReferenceManual())  
  print('Done :)')
