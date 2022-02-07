import time
import throttle

# limit to 3 calls
# allow more every 1 second
@throttle.wrap(1, 3)
def aesthetic(*values):

  return ' '.join(values).upper()

for index in range(10):

  result = aesthetic('beautiful')

  success = not result is throttle.fail

  print(index, success)

  time.sleep(0.23)