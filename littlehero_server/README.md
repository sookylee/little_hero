현재 local 가상환경에서 실행해 본 파일입니다.<br>
## Before you use..
- pip install django
- pip install requests
- pip install bs4
- pip install djangorestframework
- (pip install django-filter) --추후 사용 예정


만약 venv 환경에서 설치 오류시 <br>
```
    'python -m pip install <pkg name>'
```
시도해 보세요.

### 공고와 관련된 DB table(model)
* **created_at** : (레코드 저장 시) 생성 시각
* **site_domain** : 1365인지 vms 인지. 1365면 1, vms면 2 값을 가짐. (다른 사이트가 추가될 것을 대비..) _db_utils.py에 enum 정의되어 있음.
* **regist_no** : 1365 no.
* **url** : 게시글 링크
* **title** : 공고 제목
* **address_city** : 봉사 주소 중 '시/도'에 해당 (ex. 서울특별시, 경기도 등)
* **address_gu** : 봉사 주소 중 '구'에 해당 (ex. 마포구)
* **address_remainder** : 시/도 와 구를 제외한 나머지 주소
* **recruit_status** : 모집중인지 아닌지의 여부. Boolean type. 모집중이면 true이며 default 값은 true임.
* **adult_status**: 성인인지 학생인지의 여부. 성인이면 true, 학생이면 false
* **telephone** : 모집기관 전화번호
* **domain**: 봉사 분야 (full text)
* **text** = 공고 내용
* **do_date** = 활동 기간
* **do_date_extra** = 활동 요일/시간 등의 세부 정보
* **recruit_company** = 기관명
* **recurit_member** = 모집 인원 수

## variable type
 - regist_no : big integer
 - site_domain : integer
 - recruit_satus, adult_status: boolean
 - else: String

<br>더 필요하다고 생각되는 내용이 있으면 언제든 SLACK ME!.



-*-*-
## To Do
 1. **해결!** ~~현재까지 완성된 크롤러는 1365 홈의 1번 페이지만 긁어오도록 되어 있음. 모든 페이지를 긁어오도록 수정해야 함.~~
 2. **해결!!** ~~http connection을 비롯한 error handling 필요. 하나도 안되어있음..ㅎ...~~
 3. AWS에 환경 설치해야 함. django는 Apache 쓴다던데 그것도 더 찾아봐야 함...
