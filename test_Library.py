import unittest
from Library import library

class Test_Library(unittest.TestCase):

  def test_add_2_plus_3_returns_5(self):
    #Arrange
    lib = library()

    #Act
    result = lib.add(2,3)

    #Assert
    self.assertEqual(result, 5)

  def test_3_in_array_1_to_5(self):
    #Arrange
    testArray = [1,2,3,4,5]

    #Act

    #Assert
    self.assertIn(3, testArray)


if __name__ == '__main__':
    unittest.main()