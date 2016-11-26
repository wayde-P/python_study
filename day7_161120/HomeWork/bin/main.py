import sys
import os

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)

from core import Course_class
from core import School_class
from core import Student_class
from core import Teacher_class
from core import operate_DB

a = School_class.School("beijing")
print(a.show_school())
# a.create_course("python2",6,45444)
c = Course_class.Course()
print(c.show_course())
