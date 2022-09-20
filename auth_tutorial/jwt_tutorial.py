# JWT 패키지를 사용합니다. (설치해야할 패키지 이름: PyJWT)
import jwt
import datetime

SECRET_KEY = "SPARTA"

payload = {
    "id": "kihyeon",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=1800),
}
token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

print(token)

# 위에까지가 로그인

decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
print(decoded_token)
