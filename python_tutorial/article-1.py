class Review:
    title = ''
    content = ''
    user = ''

    def __init__(self, content=content, title=title, user=user):
        self.content = content 
        self.title = title
        self.user = user


review1 = Review(title="인생 영화입니다", content="어쩌구 저쩌구111", user="권기현")
review2 = Review(title="돈 아깝다", content="어쩌구 저쩌구222", user="김기현")
review3 = Review(title="이건 영화관에서 봐야됨", content="어쩌구 저쩌구333", user="이기현")
review4 = Review(title="가족들이랑 보지 마세요", content="어쩌구 저쩌구4444", user="손기현")


print(review1.title, review1.content, review1.user)
print(review2.title, review2.content, review2.user)