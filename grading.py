def get_marks():
    marks = int(input("Enter your marks (0-100): "))
    return marks

def evaluate_grade(marks):
    if 75 <= marks <= 100:
        return "A"
    elif 65 <= marks <= 74:
        return "B"
    elif 55 <= marks <= 64:
        return "C"
    elif 35 <= marks <= 54:
        return "S"
    elif 0 <= marks <= 34:
        return "F"
    else:
        return None

def main():
    marks = get_marks()
    grade = evaluate_grade(marks)
    if grade:
        print(f"Your grade is: {grade}")
    else:
        print("Invalid marks. Please enter a value between 0 and 100.")

if __name__ == "__main__":
    main()

