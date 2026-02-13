# Error Message Detector

def count_errors(logs):
    error_count = 0

    for log in logs:
        if log == "ERROR":
            error_count += 1

    return error_count


if __name__ == "__main__":
    logs = ["INFO", "ERROR", "WARNING", "ERROR"]
    print("Total ERROR messages:", count_errors(logs))
