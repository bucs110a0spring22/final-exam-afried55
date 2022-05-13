import requests
class MathAd:

  def __init__(self, number = "0"):
    '''Initiates a MathAd object
    args: self, number (str)'''
    self.api_url = f"https://api.isevenapi.xyz/api/iseven/{number}/"

  def __str__(self):
    '''Returns the string for the MathAd object'''
    return "A random ad and if a number is even"
 
  def get(self):
    '''Turns the information from the API into a dictionary.
    args: self (MathAd object)
    returns: expression (dict)'''
    r = requests.get(self.api_url)
    expression = r.json()
    return expression