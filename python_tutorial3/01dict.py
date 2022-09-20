members = []

person1 = {"성별": "남자", "이름": "강기훈", "나이": 20, "취미": ["자전거", "산책", "먹방"]}
person2 = {"이름": "유승주", "한국나이": 20, "성별": "여자"}
person3 = {"이름": "신중민", "나이": 18, "성별": "남자"}


# print(person2["나이"]["한국 나이"])

# members.append(person1)
# members.append(person2)
# members.append(person3)

for i in range(4):
    members.append("person" + str(i))

print(members)

# total_age = 0
# for member in members:
#     total_age += member['나이']

# print(total_age/len(members))
# print(members[0]["나이"])


# for value, key in person1.items():
#     print(value)
