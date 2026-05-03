from chatbot import (
    generate_learning_content,
    evaluate_user_answers,
    summarize_feedback,
    extract_learning_insights,
    save_session_result
)

# ==========================================
# IELTS AI ADVISOR
# ==========================================
print("===== IELTS AI Advisor =====")

# ==========================================
# USER INPUT
# ==========================================
target_band = input(
    "Enter your target IELTS band: "
)

days_left = input(
    "Days before IELTS test: "
)

print("\nChoose your focus area:")
print("1. Writing")
print("2. Reading")
print("3. Structure")

choice = input(
    "Enter your choice: "
)

# ==========================================
# TOPIC ROUTING
# ==========================================
if choice == "1":

    selected_topic = "Writing"

elif choice == "2":

    selected_topic = "Reading"

elif choice == "3":

    selected_topic = "Structure"

else:

    print(
        "Invalid choice. Defaulting to Structure."
    )

    selected_topic = "Structure"

# ==========================================
# STEP 1
# GENERATE LEARNING CONTENT
# ==========================================
print("\n[AI is generating content...]")

raw_information = generate_learning_content(
    selected_topic,
    target_band,
    days_left
)

print(
    f"\n===== {selected_topic.upper()} TASK =====\n"
)

print(raw_information)

# ==========================================
# STRUCTURE QUIZ FLOW
# ==========================================
if selected_topic == "Structure":

    user_answers = input(
        "\nEnter your answers (example: 1A 2B 3C): "
    )

    print(
        "\n[AI is evaluating answers...]"
    )

    # STEP 2
    evaluation = evaluate_user_answers(
        raw_information,
        user_answers
    )

    print("\n===== EVALUATION =====\n")

    print(evaluation)

    pipeline_input = evaluation

# ==========================================
# WRITING & READING FLOW
# ==========================================
else:

    pipeline_input = raw_information

# ==========================================
# STEP 3
# SUMMARIZE FEEDBACK
# ==========================================
print("\n[AI is summarizing feedback...]")

summary = summarize_feedback(
    pipeline_input
)

print("\n===== SUMMARY =====\n")

print(summary)

# ==========================================
# STEP 4
# EXTRACT LEARNING INSIGHTS
# ==========================================
print(
    "\n[AI is extracting learning insights...]"
)

learning_insights = extract_learning_insights(
    summary
)

print(
    "\n===== KEY TAKEAWAYS =====\n"
)

print(learning_insights)

# ==========================================
# STEP 5
# SAVE SESSION RESULT
# ==========================================
save_session_result(
    selected_topic,
    raw_information,
    summary,
    learning_insights
)

print(
    "\nSession completed successfully."
)

print(
    "Good luck with your IELTS preparation!"
)