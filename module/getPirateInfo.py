from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,WebDriverException
#from webdriver_manager.chrome import ChromeDriverManager


class PirateDataCrawler:
    def __init__(self):
        self.__service = Service('./driver/chromedriver.exe')
        # 크롬 웹드라이버 옵션 설정
        self.__options = Options()
        self.__options.add_argument('--headless')  # 브라우저를 띄우지 않고 실행하는 headless 옵션 적용
        self.__options.add_argument('--no-sandbox') # --no-sandbox 옵션 적용
        # 지역 데이터
        self.__country = {'Algeria': 'A001', 'Benin': 'A002', 'Congo': 'A003', 'Democratic Republic of Congo': 'A004', 'Egypt': 'A005', 'Ghana': 'A006', 'Guinea': 'A007', 'Gulf of Aden': 'D003', 'India': 'D002', 'Ivory Coast': 'A010', 'Kenya': 'A011', 'Mozambique': 'A012', 'Nigeria': 'A013', 'Red Sea': 'A014', 'Sierra Leone': 'A015', 'Somalia': 'A016', 'Tanzania': 'A017', 'The Congo': 'A018', 'Togo': 'A019', 'Gabon': 'A020', 'Liberia': 'A021', 'Cameroon': 'A022', 'Angola': 'A023', 'Brazil': 'B001', 'Colombia': 'B002', 'Costa Rica': 'B003', 'Ecuador': 'B004', 'Haiti': 'B005', 'Peru': 'B006', 'Dominican Republic': 'B007', 'Guyana': 'B008', 'Venezuela': 'B009', 'South China Sea': 'C001', 'Vietnam': 'C002', 'China': 'C003', 'Bangladesh': 'D001', 'Pakistan': 'D004', 'Indonesia': 'E001', 'Malacca Straits': 'E002', 'Malaysia': 'E003', 'Philippines': 'E004', 'Singapore Straits': 'E005', 'Thailand': 'E006', 'Iran': 'F001', 'Oman': 'F002', 'Papua New Guinea': 'F003', 'Yemen': 'F004'}

    def getPirateData(self,countryName):
        # 드라이버로 페이지 열기
        url = 'https://www.gicoms.go.kr/pirate/pirate_07.do'
        try:
            driver = webdriver.Chrome(service=self.__service, options=self.__options)
            # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=self.__options)
            driver.get(url)
            # "구역" select 태그 선택
            select_zone = Select(driver.find_element(By.NAME,'srcActSeaArea'))
            # "구역" select 태그에서 "현재 해역" 선택

            if countryName in self.__country.keys():
                value = self.__country[countryName]
                select_zone.select_by_value(value)
                # "1주일" radio 버튼 선택
                buttons = driver.find_elements(By.CSS_SELECTOR,'.inline_btn_group.recentlybtns > button')
                buttons[1].click() # 첫번째 버튼 클릭

                #"조회" 버튼 클릭
                driver.find_element(By.CSS_SELECTOR,'.form_footer.search_confirm > button').click()

                # 데이터 로딩 대기
                driver.implicitly_wait(7)

                # HTML 추출
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                
                # td 추출
                sea = [i.text for i in soup.find_all('td', class_='seawhere')]
                title = [tuple(i.text.split(' ')) for i in soup.find_all('td', class_='title')]
                data = [(idx+1,s,t[0],t[1]) for idx,(s,t) in enumerate(zip(sea,title))]
                # 값 반환
                return data
        except TimeoutException as te:
            print("시간 초과")
        except WebDriverException as we:
            print("웹 드라이버 오류")
    
if __name__ == "__main__":
    pdc =  PirateDataCrawler()
    a = pdc.getPirateData("Singapore Straits")
    print(a)