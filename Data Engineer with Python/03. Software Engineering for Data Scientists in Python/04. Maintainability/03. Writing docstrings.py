'''
Writing docstrings
We just learned some about the benefits of docstrings. In this exercise, you will practice writing docstrings that can be utilized by a documentation generator like Sphinx.

Note that your docstring submission must match the solution exactly. If you find yourself getting it wrong several times, it may be a good idea to refresh the sample code and start over.

Instructions
100 XP
Complete the portions of the docstring that document the parameters.
Complete the portion of the docstring describing the return value.
Complete the example function usage in the docstring.
'''
SOLUTION

# Complete the function's docstring
def tokenize(text, regex=r'[a-zA-z]+'):
  """Split text into tokens using a regular expression

  :param text: text to be tokenized
  :param regex: regular expression used to match tokens using re.findall 
  :return: a list of resulting tokens

  >>> tokenize('the rain in spain')
  ['the', 'rain', 'in', 'spain']
  """
  return re.findall(regex, text, flags=re.IGNORECASE)

# Print the docstring
help(tokenize) 