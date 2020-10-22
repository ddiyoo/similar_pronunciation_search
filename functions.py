import re
import urllib.request
import xmltodict, json

def extract_regiNum(strings):
    numbers = re.findall("\d+", strings)
    numbers = list(map(int, numbers)) ## convert type string->int
    return numbers

def collect_appliNum(registrationNum):
    appliNum_url =f"http://plus.kipris.or.kr/openapi/rest/RegistrationService/registrationInfo?registrationNumber={registrationNum}&accessKey={api_key}"
    response_appliNum = urllib.request.urlopen(appliNum_url)
    responseData_appliNum = response_appliNum.read()
    responseData_appliNum = xmltodict.parse(responseData_appliNum)
    responseData_appliNum = json.dumps(responseData_appliNum)
    responseData_appliNum = json.loads(responseData_appliNum)
    applicationNumber = responseData_appliNum['response']['body']['items']['registrationInfo']['registrationRightInfo']['applicationNumber']
    return applicationNumber

def collect_tradName(applicationNumber):
    name_url = f"http://plus.kipris.or.kr/openapi/rest/trademarkInfoSearchService/trademarkBiblioSummaryInfo?applicationNumber={applicationNumber}&accessKey={api_key}"
    response_name = urllib.request.urlopen(name_url)
    responseData_name = response_name.read()
    responseData_name = xmltodict.parse(responseData_name)
    responseData_name = json.dumps(responseData_name)
    responseData_name = json.loads(responseData_name)
    TrademarkHangeulName = responseData_name['response']['body']['items']['trademarkBiblioSummaryInfo']['TrademarkHangeulName']
    TrademarkEnglishsentenceName = responseData_name['response']['body']['items']['trademarkBiblioSummaryInfo'][
        'TrademarkEnglishsentenceName']

    return TrademarkHangeulName, TrademarkEnglishsentenceName

