# 지콤스 해적 정보 API 서버

이 프로젝트는 Flask, BeautifulSoup4, Requests 등을 사용하여 현재 해역의 지콤스의 해적 정보를 스크래핑하는 API 서버를 구축하는 것을 목표로 합니다.

## 기능

- `/pirate-info` 엔드포인트에서 POST 요청을 받으면, 웹 페이지에서 지콤스의 해적 정보를 스크래핑합니다.
- 스크래핑한 데이터는 JSON 형식으로 반환됩니다.
- 서버는 Flask 웹 프레임워크와 Selenium WebDriver를 사용합니다.
- 데이터 추출 및 가공은 Beautiful-Soup으로 수행됩니다.


## 예시 응답
POST 요청을 보내면 다음과 같은 형식으로 JSON 응답이 반환됩니다:
```JSON
{
    "no" : 1,
    "나라" : "Peru",
    "날짜" : "2023-11-16",
    "사고유형" : "Boarded",
}
```