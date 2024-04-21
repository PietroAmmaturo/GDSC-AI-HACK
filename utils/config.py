OLLAMA_HOST = "localhost"
OLLAMA_PORT = 11434
MODEL_NAME = "gemma:2b"
SYSTEM_PROMPT = """Create a JSON of type 'course' with the following fields: 'title', 'description', 'chapters'.
Chapters is a list of objects with fields 'title', 'questions'.
Questions is a list of objects with fields 'question', 'answers', 'correct_answer'.
Every question has 4 possible answers ('answers') and only one is the correct one ('correct_answer'). 
Here is an example of a JSON file, leave the structure as it is and replace the contents: {
    "title": "Test title",
    "description": "Test description",
    "chapters": [
        {
            "title": "Chapter 1",
            "description": "brief phrase to introduce the chapter",
            "concepts": [
                {
                    "name": "Concept 1",
                    "description": "small bullet point to recap the concept"
                },
                {
                    "name": "Concept 2",
                    "description": "small bullet point to recap the concept"
                }
            ],
            "questions": [
                {
                    "question": "Question 1",
                    "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
                    "answer": "Option 1",
                    "explanation": "brief explanation of the correct answer"
                },
                {
                    "question": "Question 2",
                    "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
                    "answer": "Option 1",
                    "explanation": "brief explanation of the correct answer"
                },
                {
                    "question": "Question 3",
                    "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
                    "answer": "Option 3",
                    "explanation": "brief explanation of the correct answer"
                }
            ]
        },
        {
            "title": "Chapter 2",
            "description": "brief phrase to introduce the second chapter",
            "concepts": [
                {
                    "name": "Concept 1",
                    "description": "small bullet point to recap the concept"
                },
                {
                    "name": "Concept 2",
                    "description": "small bullet point to recap the concept"
                }
            ],
            "questions": [
                {
                    "question": "Question 1",
                    "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
                    "answer": "Option 1",
                    "explanation": "brief explanation of the correct answer"
                }
            ]
        },
        {
            "title": "Chapter 3",
            "description": "brief phrase to introduce the chapter",
            "concepts": [
                {
                    "name": "Concept 1",
                    "description": "small bullet point to recap the concept"
                },
                {
                    "name": "Concept 2",
                    "description": "small bullet point to recap the concept"
                }
            ],
            "questions": [
                {
                    "question": "Question 1",
                    "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
                    "answer": "Option 1",
                    "explanation": "brief explanation of the correct answer"
                }
            ]
        }
    ]
}
Generate the course JSON from the following text, which is the course material:

"""

