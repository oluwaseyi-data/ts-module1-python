
import csv
import statistics
import sys


def letter(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def load_students(filename):
    students = []

    with open(filename) as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                score = float(row["score"])

                students.append({
                    "name": row["name"],
                    "score": score,
                    "grade": letter(score)
                })

            except ValueError:
                print(
                    f"Invalid score for {row['name']}: {row['score']}",
                    file=sys.stderr
                )

    return students


def calculate_statistics(students):
    scores = [student["score"] for student in students]

    if not scores:
        return None

    return {
        "count": len(scores),
        "mean": statistics.mean(scores),
        "median": statistics.median(scores),
        "highest": max(scores),
        "lowest": min(scores)
    }


def print_report(stats):
    if stats is None:
        print("No valid scores to report.")
        return

    print("\n=== Class Report ===")
    print(f"Number of Students: {stats['count']}")
    print(f"Mean Score: {stats['mean']:.2f}")
    print(f"Median Score: {stats['median']:.2f}")
    print(f"Highest Score: {stats['highest']:.2f}")
    print(f"Lowest Score: {stats['lowest']:.2f}")


def save_report(students, filename="gradebook/report.txt"):
    sorted_students = sorted(
        students,
        key=lambda student: student["score"],
        reverse=True
    )

    with open(filename, "w") as file:
        file.write("=== Student Gradebook ===\n\n")

        for student in sorted_students:
            file.write(
                f"{student['name']}: "
                f"{student['score']:.2f} - Grade: {student['grade']}\n"
            )

    print(f"\nReport saved to {filename}")


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python gradebook/gradebook.py filename.csv")

    filename = sys.argv[1]

    if not filename.lower().endswith(".csv"):
        sys.exit("Please provide a CSV file.")

    try:
        students = load_students(filename)
    except FileNotFoundError:
        sys.exit("File not found.")

    stats = calculate_statistics(students)

    print_report(stats)

    if students:
        save_report(students)


if __name__ == "__main__":
    main()
