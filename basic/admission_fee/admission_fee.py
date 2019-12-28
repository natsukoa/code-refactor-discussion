"""入場料.
- 子供（12歳未満）: 100円
- 大人（12歳以上）: 500円
- 学生: 300円
- 市民: 200円

条件
- 安いほうを適用する
"""


def calc_admission_fee(age, *, student=False, citizen=True):
    if age < 12:
        return 100
    if age >= 12:
        if student:
            if citizen:
                return 200
            else:
                return 300
        else:
            if citizen:
                return 200
            else:
                return 500


if __name__ == "__main__":
    print(calc_admission_fee(age=5))
    print(calc_admission_fee(15, student=True))
    print(calc_admission_fee(30))
    print(calc_admission_fee(30, citizen=False))
    print(calc_admission_fee(18, student=True, citizen=False))
