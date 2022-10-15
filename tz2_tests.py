import unittest
import tz2_functions
import cProfile

class Test_tz2(unittest.TestCase):
    def test__min(self):
        self.assertEqual(tz2_functions._min(file1), 1)
    def test__max(self):
        self.assertEqual(tz2_functions._max(file1), 4)
    def test__sum(self):
        self.assertEqual(tz2_functions._sum(file1), 10)
    def test__mult(self):
        self.assertEqual(tz2_functions._mult(file1), 24)
    def test__speed(self):
        cProfile.run("tz2_functions._max(file2)")

if __name__ == "__main__":
    print('Введите имя файла для тестирования корректности функций : ')
    file1 = input()
    print('Введите имя файла для тестрования скорости работы программы : ')
    file2 = input()
    unittest.main()
