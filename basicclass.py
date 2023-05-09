class Student():
    def __init__(self,name):
        self.name = name
        self.hello()

    def hello(self):
        print('สวัสดีจ้าาาผมชื่อ{}ครับ'.format(self.name))

    def study(self,subject):
        print('{}กำลังเรียนวิชา{}'.format(self.name,subject))

    def playgame(self):
        print('กำลังเล่นเกม')

class SuperStudent(Student):
    def __init__(self,name):
        super().__init__(name)

    def coding(self,project):
        print('ผมกำลังเขียนโปรเจค{}'.format(project))

    def showmyproject(self,project):
        print('ผมเป็น super student ชื่อ{}'.format(self.name))
        self.coding(project)
        print('โปรเจคเสร็จแล้ว!')

somchai = Student('สมชาย')
somchai.study('คณิตศาสตร์')
print('--------------------')
john = SuperStudent('จอห์น')
john.showmyproject('เกมงู')
