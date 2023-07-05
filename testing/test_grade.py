import unittest
import grade_Calc


class TestGrade(unittest.TestCase):
    module_1 = ('module_1')
    module_2 = ('module_2')
    module_3 = ('module_3')
    module_4 = ('module_4')
    module_5 = ('module_5')
    def test_grade(self):
        module_1 = ('module_1')
        module_2 = ('module_2')
        module_3 = ('module_3')
        module_4 = ('module_4')
        module_5 = ('module_5')
        module_marks = {module_1:100, module_2:100,
         module_3:100, module_4:100,
        module_5:100}
        result = grade_Calc.calcGrade(module_marks)
        self.assertEqual(result,"module1 : First")

if __name__ == "__main__":
    unittest.main()