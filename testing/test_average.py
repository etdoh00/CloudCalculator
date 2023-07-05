import average_m
import unittest

class TestAverage(unittest.TestCase):
    module_1 = ('module_1')
    module_2 = ('module_2')
    module_3 = ('module_3')
    module_4 = ('module_4')
    module_5 = ('module_5')
    def test_average(self):
        module_1 = ('module_1')
        module_2 = ('module_2')
        module_3 = ('module_3')
        module_4 = ('module_4')
        module_5 = ('module_5')
        module_marks = {module_1:10, module_2:20,
         module_3:30, module_4:40,
        module_5:50}
        result = average_m.average(module_marks)
        self.assertEqual(result,30)

if __name__ == "__main__":
    unittest.main()