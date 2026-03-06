class StudentRecords:

    total_students = 0
    college_name = "Islamia College"

    def __init__(self, roll_no, first_name, last_name, course):
        self.roll_no = roll_no
        self.first_name = first_name
        self.last_name = last_name
        self.course = course

        type(self).total_students += 1

    def fullname(self):
        return "{} {}".format(self.first_name, self.last_name)

    @classmethod
    def change_college_name(cls, new_college_name):
        cls.college_name = new_college_name

    @staticmethod
    def is_valid_roll(roll_no):
        if not isinstance(roll_no, int):
            return False
        if roll_no <= 0:
            return False
        return True

    @classmethod
    def from_string(cls, data_string):
        roll_no, first_name, last_name, course = data_string.split(",")
        roll_no = int(roll_no)

        if not cls.is_valid_roll(roll_no):
            raise ValueError("Invalid roll number")

        return cls(roll_no, first_name, last_name, course)

# For FULL STAFF -->
class CollegeStaff:

    def __init__(self, name, staff_id, deptt):
        self.name = name
        self.staff_id = staff_id
        self.deptt = deptt

    def show_details(self):
        print(self.name, self.staff_id, self.deptt)
    
# For TEACHING STAFF -->
class TeachingStaff(CollegeStaff):

    def __init__(self, name, staff_id, deptt, subject, research_area):
        super().__init__(name, staff_id, deptt)
        self.subject = subject
        self.research_area = research_area

    def take_class(self):
        print(f"{self.name} is teaching {self.subject}")
    
# For NON-TEACHINIG STAFF -->
class NonTeachingStaff(CollegeStaff):
    def __init__(self, name, staff_id, deptt, role, shift):
        super().__init__(name, staff_id, deptt)
        self.role = role
        self.shift = shift

    def perform_duty(self):
        print(f"{self.name} ({self.role}) is managing {self.deptt} in {self.shift} shift.")
    
t1 = TeachingStaff("Afeef", 101, "IT", "Python", "AI")
t2 = NonTeachingStaff("Karim", 102, "Canteen", "Cook", "Evening")

# t1.show_details()
# t1.take_class()
# t2.show_details()
# t2.perform_duty()