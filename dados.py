import csv
def load_access():
  x = []
  y = []

  file = open('access.csv', 'r')
  reader = csv.reader(file)
  next(reader)

  for home, como_funciona, contato, comprou in reader:
    x.append([int(home), int(como_funciona), int(contato)])
    y.append(int(comprou))
  return x, y  

load_access()
