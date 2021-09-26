
import pickle
import sys

def predict(data):
    #Your prediction code here
    with open("./asset/pickle_model.pkl","rb") as file:
      pickle_file=pickle.load(file)
    for i in range(len(data)):
      if(type(data[i])==str):
        data[i]=float(data[i])
      print(data)
    score=pickle_file.score([data],[2])
    data=score*100
    return data

# data = []
# predict(data)