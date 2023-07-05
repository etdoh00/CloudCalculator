import total_mark
import grade_Calc
import average_m
import unittest
import Classify_grade

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

