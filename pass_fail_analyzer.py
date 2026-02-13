# Pass / Fail Analyzer

def analyze_results(marks):
    pass_count = 0
    fail_count = 0

    for mark in marks:
        if mark >= 50:
            pass_count += 1
        else:
            fail_count += 1

    print("Total Students:", len(marks))
    print("Total Passed:", pass_count)
    print("Total Failed:", fail_count)


if __name__ == "__main__":
    marks = [45, 78, 90, 33, 60]
    analyze_results(marks)
