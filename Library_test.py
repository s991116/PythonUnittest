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

if __name__ == '__main__':
    unittest.main()