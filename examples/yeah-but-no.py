import random
import math

# creates a long sentence composed of 
# yeah, no, but, i mean, like, and so on

phrases = ['yeah', 'no', 'but', 'i mean', 'like']

# recursive solution
def yeah_but_no(n, phrase=''):
    if n == 0:
        return phrase[1:]
    # randomlly select a phrase from the list that is not the last one
    fragment = random.choice(phrases)
    while fragment == phrase[-len(fragment):]:
        fragment = random.choice(phrases)
    return yeah_but_no(n - 1, phrase + ' ' + fragment)

# iterative solution 
def yeah_but_no_loop(n):
  phrase = ''
  for i in range(n):
     # randomlly select a phrase from the list that is not the last one
    fragment = random.choice(phrases)
    while fragment == phrase[-len(fragment):]:
        fragment = random.choice(phrases)
    phrase += ' ' + fragment 
  return phrase[1:]

for depth in range(3, 12):
  print(yeah_but_no(depth))
  #print(yeah_but_no_loop(depth))
