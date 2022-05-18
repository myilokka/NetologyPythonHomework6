class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        all_students.append(self)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and 1<= grade <= 10 and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def mean_grade(self):
        local_sum = 0
        global_sum = 0
        k = 0
        for value in self.grades.values():
            for i in value:
                local_sum += i
            global_sum += local_sum
            local_sum = 0
            k += len(value)+1
        res = global_sum/k
        return round(res, 2)

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\n'
               f'Средняя оценка за домашние задания: {self.mean_grade()}\n'
               f'Курсы в процессе изучения: {self.courses_in_progress }\n'
               f'Завершенные курсы: {self.finished_courses}')
        return res

    def __le__(self, other):
        if isinstance(other, Student):
            if self.mean_grade() < other.mean_grade():
                print(f'У ученика {other.name} {other.surname} рейтинг выше, чем у ученика {self.name} {self.surname}')
                res = self.mean_grade() <= other.mean_grade()
            elif self.mean_grade()==other.mean_grade():
                print(f'Рейтинг ученика {other.name} {other.surname} такой же, как у ученика {self.name} {self.surname}')
                res = self.mean_grade() <= other.mean_grade()
            else:
                print(f'У ученика {other.name} {other.surname} рейтинг ниже, чем у ученика {self.name} {self.surname}')
                res = self.mean_grade() < other.mean_grade()
        else:
            res = 'Ошибка!'
        return res

    def course_mean(self, course, all_roles):
        sum=0
        k=0
        for role in all_roles:
            if course in role.grades.keys():
                for i in range(len(role.grades[course])):
                    sum+=role.grades[course][i]
                    k+=1
        return round(sum/k, 2)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        all_lecturers.append(self)

    def mean_grade(self):
        return Student.mean_grade(self)

    def __le__(self, other):
        if isinstance(other, Lecturer):
            if self.mean_grade() < other.mean_grade():
                print(f'У лектора {other.name} {other.surname} рейтинг выше, чем у лектора {self.name} {self.surname}')
                res = self.mean_grade() <= other.mean_grade()
            elif self.mean_grade()==other.mean_grade():
                print(f'Рейтинг лектора {other.name} {other.surname} такой же, как у лектора {self.name} {self.surname}')
                res = self.mean_grade() <= other.mean_grade()
            else:
                print (f'У лектора {other.name} {other.surname} рейтинг ниже, чем у лектора {self.name} {self.surname}')
                res = self.mean_grade() < other.mean_grade()
        else:
            res = 'Ошибка!'
        return res

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\n'
               f'Средняя оценка за лекции: {self.mean_grade()}')
        return res

    def course_mean(self, course, all_roles):
        return Student.course_mean(self, course, all_roles)


class Reviewer(Mentor):
     def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

     def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}')
        return res


all_students = []
all_lecturers=[]


student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python', 'Jango']
student2 = Student('Ruoy', 'Manan', 'your_gender')
student2.courses_in_progress += ['Python']

lecturer1 = Lecturer('Some', 'Buddy')
lecturer1.courses_attached += ['Python']
lecturer2 = Lecturer('One', 'Buddy')
lecturer2.courses_attached += ['Python', 'Jango']

cool_reviewer2 = Reviewer("Another", "Buddy")
cool_reviewer2.courses_attached += ['Python','Jango']
cool_reviewer1 = Reviewer("Second", "Buddy")
cool_reviewer1.courses_attached += ['Python','Jango']

student1.rate_lecturer(lecturer1, 'Python', 5)
student2.rate_lecturer(lecturer1, 'Python', 8)
student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer2, 'Jango', 5)
student1.rate_lecturer(lecturer2, 'Jango', 8)
student2.rate_lecturer(lecturer2, 'Python', 10)

cool_reviewer1.rate_hw(student1, 'Python', 10)
cool_reviewer2.rate_hw(student1, 'Python', 5)
cool_reviewer2.rate_hw(student2, 'Python', 9)
cool_reviewer1.rate_hw(student1, 'Jango', 4)
cool_reviewer2.rate_hw(student1, 'Jango', 7)
cool_reviewer2.rate_hw(student2, 'Python', 10)

print(cool_reviewer1)
print(cool_reviewer2)
print(lecturer1)
print(lecturer2)
print(student1)
print(student2)


print(student1 <= student2)
print(lecturer1 <= lecturer2)

print(student2.course_mean('Jango', all_students))
print(lecturer2.course_mean('Jango', all_lecturers))
