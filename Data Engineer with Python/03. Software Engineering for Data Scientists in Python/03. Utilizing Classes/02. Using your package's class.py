'''
Using your package's class
You just wrote the beginnings of a Document class that you'll build upon to perform text analysis. In this exercise, you'll test out its current functionality of storing text.

Below is the document tree that you've built up so far when developing your package. You'll be working in my_script.py.

working_dir
├── text_analyzer
│    ├── __init__.py
│    ├── counter_utils.py
│    ├── document.py
└── my_script.py
Instructions
100 XP
import your text_analyzer package.
Create an instance of Document with the datacamp_tweet variable that's been loaded into your session.
Print the contents of the text attribute of your newly created Document instance.
'''
SOLUTION

# Import custom text_analyzer package
import text_analyzer

# Create an instance of Document with datacamp_tweet
my_document = text_analyzer.Document(text=datacamp_tweet)

# Print the text attribute of the Document instance
print(my_document.text)
