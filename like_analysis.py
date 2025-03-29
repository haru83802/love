import json
import os

# 데이터 파일 이름
DATA_FILE = "data.json"

# 데이터 불러오기 (없으면 빈 리스트 생성)
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

# 데이터 저장하기
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# 좋아할 가능성 계산
def calculate_affinity(data, person1, person2):
    score = 0
    total_entries = 0

    for entry in data:
        total_entries += 1
        # 두 사람이 함께 저장된 경우 점수 증가
        if {entry["name1"], entry["name2"]} == {person1["name"], person2["name"]}:
            score += 1

    # 데이터가 없으면 0% 반환
    if total_entries == 0:
        return 0

    # 점수를 백분율로 변환
    return min(100, int((score / total_entries) * 100))

# 메인 함수
def main():
    print("📊 좋아하는지 분석 프로그램")

    # 사용자 입력 받기
    name1 = input("첫 번째 사람의 이름: ")
    school1 = input("첫 번째 사람의 학교 이름: ")
    grade1 = input("첫 번째 사람의 학년: ")
    class1 = input("첫 번째 사람의 반: ")
    number1 = input("첫 번째 사람의 번호: ")

    name2 = input("두 번째 사람의 이름: ")
    school2 = input("두 번째 사람의 학교 이름: ")
    grade2 = input("두 번째 사람의 학년: ")
    class2 = input("두 번째 사람의 반: ")
    number2 = input("두 번째 사람의 번호: ")

    # 입력 데이터 객체 생성
    person1 = {"name": name1, "school": school1, "grade": grade1, "class": class1, "number": number1}
    person2 = {"name": name2, "school": school2, "grade": grade2, "class": class2, "number": number2}

    # 데이터 불러오기
    data = load_data()

    # 좋아할 가능성 계산
    affinity = calculate_affinity(data, person1, person2)
    print(f"\n📌 '{name1}'과(와) '{name2}'의 좋아할 가능성: {affinity}%")

    # 데이터 저장
    data.append({"name1": name1, "name2": name2, "school1": school1, "grade1": grade1, "class1": class1,
                 "school2": school2, "grade2": grade2, "class2": class2})
    save_data(data)

    print("✅ 데이터가 저장되었습니다!")

# 실행
if __name__ == "__main__":
    main()
