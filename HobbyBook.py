my_info = {"name": "Jorge Navarro",
           "occupation": "Student",
           "age": 35,
           "hobbies": ["Cook", "Play Videos Games", "watch racing"],
           "wake-up":{"Mon - Sat": 6, "Sunday": 11}}

# Print out results are stored in the dictionary
print(f'Hello I am {my_info["name"]} and I am a {my_info["occupation"]}')
print(f'I have {len(my_info["hobbies"])} hobbies!')
print(f'On Sundays I get up at {my_info["wake-up"]["Sunday"]}')