""" 2つの値の足し算と引き算の結果を表示する. """


def calc(num1, num2):
    result_add = num1 + num2
    result_sub = num1 - num2

    return result_add, result_sub


if __name__ == "__main__":
    add, sub = calc(10, 5)

    print(f"{add=}")
    print(f"{sub=}")

"""
1.
2値の足し算の結果を返す関数と引き算の結果を返す関数に分割しましょう

2.
分割した関数のテストを書きましょう
"""