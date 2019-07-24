
from django.test import TestCase, Client
from courses.models import *


class EmployeeTestCase(TestCase):
    def setUp(self):
        print("setUp actitity")
        Employee.objects.create(eno=100, ename='jack', esal=1000, eaddr="tokmok")
        Employee.objects.create(eno=200, ename='SAM', esal=2000, eaddr="sokuluk")

    def test_employee_info(self):
        print("testing employee information")
        qs = Employee.objects.all()
        self.assertEqual(qs.count(), 2)
        e1 = Employee.objects.get(ename="jack")
        e2 = Employee.objects.get(ename="SAM")
        self.assertEqual(e1.get_salary(), 1000)
        self.assertEqual(e2.get_salary(), 2000)

class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="English",
            imgpath="http://www.answersfrom.com/wp-content/uploads/2011/09/Not-talanted-but-curious.jpg"
        )


    def test_category_imgpath(self):
        english = Category.objects.get(name="English")
        self.assertEqual(english.imgpath, 'http://www.answersfrom.com/wp-content/uploads/2011/09/Not-talanted-but-curious.jpg')



