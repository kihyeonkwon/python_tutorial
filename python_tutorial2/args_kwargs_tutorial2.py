def test_kwargs(*args, **kwargs):
    print('===========================')
    print(args)
    print(f'kwargs: {kwargs}')
    return True


info = {"age": "90", "name": "옆집할머니", "car": "아이오닉",
        "num": "010-1234-5678", "address": "경기도"}
test_kwargs(fruit1='사과', fruit2='망고')
test_kwargs(**info)
test_kwargs(info)
