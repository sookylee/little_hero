### 공고와 관련된 DB table(model)
* author : 게시글 작성자 (= 모집 기관)
* title : 공고 제목
* address_city : 봉사 주소 중 '시/도'에 해당 (ex. 서울특별시, 경기도 등)
* address_gu : 봉사 주소 중 '구'에 해당 (ex. 마포구)
* address_remainder : 시/도 와 구를 제외한 나머지 주소
* recruit_status : 모집중인지 아닌지의 여부. Boolean type. 모집중이면 true이며 default 값은 true임.
* text = 공고 내용
* created_date = 모집 시작일
* end_date = 모집 마감일 
* published_date : 본 공고 게재 날짜(없애도 됨)


더 필요하다고 생각되는 내용이 있으면 comment 바랍니다.
