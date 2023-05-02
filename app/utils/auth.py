from flask import session, redirect
from functools import wraps

def login_required(func):
  @wraps(func)
  def wrapped_function(*args, **kwargs):
    if session.get('loggedIn') == True:
      #This is where the function is ran IF the user is logged in via session
      return func(*args, **kwargs)

    return redirect('/login')
  
  return wrapped_function