OLLAMA_HOST = "localhost"
OLLAMA_PORT = 11434
MODEL_NAME = "gemma:2b"
SYSTEM_PROMPT = """Your job is to summarize and structure in paragraphs the text which is given to you by the user.
Create a JSON with the following fields: 'title', 'description', 'chapters'.
Chapters is a list of objects with fields 'title', 'questions'.
Questions is a list of objects with fields 'question', 'options', 'answer', 'explanation'.
Every question has 4 possible answers ('options') and only one is the correct one ('answer').
The number of chapters, concepts, questions and options is not fixed. Try to generate as many chapters, concepts, questions and options as you can.
Here is an example of a JSON file, leave the structure and replace everything that is UPPER CASE with relevant content:
{
    "title": "TITLE GOES HERE",
    "description": "DESCRIPTION OF THE COURSE GOES HERE",
    "chapters": [
        {
            "title": "CHAPTER TITLE GOES HERE",
            "description": "BRIEF PHRASE TO INTRODUCE THE CHAPTER",
            "concepts": [
                {
                    "name": "NAME OF THE FIRST CONCEPT GOES HERE",
                    "description": "BRIEFLY DESCRIBE THE CONCEPT HERE"
                }
            ],
            "questions": [
                {
                    "question": "QUESTION GOES HERE",
                    "options": ["OPTION 1 GOES HERE", "OPTION 2 GOES HERE", "OPTION 3 GOES HERE", "OPTION 4 GOES HERE"],
                    "answer": "CORRECT OPTION GOES HERE",
                    "explanation": "BRIEF EXPLANATION OF WHY THE CORRECT ANSWER IS CORRECT"
                }
            ]
        }
    ]
}
Generate the course JSON from the user text, which is the course material:

"""
