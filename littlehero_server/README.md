## Before you use..
- pip install django
- pip install requests
- pip install bs4
- pip install djangorestframework
- pip install django-filter
현재 local 가상환경에서 실행해 본 파일입니다.
만약 venv 환경에서 설치 오류시 
    'python -m pip install <pkg name>'
로 시도해 보세요.

### 공고와 관련된 DB table(model)
* created_at : (레코드 저장 시) 생성 시각
* regist_no : 1365 no.
* url : 게시글 링크
* title : 공고 제목
* address_city : 봉사 주소 중 '시/도'에 해당 (ex. 서울특별시, 경기도 등)
* address_gu : 봉사 주소 중 '구'에 해당 (ex. 마포구)
* address_remainder : 시/도 와 구를 제외한 나머지 주소
* recruit_status : 모집중인지 아닌지의 여부. Boolean type. 모집중이면 true이며 default 값은 true임.
* adult_status: 학생/성인/노인 등의 구분
* telephone : 모집기관 전화번호
* domain: 봉사 분야 (full text)
* text = 공고 내용
* do_date = 활동 기간
* do_time = 활동 시간
* do_week = 활동 요일
* recruit_date = 모집 기간
* recruit_company = 기관명
* recurit_member = 모집 인원 수

### variable type
 - regist_no : big integer
 - recruit_satus: boolean
 - else: String

더 필요하다고 생각되는 내용이 있으면 comment 바랍니다.




## To Do
1. 현재까지 완성된 크롤러는 1365 홈의 1번 페이지만 긁어오도록 되어 있음. 모든 페이지를 긁어오도록 수정해야 함.
2. http connection을 비롯한 error handling 필요. 하나도 안되어있음..ㅎ...
3. AWS에 환경 설치해야 함. django는 Apache 쓴다던데 그것도 더 찾아봐야 함...
