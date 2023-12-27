import json

jso ={
  "nom": "Jean",
  "age": 25,
  "ville": "Paris"
}


with open("data.json","w") as file:
     json.dump(jso,file)
     print("succes")

with open ("data.json","r") as file :
     data = json.load(file)
     print(data)

data["language"] = "python"
with open("data.json","w") as file:
     json.dump(data,file)

with open("data.json","r") as file:
     data2=json.load(file)
     print("the modification:",data2)
