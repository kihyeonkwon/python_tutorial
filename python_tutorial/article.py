class User:
    name = ''
    age = 0

    def __init__(self, name=name, age = age):
        self.name = name
        self.age = age


class Review:
    title = ''
    content = ''
    user = ''

    def __init__(self, content=content, title=title, user=user):
        self.content = content 
        self.title = title
        self.user = user


user1 = User(name="홍길동", age=30)

review1 = Review(title="이거 좀 재밌네", content="어쩌구 저쩌구", user=user1)
print(review1.user.name)

user1.name = "김길동"
print(review1.user.name)
