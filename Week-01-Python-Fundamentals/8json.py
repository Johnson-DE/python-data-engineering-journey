"""import json

data = '{"name":"john","age":23,"city":"tenkasi"}'

parsed = json.loads(data)

print(parsed["name"])
"""

#Problem 1 (Access multiple JSON values)

"""import json

data = '{"name":"john","age":23,"city":"tenkasi"}'

parsed = json.loads(data)

print(parsed["name"])
print(parsed["age"])
print (parsed["city"])"""

#Problem 2 — Add New Value

"""import json
data = '{"name":"john", "age":23, "city":"tenkasi"}'
parsed = json.loads(data)
parsed["skills"] = "pyhton"
print(parsed["skills"])"""

#Problem 3 — Loop Through JSON

"""import json

data = '{"name":"john","age":23, "city":"tenkasi"}'
parsed = json.loads(data)

for key in parsed:
    print(key,parsed[key])"""

# JSON Array Handling

"""import json

data = '''[
    {"name":"john", "age":23, "city":"tenkasi"},
    {"name":"prem", "age":25, "city":"tenkasi"}
    ]'''

parsed = json.loads(data)
parsed.append (
    {"name":"arun", "age":27, "city":"madurai"}
    )

for person in parsed:
    print(person["name"],person["age"])"""

#JSON DUMPS

import json

student = {
    "name":"john",
    "age": 23,
    "city":"tenkasi"
}

json_data = json.dumps(student)

print(json_data)