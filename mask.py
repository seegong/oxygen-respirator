
import bs4
import json
import requests
import time

addr_neis = """https://open.neis.go.kr/hub/mealServiceDietInfo?Type=json&ATPT_OFCDC_SC_CODE=J10&SD_SCHUL_CODE=7530769&MLSV_YMD=%Y%m%d"""

def GOD_FEED_ME_PLZ() -> str:
    something_being_array_of_characters: str = time.strftime(addr_neis, time.localtime(time.time()))

    anything_received_from_neis_api = requests.get(url=something_being_array_of_characters, verify=False)

    if(anything_received_from_neis_api is None):
        return "급식정보를 가져올 수 없네요, 쉬는날인가봄 ㅇㅅㅇ"

    return anything_received_from_neis_api.text

def DO_YOU_LOVE_PARSING():

    what_ive_gotten_from_the_text = json.loads(GOD_FEED_ME_PLZ())

    # For whom would not be easily able to analyze this code, just follow the code, do not deny the reality ww, HAVE A GREAT TIME www
    some_text_thing_zz = what_ive_gotten_from_the_text['mealServiceDietInfo'][1]['row'][0]['DDISH_NM']

    the_text_which_has_to_be_filled: str = ''

    some_variable_to_count_and_iterate: int = 0

    # The departure of the STRING-PARSING's GREAT DEVIL KING, www
    while True:
        variable_that_stores_the_integer_value_of_first_korean_unicode: int = 0xAC00
        variable_which_has_the_last_korean_unicode_number: int = 0xD7A3

        if(some_variable_to_count_and_iterate is len(some_text_thing_zz)):
            break

        variable_which_is_orded: str = ord(some_text_thing_zz[some_variable_to_count_and_iterate])

        if(variable_which_is_orded >= variable_that_stores_the_integer_value_of_first_korean_unicode and variable_which_has_the_last_korean_unicode_number >= variable_which_is_orded):
            the_text_which_has_to_be_filled += chr(variable_which_is_orded)
        else:
            if(chr(variable_which_is_orded) == '>'):
                the_text_which_has_to_be_filled += '\n'
    
        some_variable_to_count_and_iterate += 1

    return the_text_which_has_to_be_filled

print(DO_YOU_LOVE_PARSING())