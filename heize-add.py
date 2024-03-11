#heize

def add(num1, num2):
    return num1 + num2

def main():
    print("더하기 계산기입니다.")
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))
    result = add(num1, num2)
    print("결과:", result)

if __name__ == "__main__":
    main()