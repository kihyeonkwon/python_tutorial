def my_function(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}인 키에 값 {value}가 저장이 되어있습니다.")


my_function(a="Real", b="Python", c="Is", d="Great", e="!")
