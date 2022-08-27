from datetime import datetime
import os
absolute_path = os.path.dirname(__file__)
relative_path = "out\\"
full_path = os.path.join(absolute_path, relative_path)
now = datetime.now()
current_time = now.strftime("%H.%M.%S")
prefix = input('prefix: ')
suffix = input('suffix: ')
text = input('text: ')
textnow = ''
f = open(full_path + current_time + '.txt', 'x', encoding = 'utf-8')
for x in range(len(text) * 2 - 1):
  if (x >= len(text)):
    textnow = textnow[:-1]
  else:
    textnow += text[x]
  f.write(prefix + textnow + suffix + '\n')
