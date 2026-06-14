#Problem 5. Write a program to convert a student’s marks of a course into a grade.
# Use the grading criteria of our university.


def marktograde(mark):
    match(mark):
         case s if 90 <= s <= 100:
             return "A+"
         case s if 85 <= s < 90:
             return "A"
         case s if 80 <= s < 85:
             return "B+"
         case s if 75 <= s < 80:
             return "B"
         case s if 70 <= s < 75:
             return "C+"
         case s if 65 <= s < 70:
             return "C"
         case s if 60 <= s < 65:
             return "D+"
         case s if 50 <= s < 60:
             return "D"
         case s if 0 <= s < 50:
             return "F"
         
mark = float(input("Enter the mark: "))
print(f"Grade for {mark} is: {marktograde(mark)}")
         