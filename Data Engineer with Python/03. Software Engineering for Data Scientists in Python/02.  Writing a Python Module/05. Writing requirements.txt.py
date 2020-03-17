'''
Writing requirements.txt
We covered how having a requirements.txt file can help your package be more portable by allowing your users to easily recreate its intended environment. In this exercise, you will be writing the contents of a requirements file to a python variable.

Note, in practice, the code you write in this exercise would be written to it's own txt file instead of a variable in your python session.

Instructions
100 XP
Write the requirement for matplotlib with at least version 3.0.0 or above.
Write the requirement for numpy version 1.15.4 exactly.
Write the requirement for pandas with at most version 0.22.0.
Write a non-version specific requirement for pycodestyle
'''
SOLUTION

requirements = """
matplotlib>=3.0.0
numpy==1.15.4
pandas<=0.22.0
pycodestyle
"""