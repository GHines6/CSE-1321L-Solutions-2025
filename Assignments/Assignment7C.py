def get_scores():
    while True:
        try:
            num_students = int(input("Enter number of students: "))
            if num_students <= 0:
                print("Error: Number of students must be at least 1.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid integer.")
    scores = []
    for i in range(1, num_students + 1):
        while True:
            try:
                score = int(input(f"Enter score for student {i}: "))
                break
            except ValueError:
                print("Error: Please enter a valid integer.")
        scores.append(score)
    return scores
def analyze_scores(scores):
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)
    passed = sum(1 for s in scores if s >= 60)
    failed = len(scores) - passed
    return highest, lowest, average, passed, failed
def display_results(high, low, avg, passed, failed):
    print()
    print("--- Score Report ---")
    print(f"Highest score: {high}")
    print(f"Lowest score: {low}")
    print(f"Average score: {avg:.1f}")
    print(f"Students passed: {passed}")
    print(f"Students failed: {failed}")
def main():
    scores = get_scores()
    high, low, avg, passed, failed = analyze_scores(scores)
    display_results(high, low, avg, passed, failed)
main()