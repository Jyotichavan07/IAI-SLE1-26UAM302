# Rule-Based Student Study Recommendation Agent
# SLE-1: Introduction to Artificial Intelligence

def study_agent(study_hours, difficulty, exam_days):
    """
    A simple rule-based AI agent that analyzes
    study conditions and provides recommendations.
    """

    # Determine urgency
    if exam_days <= 3:
        urgency = "HIGH"
    elif exam_days <= 7:
        urgency = "MEDIUM"
    else:
        urgency = "LOW"

    # Rule-based decision making
    if exam_days <= 3 and difficulty == "high":
        recommendation = (
            "Focus on difficult concepts and practice important problems."
        )
        action_plan = [
            "Revise difficult concepts",
            "Practice important problems",
            "Take a short mock test",
            "Review mistakes"
        ]

    elif exam_days <= 3:
        recommendation = (
            "Focus on revision and important exam topics."
        )
        action_plan = [
            "Revise important topics",
            "Review notes",
            "Practice previous questions",
            "Avoid starting too many new topics"
        ]

    elif exam_days <= 7 and study_hours < 2:
        recommendation = (
            "Increase your study time and focus on high-priority topics."
        )
        action_plan = [
            "Increase daily study time",
            "Prioritize important topics",
            "Practice questions",
            "Revise weak areas"
        ]

    elif difficulty == "high":
        recommendation = (
            "Spend more time understanding difficult concepts "
            "and solve practice problems."
        )
        action_plan = [
            "Understand difficult concepts",
            "Make short revision notes",
            "Solve practice problems",
            "Test your understanding"
        ]

    elif difficulty == "medium":
        recommendation = (
            "Revise the concepts and solve practice questions regularly."
        )
        action_plan = [
            "Revise important concepts",
            "Solve practice questions",
            "Review mistakes",
            "Perform regular revision"
        ]

    else:
        recommendation = (
            "Maintain regular study and continue with concept revision."
        )
        action_plan = [
            "Review concepts",
            "Practice regularly",
            "Revise previous topics",
            "Track your progress"
        ]

    return urgency, recommendation, action_plan


print("=" * 55)
print("       STUDENT STUDY RECOMMENDATION AGENT")
print("=" * 55)

# Get user input
while True:
    try:
        study_hours = float(
            input("\nEnter your available study hours per day: ")
        )

        if study_hours < 0:
            print("Study hours cannot be negative.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")


while True:
    difficulty = input(
        "Enter subject difficulty (low/medium/high): "
    ).lower().strip()

    if difficulty in ["low", "medium", "high"]:
        break

    print("Please enter only: low, medium, or high.")


while True:
    try:
        exam_days = int(
            input("Enter days remaining for exam: ")
        )

        if exam_days < 0:
            print("Days remaining cannot be negative.")
            continue

        break

    except ValueError:
        print("Please enter a valid whole number.")


# Run the AI agent
urgency, recommendation, action_plan = study_agent(
    study_hours,
    difficulty,
    exam_days
)


# Display results
print("\n" + "=" * 55)
print("                    AI ANALYSIS")
print("=" * 55)

print("\nInput Summary")
print("-" * 55)
print(f"Study Hours/Day : {study_hours:.1f} hours")
print(f"Difficulty      : {difficulty.upper()}")
print(f"Days Remaining  : {exam_days} days")

print("\nAI Decision")
print("-" * 55)
print(f"Urgency Level   : {urgency}")
print(f"Difficulty      : {difficulty.upper()}")

print("\nRecommendation")
print("-" * 55)
print(recommendation)

print("\nAction Plan")
print("-" * 55)

for number, action in enumerate(action_plan, start=1):
    print(f"{number}. {action}")

print("\n" + "=" * 55)
print("             END OF AI RECOMMENDATION")
print("=" * 55)
