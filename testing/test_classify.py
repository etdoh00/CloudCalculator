import Classify_grade
import unittest

class TestClassify(unittest.TestCase):
    module_1 = ('module_1')
    module_2 = ('module_2')
    module_3 = ('module_3')
    module_4 = ('module_4')
    module_5 = ('module_5')
    def test_classify(self):
        module_1 = ('module_1')
        module_2 = ('module_2')
        module_3 = ('module_3')
        module_4 = ('module_4')
        module_5 = ('module_5')
        module_marks = {module_1:10, module_2:20,
         module_3:30, module_4:40,
        module_5:50}
        result = Classify_grade.classifyGrade(module_marks)
        self.assertEqual(result,"No classification awarded, mark too low")

if __name__ == "__main__":
    unittest.main()