SPEICES_OF_ANIMAL = (
        ("개/강아지", "개/강아지"),
        ("고양이", "고양이"),
        ("토끼", "토끼"),
        ("소동물","소동물"),
        ("파충류","파충류"),
    )

NUMBER_OF_ANIMAL = (
        (1, "1마리"),
        (2, "2마리"),
        (3, "3마리 이상"),
    )
    
SEX_OF_ANIMAL = (
    ("암컷", "암컷"),
    ("수컷", "수컷"),
    )

GENDER = (
    ("여성", "여성"),
    ("남성", "남성"),
    )

DWELLING = (
    ("apart", "아파트"),
    ("villa", "빌라"),
    ("house", "주택"),
    ("office_hotel", "오피스텔"),
    ("etc", "기타"),
    )
    
HAS_YARD = (
    (True, "마당 있음"),
    (False, "마당 없음"),
    )
    

RATE = (
    (i, i) for i in range(1,11)
    )
    
CONTACT_STATUS = (
    ("cancel", "취소"),
    ("wait", "확인 대기중"),
    ("reserve", "결제 완료"),
    ("progress", "시팅 중"),
    ("complete", "시팅 완료"),
    ("end", "리뷰 완료")
    )
    

ADDRESS = ('서울특별시 성북구 정릉로10길 17',
'서울 성북구 정릉동 1020-2',
'서울 강북구 미아동 438',
'서울 서대문구 홍은동 산 1-45',
'서울특별시 성북구 성북동 330-4',
'서울 중구 수표동 65-4',
'서울 중구 다동 88',
'서울 중구 필동1가 3-7',
'서울 용산구 효창동 260',
'서울 성동구 금호동3가 1344-103',
'서울 광진구 자양동 10-37',
'서울 강남구 역삼동 699-27',
'서울 강남구 논현동 279-177',
'서울 영등포구 여의도동 15-21',
'서울 강서구 마곡동 727-1247',
'서울 양천구 목동 542',
'서울 은평구 녹번동 133-8',
'서울 서대문구 연희동 69-4',
'서울 강서구 화곡동 362-188',
'서울 구로구 구로동 547-11',
'서울 구로구 항동 79',
'서울 관악구 신림동 612-28',
'서울 동대문구 용두동 237-11',
'경기 부천시 소사구 소사본동 180-7',
'경기 안양시 만안구 석수동 산 11-1',
'경기 성남시 중원구 갈현동 368-3',
'경기 수원시 장안구 파장동 산 12-1')