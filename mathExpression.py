import requests
class MathExpression:

  def __init__(self):
    '''Initiates a MathExpression object
    args: self'''
    self.api_url = "https://x-math.herokuapp.com/api/random"

  def __str__(self):
    return "A random math expression"
  def get(self):
    '''Turns the information from the API into a dictionary
    args: self (MathExpression object)
    returns: expression (dict)'''
    r = requests.get(self.api_url)
    expression = r.json()
    return expression