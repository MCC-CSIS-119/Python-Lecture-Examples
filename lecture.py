class_full = False
max_class_size = 5
class_name = "Math"

students = ["Dan", "Joy", "Joe", "Yubenis"]

accredited_classes = ["Scripting", "Linux"]

students.append("Stewart")

if len(students) >= max_class_size:
    class_full = True

if class_full and class_name in accredited_classes:
    print(f"{class_name} is full and accredited")
else:
    print(f"{class_name} is open and not accredited")
