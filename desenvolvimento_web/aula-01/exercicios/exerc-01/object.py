class Lesson:
    def __init__(self, teacher, student, subject, topic):
        self.teacher = teacher
        self.student = student
        self.subject = subject
        self.topic = topic
    
    def give_lesson(self):
        print(f"{self.teacher} gave {self.student} a lesson on {self.subject} about {self.topic}")
        
    def give_homework(self):
        print(f"{self.teacher} gave {self.student} a homework on {self.subject} about {self.topic}")