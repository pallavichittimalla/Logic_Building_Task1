# Message Length Analyzer

def analyze_messages(messages):
    for message in messages:
        length = len(message)
        print(f"Message: {message} | Length: {length}")

        if length > 10:
            print("Flag: Message longer than 10 characters")
        print()


if __name__ == "__main__":
    messages = ["Hi", "Welcome to the platform", "OK"]
    analyze_messages(messages)
