# nesting Dictionary inside a Dictionary and List inside a Dictionary

# example 1
travel_blog = {
    "India":"Delhi",
    "famous_places": ["Hyderabad","Delhi","Chennai","AP"],
    "most_famous_visiting": {
        "Hyderabad": ["Charminar","Golkonda","Palaknama Palace"],
        "Delhi": ["RedFort","TajMahal"],
        "Chennai":["Beach","Temple"],
        "AP":["Thirupathi","beach","etccccc"],
        "Nagole": ["temples","restaruents","friends"],
        "NagoleTemples": {
            "temples" :["Hanuman","SriRam","Baba"],
        }
    }
}

# dictionary -- dictrionary ---> key = nagoleTemples -- dictiionary --> temples -- List

# printing dictionary of all keys
print(travel_blog)

# Printing only value using key
print(travel_blog["India"])   #India

# Print all list of famous places in India
print(travel_blog["famous_places"]) # List type

# Each and every value in famous palces
for place in travel_blog["famous_places"]:
    print(place)
    
# output
# Hyderabad
# Delhi

for place in travel_blog["most_famous_visiting"]["Hyderabad"]:
    print(place)

for place in travel_blog["most_famous_visiting"]["Hyderabad"]:
    # print(place)
    if place == "Golkonda":
        print("ONly one Paritcular place in Hyderabd ==> :" + place)



# Nesting Dictionary inside the List

countries = [
   { "India"},
   { "USA"},
   { "Japan"},
]


