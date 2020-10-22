##kipris plus api를 활용한 유사상표명 데이터 수집

##1. rejectionDetailContents 로부터 유사 상표 등록번호 추출 및 등록번호 완성
상표 등록번호체계(출처:https://www.designmap.or.kr:10443/ipf/IpTrFrD.jsp?p=235)
2자리-7자리-4자리
앞의 2자리는 권리구분을 의미(상표는 40~47)
가운데 7자리는 심사 후 등록이 결정되어 등록료를 냄으로써 부여되는 일련번호
끝의 4자리는 일반적으로 숫자 '0000'이며, 생략도 가능



##2. 등록번호를 활용한 유사 상표 출원번호 수집
API item site address
http://plus.kipris.or.kr/portal/data/service/DBII_000000000000015/view.do?menuNo=200100&kppBCode=&kppMCode=&kppSCode=&subTab=SC001&entYn=N&clasKeyword=%eb%93%b1%eb%a1%9d%ec%a0%95%eb%b3%b4#soap_ADI_0000000000009942%20request%20url%20:%20http://plus.kipris.or.kr/openapi/rest/RegistrationService/

REST-1.등록사항

input : registrationNumber
output : applicationNumber

##3. 출원번호를 활용한 유사 상표명 수집
API item site address
http://plus.kipris.or.kr/portal/data/service/DBII_000000000000012/view.do?pageIndex=3&menuNo=200100&kppBCode=&kppMCode=&kppSCode=&subTab=SC001&entYn=N&clasKeyword=#soap_ADI_0000000000010092

REST-서지정보-4.서지요약정보

input : applicationNumber
output : TrademarkHangeulName, TrademarkEnglishsentenceName