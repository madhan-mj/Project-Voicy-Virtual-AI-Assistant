import random
import json
import torch
from Brain import NeuralNet
from NeuralNetwork import bag_of_words,tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json','r') as json_data:
      intents = json.load(json_data)

FILE = "Tasks.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#--------------------------------------------

Name = "A I"


from Speak import say
from Task import NonInputExecution
from Task import InputExecution
from Task import wish
wish()

from Listen import Listen
def Main():
            
      query = Listen()
      sentence = str(query.lower())
      result = str(sentence)

      sentence = tokenize(sentence)
      X = bag_of_words(sentence,all_words)
      X = X.reshape(1,X.shape[0])
      X = torch.from_numpy(X).to(device)

      output = model(X)

      _ , predicted = torch.max(output,dim=1)

      tag = tags[predicted.item()]

      probs = torch.softmax(output,dim=1)
      prob = probs[0][predicted.item()]

      if prob.item() > 0.75:

            for intent in intents['intents']:

                  if tag == intent["tag"]:

                        reply = random.choice(intent["responses"])
                        
                        
                        if tag == 'bye':
                              reply = random.choice(intent["responses"])
                              say(reply)
                              exit()

                        elif "date" in reply:
                              NonInputExecution(reply)

                        elif "time" in reply:
                              NonInputExecution(reply)

                        elif "day" in reply:
                              NonInputExecution(reply)

                        elif "wikipedia" in reply:
                              InputExecution(reply,result)

                        elif "google" in reply:
                              say("searching google...")
                              InputExecution(reply,result)
                        
                        elif "music" in reply:
                              say("playing songs from youtube!")
                              InputExecution(reply,result)

                        elif "temperature" in reply:
                              InputExecution(reply,result)

                        elif "shutdown" in reply:
                              InputExecution(reply,result)
                              
                        elif "restart" in reply:
                              InputExecution(reply,result)

                        elif "sleep" in reply:
                              InputExecution(reply,result)
                      
                        elif "close" in reply:
                              InputExecution(reply,result)

                        elif "news" in reply:
                              NonInputExecution(reply)

                        elif "play music" in reply:
                              InputExecution(reply,result)

                        elif "switch window" in reply:
                              InputExecution(reply,result)  

                        elif "email" in reply:
                              InputExecution(reply,result) 
                         
                        elif "battery" in reply:
                              InputExecution(reply,result)

                        else :
                              say(reply)


while True:
      
      Main()

