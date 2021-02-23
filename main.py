from ReferenceManual import createReferenceManual
from ReferenceManual import printReferenceManual
from ColorPair_test_data import td

if __name__ == '__main__':
  td.test_number_to_pair(4, 'White', 'Brown')
  td.test_number_to_pair(5, 'White', 'Slate')
  td.test_pair_to_number('Black', 'Orange', 12)
  td.test_pair_to_number('Violet', 'Slate', 25)
  td.test_pair_to_number('Red', 'Orange', 7)
  print('Reference Manual')
  printReferenceManual(createReferenceManual())  
  print('Done :)')
