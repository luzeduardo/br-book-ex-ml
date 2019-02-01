from dados import load_access
from sklearn.naive_bayes import MultinomialNB
x, y = load_access()

modelo = MultinomialNB()
modelo.fit(x, y)
test_data = [1, 0 , 1]
result = modelo.predict([test_data])

print(result)