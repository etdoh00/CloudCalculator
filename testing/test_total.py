import unittest
import total_mark

class TestTotal(unittest.TestCase):
    module_1 = ('module_1')
    module_2 = ('module_2')
    module_3 = ('module_3')
    module_4 = ('module_4')
    module_5 = ('module_5')
    def test_total(self):
        module_1 = ('module_1')
        module_2 = ('module_2')
        module_3 = ('module_3')
        module_4 = ('module_4')
        module_5 = ('module_5')
        module_marks = {module_1:100, module_2:100,
         module_3:100, module_4:100,
        module_5:100}
        result = total_mark.t_marks(module_marks)
        self.assertEqual(result,500)

if __name__ == "__main__":
    unittest.main()

