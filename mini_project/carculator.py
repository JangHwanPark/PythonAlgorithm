subject = [
    "c",
    "파이썬",
    "자바",
    "자바스크립트",
    "컴퓨터개론",
    "소프트웨어 공학",
    "컴퓨터 구조"
]

menu = [
    "학생 이름 및 성적 입력",
    "학생별 평균 성적 계산",
    "과목별 평균 성적 계산",
    "학생별 평균 성적 석차",
    "학생 정보 조회",
    "종료"
]

information = []
user_console = "user >> "

while True:
    print("=" * 7 + " 프로그램을 시작합니다." + "=" * 7)
    print("원하는 메뉴를 선택해 주세요.")
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")

    print("=" * 35)
    user_input = int(input(user_console))

    # 학생 정보 및 점수 등록
    if user_input == 1:
        print("\n" + "=" * 10 + " 학생 정보 및 점수 등록" + "=" * 10)
        print("학생 이름을 입력해 주세요")
        user_name = input(user_console)

        # 중복 검사
        exists = False
        for user in information:
            if user["name"] == user_name:
                exists = True
                break

        if not exists:
            user_info = {"name": user_name, "sbj_score": {}, "avg_score": 0.0}
            total_score = 0
            for j in range(len(subject)):
                print(f"{subject[j]} 과목의 점수를 입력해 주세요")
                user_score = int(input(user_console))

                user_info["sbj_score"][subject[j]] = user_score
                total_score += user_score

            # 평균 점수 계산
            user_info["avg_score"] = total_score / len(subject)
            information.append(user_info)
            print(f"{user_name} 학생의 정보와 점수가 등록되었습니다.\n")
        else:
            print(f"{user_name}은 이미 등록된 학생입니다.\n")

    # 학생별 평균 계산
    elif user_input == 2:
        print("=" * 10 + " 학생별 평균 성적 " + "=" * 10)
        for user in information:
            print(f"{user['name']} 학생의 평균 성적: {user['avg_score']:.2f}")
        print('\n')

    # 과목별 평균 계산
    elif user_input == 3:
        print("=" * 10 + " 과목별 평균 성적 " + "=" * 10)
        subject_avg = {subj: 0.0 for subj in subject}
        for subj in subject:
            total = 0

            for user in information:
                total += user["sbj_score"].get(subj, 0)
            subject_avg[subj] = total / len(information)
            print(f"{subj}의 평균 성적: {subject_avg[subj]:.2f}")
        print("\n")

    # 학생별 평균 성적 석차 내림차순
    elif user_input == 4:
        print("=" * 10 + " 학생별 평균 성적 (내림차순) " + "=" * 10)
        information.sort(key=lambda x: x["avg_score"], reverse=True)

        rank = 1
        for user in information:
            print(f"{rank}등: {user['name']} - 평균 성적: {user['avg_score']:.2f}")
            rank += 1
        print("\n")

    # 등록된 학생 정보 조회
    elif user_input == 5:
        print("=" * 10 + " 정보 조회 " + "=" * 10)
        user_name = input(user_console)

        user_data = None
        for user in information:
            if user["name"] == user_name:
                user_data = user
                break

        if user_data:
            print(f"이름: {user_data['name']}")
            for sbj in user_data["sbj_score"]:
                print(f"{sbj} 점수: {user_data['sbj_score'][sbj]}")
            print(f"평균 점수: {user_data['avg_score']:.2f}\n")
        else:
            print(f"{user_name} 학생이 존재하지 않습니다.\n")

    # 프로그램 종료
    elif user_input == 6:
        print("=" * 10 + " 프로그램을 종료합니다." + "=" * 10)
        break

    # 잘못된 입력 처리
    else:
        print("입력한 메뉴가 존재하지 않습니다. 다시 입력해주세요.\n")