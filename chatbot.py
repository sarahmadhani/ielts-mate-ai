
import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)

MODEL_NAME = "gpt-4o-mini"

def run_ai_pipeline(
    system_prompt: str,
    user_prompt: str
) -> str:
    """
    Generic AI execution layer.

    This function acts as the central gateway
    between the application and the LLM.
    """

    try:

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as error:

        return f"""
        AI Pipeline Error:
        {error}
        """


# ==========================================
# STEP 1
# GENERATE LEARNING CONTENT
# ==========================================
def generate_learning_content(
    selected_topic: str,
    target_band: str,
    days_left: str
) -> str:

    system_prompt = """
    You are a professional IELTS tutor.

    Your responsibilities:
    - teach IELTS concepts clearly
    - provide practical study strategies
    - help intermediate learners
    - generate quizzes when needed
    """

    # ======================================
    # STRUCTURE QUIZ MODE
    # ======================================
    if selected_topic == "Structure":

        user_prompt = f"""
        The student targets IELTS band {target_band}.
        The student has {days_left} days before the exam.

        Generate 5 IELTS grammar multiple-choice questions.

        Requirements:
        - 4 answer options (A, B, C, D)
        - intermediate IELTS difficulty
        - focus on grammar and sentence structure
        - do not provide answers
        - do not provide explanations
        """

    # ======================================
    # WRITING MODE
    # ======================================
    elif selected_topic == "Writing":

        user_prompt = f"""
        The student targets IELTS band {target_band}.
        The student has {days_left} days before the exam.

        Generate IELTS Writing strategies.

        Include:
        - common mistakes
        - writing improvement tips
        - daily habits
        - time management advice

        Limit response to 250 words.
        """

    # ======================================
    # READING MODE
    # ======================================
    elif selected_topic == "Reading":

        user_prompt = f"""
        The student targets IELTS band {target_band}.
        The student has {days_left} days before the exam.

        Generate IELTS Reading strategies.

        Include:
        - skimming techniques
        - scanning techniques
        - vocabulary tips
        - time management advice

        Limit response to 250 words.
        """

    else:

        user_prompt = """
        Generate general IELTS preparation advice.
        """

    return run_ai_pipeline(
        system_prompt,
        user_prompt
    )


# ==========================================
# STEP 2
# EVALUATE USER ANSWERS
# ==========================================
def evaluate_user_answers(
    generated_questions: str,
    user_answers: str
) -> str:

    system_prompt = """
    You are an IELTS grammar evaluator.
    """

    user_prompt = f"""
    Evaluate the student's answers.

    Questions:
    {generated_questions}

    Student Answers:
    {user_answers}

    Include:
    - correct answers
    - final score
    - grammar explanations
    - improvement advice
    """

    return run_ai_pipeline(
        system_prompt,
        user_prompt
    )


# ==========================================
# STEP 3
# SUMMARIZE AI RESULT
# ==========================================
def summarize_feedback(
    raw_feedback: str
) -> str:

    system_prompt = """
    You summarize IELTS feedback clearly.
    """

    user_prompt = f"""
    Summarize this IELTS feedback into concise points:

    {raw_feedback}
    """

    return run_ai_pipeline(
        system_prompt,
        user_prompt
    )

# ==========================================
# STEP 4
# EXTRACT LEARNING INSIGHTS
# ==========================================
def extract_learning_insights(
    summarized_feedback: str
) -> str:

    system_prompt = """
    You extract actionable IELTS learning insights.
    """

    user_prompt = f"""
    Extract:
    - main weaknesses
    - study strategies
    - daily improvement habits

    From this content:

    {summarized_feedback}
    """

    return run_ai_pipeline(
        system_prompt,
        user_prompt
    )

# ==========================================
# STEP 5
# SAVE SESSION RESULT
# ==========================================
def save_session_result(
    selected_topic: str,
    raw_information: str,
    summarized_feedback: str,
    extracted_insights: str
):

    session_data = {

        "selected_topic": selected_topic,

        "raw_information": raw_information,

        "summary": summarized_feedback,

        "learning_insights": extracted_insights
    }

    with open(
        "student_result.json",
        "w"
    ) as file:

        json.dump(
            session_data,
            file,
            indent=4
        )

    print(
        "\nSession result saved successfully."
    )
