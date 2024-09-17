import math
total_width = 30
padding = 10

# TODO rewrite cantor_pattern as a recursive function
# that terminates when there is only one '-' in most recent
# line of the pattern
def cantor_pattern(n):
  seg = '-' * math.floor(total_width/n) 
  n_repeat = math.ceil((total_width-n)/(len(seg)))
  pattern = (seg + ' ') * n_repeat
  n_pad = math.floor((total_width+padding - len(pattern))/2)
  pattern = n_pad * ' ' + pattern + n_pad * ' '
  print(pattern)

for i in range(1, 25):
  cantor_pattern(i)
  
