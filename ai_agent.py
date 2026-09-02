# Rule-Based Student Study Recommendation Agent
# SLE-1: Introduction to Artificial Intelligence

def study_agent(study_hours, difficulty, exam_days):
    """
    A simple rule-based AI agent that recommends
    a study strategy based on user inputs.
    """

    if exam_days <= 3 and difficulty == "high":
        recommendation = (
            "Focus on difficult concepts and practice important problems."
        )

    elif exam_days <= 7 and study_hours < 2:
        recommendation = (
            "Increase your study time and revise the most important topics."
        )

    elif difficulty == "high":
        recommendation = (
            "Spend more time understanding difficult concepts "
            "and solve practice problems."
        )

    elif difficulty == "medium":
        recommendation = (
            "Revise the concepts and solve a few practice questions."
        )

    else:
        recommendation = (
            "Review the concepts and continue with regular practice."
        )

    return recommendation


print("=== Student Study Recommendation Agent ===")

study_hours = float(input("Enter your available study hours per day: "))

difficulty = input(
    "Enter subject difficulty (low/medium/high): "
).lower()

exam_days = int(input("Enter days remaining for exam: "))

result = study_agent(study_hours, difficulty, exam_days)

print("\nAI Agent Recommendation:")
print(result)
