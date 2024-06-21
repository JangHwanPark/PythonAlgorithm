import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import seaborn as sns

user_console = "user >> "

# Define the API endpoint and your API key for options
options_url = "https://kosis.kr/openapi/statisticsList.do"
options_params = {
    "method": "getList",
    "apiKey": "NDgwNDVlNjFjMTUyMTliNDQ2ZWZmNmFmY2NjMGVkNjI=",
    "vwCd": "MT_ZTITLE",
    "parentListId": "A",
    "format": "json",
    "jsonVD": "Y"
}

# Fetch options data from the API
response = requests.get(options_url, params=options_params)

# Check if the request was successful
if response.status_code == 200:
    try:
        options_data = response.json()
        options_df = pd.DataFrame(options_data)

        # Display available options
        print("사용 가능한 옵션:")
        for index, row in options_df.iterrows():
            print(f"{row['LIST_NM']}: {row['LIST_ID']}")

        # 사용자 입력 받기
        print("\n데이터셋 이름을 입력하세요.")
        user_input = input(user_console)

        # 입력에 따라 LIST_ID 찾기
        parentListId = None
        for index, row in options_df.iterrows():
            if row['LIST_NM'] == user_input:
                parentListId = row['LIST_ID']
                break

        if parentListId is None:
            print("잘못된 입력입니다. 올바른 데이터셋 이름을 입력하세요.")
        else:
            # Define the API endpoint and your API key for the data fetch
            url = "https://kosis.kr/openapi/statisticsList.do"

            params = {
                "method": "getList",
                "apiKey": "",
                "vwCd": "MT_ZTITLE",
                "parentListId": parentListId,
                "format": "json",
                "jsonVD": "Y"
            }

            # Fetch data from the API
            response = requests.get(url, params=params)

            # Check if the request was successful
            if response.status_code == 200:
                try:
                    data = response.json()
                    df = pd.DataFrame(data)

                    while True:
                        # 메뉴 출력
                        print("\n메뉴:")
                        print("1. 데이터셋 저장")
                        print("2. 데이터셋 수치 분석 및 시각화")
                        print("3. 종료")
                        print("\n원하는 작업을 선택하세요.")
                        user_input = int(input(user_console))

                        if user_input == 1:
                            # 데이터셋 저장
                            data_set = ["csv", "json", "xlsx"]
                            print("\n원하는 데이터 형식을 입력하세요.")
                            for i in range(len(data_set)):
                                print(f"{i + 1}. {data_set[i]}")
                            user_input = int(input(user_console))
                            save_url = "./data/kosis_demographics"

                            while True:
                                if user_input == 1:
                                    df.to_csv(f"{save_url}.csv", index=False)
                                    print(f"데이터가 {save_url}.csv 에 저장되었습니다.")
                                    break
                                elif user_input == 2:
                                    df.to_json(f"{save_url}.json", index=False)
                                    print(f"데이터가 {save_url}.json 에 저장되었습니다.")
                                    break
                                elif user_input == 3:
                                    df.to_excel(f"{save_url}.xlsx", index=False)
                                    print(f"데이터가 {save_url}.xlsx 에 저장되었습니다.")
                                    break
                                else:
                                    print("없는 형식입니다. 다시 입력하세요.")
                                    user_input = int(input(user_console))
                        elif user_input == 2:
                            # 데이터셋 수치 분석 및 시각화
                            np_data = df.to_numpy()
                            print("\n넘파이 배열을 사용한 분석 결과:")
                            print(f"데이터의 전체 개수: {np_data.size}")
                            print(f"데이터의 차원: {np_data.shape}")

                            if 'value' in df.columns:
                                numerical_data = df['value'].to_numpy()
                                print(f"평균값: {np.mean(numerical_data)}")
                                print(f"최대값: {np.max(numerical_data)}")
                                print(f"최소값: {np.min(numerical_data)}")

                                # 시각화
                                plt.figure(figsize=(10, 6))
                                sns.histplot(numerical_data, kde=True)
                                plt.title("Value Distribution")
                                plt.xlabel("Value")
                                plt.ylabel("Frequency")
                                plt.show()

                                plt.figure(figsize=(10, 6))
                                sns.boxplot(data=numerical_data)
                                plt.title("Value Boxplot")
                                plt.xlabel("Value")
                                plt.show()
                            else:
                                print("수치형 데이터가 포함된 컬럼이 없습니다.")
                        elif user_input == 3:
                            # 종료
                            print("프로그램을 종료합니다.")
                            break
                        else:
                            print("잘못된 입력입니다. 다시 선택하세요.")
                except ValueError as e:
                    print("JSON 파싱 오류:", e)
            else:
                print("데이터를 가져오지 못했습니다. 상태 코드:", response.status_code)
                print("응답 내용:", response.text)
    except ValueError as e:
        print("옵션 데이터 JSON 파싱 오류:", e)
else:
    print("옵션 데이터를 가져오지 못했습니다. 상태 코드:", response.status_code)
    print("응답 내용:", response.text)