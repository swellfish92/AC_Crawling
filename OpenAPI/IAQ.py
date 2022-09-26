# 아래에 해당하는 공기질 및 환경정보를 OpenAPI로 불러오는 코드들

# 인천국제공항공사_실내대기질 정보
# https://www.data.go.kr/data/15095049/openapi.do
# 서울시 지하철역사내 실내공기질 정보(시간단위)
# https://data.seoul.go.kr/dataList/OA-15495/A/1/datasetView.do
# 부산광역시_실내공기질 실시간 측정 자료
# https://www.data.go.kr/data/3056201/openapi.do
# 인천광역시서구시설관리공단_실시간 실내공기질 측정 데이터 조회 서비스
# https://www.data.go.kr/data/15096392/openapi.do
# 한국환경공단_다중이용시설 실내공기질 자동측정망 실시간정보
# https://www.data.go.kr/data/15038044/openapi.do
# 역사별 습도 정보
# https://data.kric.go.kr/rips/M_01_02/detail.do;jsessionid=nrJZ4DBQcYGx8JWPf71xOT3T?id=195&service=convenientInfo&operation=stationHumidity&page=4
# 역사별 공기질 측정 정보
# https://data.kric.go.kr/rips/M_01_02/detail.do;jsessionid=nrJZ4DBQcYGx8JWPf71xOT3T?id=193&service=convenientInfo&operation=stationAirQuality&page=4
# 한국공항공사_실시간 공항 소음측정 정보
# https://www.data.go.kr/data/15085847/openapi.do#tab_layer_prcuse_exam
# 역사별 소음도 정보
# https://data.kric.go.kr/rips/M_01_02/detail.do;jsessionid=nrJZ4DBQcYGx8JWPf71xOT3T?id=196&service=convenientInfo&operation=stationNoiseLevel&page=4

# 키는 각각의 함수 안에 넣어 두기로 함 (일괄 처리할 경우 변수명이 복잡함... 개별로 확인할 것!
# 응답을 돌려주는 데까지만 짬. 뭘 쓸 지는 나중에 보고나서 확인

import requests
import json
import xmltodict
# ssl 에러로 인해 추가한 부분 (_ssl.c:1123)
# https://koreapy.tistory.com/1444

# 인천국제공항공사_실내대기질 정보
def get_incheon_airport_iaq():
    key = 'owsao31Eak4pE2i8SQkuu6bVXieWxILomFCxifqPQAW4wgbkVJ%2F9X0hIzljulAYMV6KcUZPLla2xAUusk4B1wg%3D%3D'
    url = 'https://apis.data.go.kr/B551177/IndoorAirQualityInfo/getIndoorAirQuality?serviceKey='+key+'&type=json'
    print(url)
    result = requests.get(url, verify=False)
    jsonresult = json.loads(result.text)
    return jsonresult['response']['body']

# 서울시 지하철역사내 실내공기질 정보(시간단위)
# 253개 역사라고 했는데, 240개밖에 안 나옴. (2022.09.26 기준). 어쩄든 넉넉하게 300개까지 전부 불러오게 해 뒀음.
def get_seoul_subway_iaq(numOfRows=999, type='json'):
    key = '51716a4673737765343651706f7152'
    url = 'http://openapi.seoul.go.kr:8088/' + key + '/xml/airPolutionInfo/1/300/TYPE=json'
    result = requests.get(url, verify=False)
    print(result.text)
    jsonresult = xmltodict.parse(result.text)
    return jsonresult

# 부산광역시_실내공기질 실시간 측정 자료
def get_busan_subway_iaq(datehour, location_code):
    key = 'owsao31Eak4pE2i8SQkuu6bVXieWxILomFCxifqPQAW4wgbkVJ%2F9X0hIzljulAYMV6KcUZPLla2xAUusk4B1wg%3D%3D'
    url = 'http://apis.data.go.kr/6260000/IndoorAirQuality/getIndoorAirQualityByStation?serviceKey=' + key + '&pageNo=1&numOfRows=999&resultType=json&controlnumber=' + str(datehour) + '&areaIndex=' + str(location_code)
    result = requests.get(url, verify=False)
    jsonresult = xmltodict.parse(result.text)
    return jsonresult

    # datehour는 yyyymmddhh임 (ex-2022092410)
    # 추가. location_code는 내부에 존재하는 코드체계로, 아래와 같이 구분됨
    # 서면역1호선승강장	201193
    # 서면역2호선대합실	202191
    # 서면역2호선승강장	202192
    # 사상역대합실	202271
    # 수영역대합실	203011
    # 연산역대합실	203051
    # 미남역대합실	203091
    # 덕천역대합실	203131
    # 동래역4호선대합실	204021
    # 남포역대합실	201111
    # 서면역1호선대합실	201191


# 인천광역시서구시설관리공단_실시간 실내공기질 측정 데이터 조회 서비스
def get_incheon_facility_iaq():
    key = 'owsao31Eak4pE2i8SQkuu6bVXieWxILomFCxifqPQAW4wgbkVJ%2F9X0hIzljulAYMV6KcUZPLla2xAUusk4B1wg%3D%3D'
    url = 'http://apis.data.go.kr/B551296/SeoguIaqSvc/getSeoguIaqRtData?serviceKey=' + key + '&pageNo=1&numOfRows=999'
    print(url)
    result = requests.get(url, verify=False)
    jsonresult = xmltodict.parse(result.text)
    return jsonresult

# 한국환경공단_다중이용시설 실내공기질 자동측정망 실시간정보
def get_korea_facility_iaq(date):
    key = 'owsao31Eak4pE2i8SQkuu6bVXieWxILomFCxifqPQAW4wgbkVJ%2F9X0hIzljulAYMV6KcUZPLla2xAUusk4B1wg%3D%3D'
    url = 'http://apis.data.go.kr/B552584/InairQualityMonitoringService01/getInairHourData01?date='+ str(date) + '&serviceKey=' + key
    print(url)
    result = requests.get(url, verify=False)
    jsonresult = xmltodict.parse(result.text)
    return jsonresult

    # datehour는 yyyymmdd임 (ex-20220924)

# 한국공항공사_실시간 공항 소음측정 정보
# https://www.data.go.kr/data/15085847/openapi.do#tab_layer_prcuse_exam
def get_korea_facility_iaq():
    key = 'owsao31Eak4pE2i8SQkuu6bVXieWxILomFCxifqPQAW4wgbkVJ/9X0hIzljulAYMV6KcUZPLla2xAUusk4B1wg=='
    url = 'https://api.odcloud.kr/api/getNoiseMeasureRT/v1/noiseMeasureRT?perPage=999&serviceKey=' + key
    print(url)
    result = requests.get(url, verify=False)
    jsonresult = json.loads(result.text)
    return jsonresult

    # datehour는 yyyymmdd임 (ex-20220924)

print(get_korea_facility_iaq())

# 역사별 정보는 승인-허가가 자동이 아닌 것으로 보임. 일단 3개(습도/공기질/소음도)는 다 신청해놓고 대기를 기다리는 중.
