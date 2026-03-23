# data = {
#     "a": "A",
#     "b": "B",
#     "c": "C"
# }

# print(data["a"], data["b"])

# for i in data:
#     print(f"{i} is {data[i]}")

# Example

students = [
    {
        "name": "Heromine",
        "house": "Gryffindor",
        "patronus": "Otter"
    },
    {
        "name": "Harry",
        "house": "Gryffindor",
        "patronus": "Stag"
    },
    {
        "name": "Ron",
        "house": "Gryffindor",
        "patronus": "Jack Russell"
    },
    {
        "name": "Draco",
        "house": "Sydney",
        "patronus": None,
    }
]

for i in range(len(students)):
    print(f"{i+1}. {students[i]["name"]} lives in {students[i]["house"]} and patronus is {students[i]["patronus"]}.")