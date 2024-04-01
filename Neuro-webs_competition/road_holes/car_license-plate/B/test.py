import unittest
class Testing(unittest.TestCase):
    def setUp(self):
        self.a = '10'
    def test1(self):
        print(self.a)
    def test2(self):
        print(self.a+'dsadsa')
    def test3(self):
        print(self.a +10)
if __name__ == '__main__':
    unittest.main()