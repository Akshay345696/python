class Principal:
    def role(self):
        print("i am managing all activity of college")

class Dean:
    def role(self):
        print('Dean= L am decision taking person')

class Hod:
    def role(self):
        print('Hod= I have responsibility of Teachers and Students')

class Faculty:
    def role(self):
        print('Faculty= I have to complete syllabus successfully')

def fun(object):
    object.role()
campus=[Principal(),Dean(),Hod(),Faculty()]
for object in campus:
    fun(object)
