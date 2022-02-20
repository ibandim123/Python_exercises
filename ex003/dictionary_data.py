# this is my training with type of data storage in Python: Dictionary
# Create register for civilian population data

# Dictionary
register = {
  "id_person": "",
  "name": "",
  "birthYear": "" ,
  "sex": "",
  "height": "",
  "place_home": "",
  "body_type": "",
  "skin": "",
  "skill": "",
  "profession": ""
}

# Place register data
register["id_person"] = input("Civilian ID:")
register["name"] = input("Name:")
register["birthYear"] = input("Birth Year:")
register["sex"] = input("Sex:")
register["height"] = input("Height of this person:")
register["place_home"] = input("Place birth:")
register["body_type"] = input("Body Type:")
register["skin"] = input("Skin:")
register["skill"] = input("Skills:")
register["profession"] = input("Profession or Job:")

# print
print(register)

#================================================================
# Another exemple: 

civilian = dict()

civilian['name'] = str(input('Name:'))
civilian['id']   = int(input('ID:'))
civilian['sex']  = str(input('Sex:'))
civilian['birth']= int(input('birth:'))
civilian['body'] = str(input('body:'))
civilian['skin'] = str(input('skin:'))
civilian['skill']= str(input('skill:'))
civilian['Job']  = str(input('Job:'))


print(civilian)

# this print have same propost
