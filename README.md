# IELTS Mate AI

An AI-powered IELTS learning assistant built with Python and OpenAI/OpenRouter APIs.

This project was created as an AI Engineering practice assignment to demonstrate:

* chatbot interaction
* context injection
* multi-step AI pipeline
* quiz evaluation
* JSON result storage

---

# Features

## Writing Advisor

Generate IELTS Writing study strategies based on:

* target IELTS band
* remaining study days

## Reading Advisor

Generate IELTS Reading strategies including:

* skimming
* scanning
* vocabulary improvement
* time management

## Structure Quiz

Generate IELTS grammar quizzes with:

* multiple choice questions
* answer evaluation
* score analysis
* grammar explanations

## AI Pipeline

The application uses a multi-step AI workflow:

```text
User Input
↓
Generate Learning Content
↓
Evaluate Answers (Structure mode only)
↓
Summarize Feedback
↓
Extract Learning Insights
↓
Save Session Result to JSON
```

---

# Tech Stack

* Python
* OpenAI SDK
* OpenRouter API
* dotenv
* JSON

---

# Project Structure

```text
project/
│
├── chatbot.py
├── main.py
├── .env
├── requirements.txt
└── student_result.json
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/sarahmadhani/ielts-mate-ai.git
cd ielts-mate-ai
```

---

## 2. Install Dependencies

Using uv:

```bash
uv sync
```

Or using pip:

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
API_KEY=your_openrouter_api_key
BASE_URL=https://openrouter.ai/api/v1
```

---

# Running the Project

Using uv:

```bash
uv run main.py
```

Or using python:

```bash
python main.py
```

---

# Example Workflow

```text
===== IELTS AI Advisor =====

Enter your target IELTS band: 7
Days before IELTS test: 20

Choose your focus area:
1. Writing
2. Reading
3. Structure
```

If the user selects Structure:

```text
AI generates grammar questions
↓
User submits answers
↓
AI evaluates score and explanations
↓
AI summarizes weaknesses
↓
AI extracts learning insights
```

---

# AI Engineering Concepts Used

## 1. Context Injection

The AI receives additional learning context:

* target IELTS band
* days before exam
* selected learning topic

Example:

```python
The student targets IELTS band 7.
The student has 20 days before the exam.
```

---

## 2. Multi-Step Pipeline

The project follows a structured AI pipeline:

```python
generate_learning_content()
↓
evaluate_user_answers()
↓
summarize_feedback()
↓
extract_learning_insights()
↓
save_session_result()
```

---

## 3. Prompt Engineering

Different prompts are dynamically generated based on:

* Writing
* Reading
* Structure

---

## 4. JSON Session Storage

The application stores learning results in:

```text
student_result.json
```

Example:

```json
{
    "selected_topic": "Structure",
    "summary": "Student needs improvement in article usage.",
    "learning_insights": "Practice grammar exercises daily."
}
```

---

# Future Improvements

Potential future enhancements:

* Streamlit UI
* Speaking practice mode
* PDF material integration
* Band score prediction
* Vocabulary tracking
* Personalized study plans

---

# Author

Created by Sarah Ramadhani as part of AI Engineering practice and IELTS preparation learning.
