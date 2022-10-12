from ctypes import sizeof
from re import L
from typing import Any
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import pandas as pd

PATH="C:\Program Files\Mozilla Firefox"



def get_member(BID):
        
    #--| Setup
    options = Options()
    options.add_argument("--headless")

    
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('permissions.default.stylesheet', 2)
    firefox_profile.set_preference('permissions.default.image', 2)
    firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')

    driver = webdriver.Firefox(firefox_profile=firefox_profile, options=options, service=FirefoxService(executable_path=GeckoDriverManager().install()))
    
    #----

    driver.get(f"https://www.parlamento.pt/DeputadoGP/Paginas/Biografia.aspx?BID={BID}")

    driver.implicitly_wait(0.5)

    try:
        member_name_element = driver.find_element(by=By.ID, value="ctl00_ctl50_g_5d3195b4_4c80_4cd5_a696_bf57c8c2232d_ctl00_ucNome_rptContent_ctl01_lblText")
        member_dob_element = driver.find_element(by=By.ID, value="ctl00_ctl50_g_5d3195b4_4c80_4cd5_a696_bf57c8c2232d_ctl00_ucDOB_rptContent_ctl01_lblText")
        member_legislature_element = driver.find_elements(by=By.CLASS_NAME, value="row.Border-Repeater")
    except:
        driver.quit()
        return 0

    member_info = [member_name_element.text, member_dob_element.text,
                         0,"","",
                         0,"","",
                         0,"","",
                         0,"","",
                         0,"","",
                         0,"","",
                         0,"","",
                         0,"","",
                         0,"","",
                         0,"","",
                         0,"","",
                         0,"","",
                         0,"","",
                         0,"","",
                         0,"","",
                         0,"",""]

    
    number_terms = len(member_legislature_element)


    for i in range(number_terms):
        member_term = member_legislature_element[i].text.split('\n')
        match member_term[0]:
            case "Cons":
                member_info[2] = 1
                member_info[3] = member_term[1]
                member_info[4] = member_term[2]
            case "I":
                member_info[5] = 1
                member_info[6] = member_term[1]
                member_info[7] = member_term[2]
            case "II":
                member_info[8] = 1
                member_info[9] = member_term[1]
                member_info[10] = member_term[2]
            case "III":
                member_info[11] = 1
                member_info[12] = member_term[1]
                member_info[13] = member_term[2]
            case "IV":
                member_info[14] = 1
                member_info[15] = member_term[1]
                member_info[16] = member_term[2]
            case "V":
                member_info[17] = 1
                member_info[18] = member_term[1]
                member_info[19] = member_term[2]
            case "VI":
                member_info[20] = 1
                member_info[21] = member_term[1]
                member_info[22] = member_term[2]
            case "VII":
                member_info[23] = 1
                member_info[24] = member_term[1]
                member_info[25] = member_term[2]
            case "VIII":
                member_info[26] = 1
                member_info[27] = member_term[1]
                member_info[28] = member_term[2]
            case "IX":
                member_info[29] = 1
                member_info[30] = member_term[1]
                member_info[31] = member_term[2]
            case "X":
                member_info[32] = 1
                member_info[33] = member_term[1]
                member_info[34] = member_term[2]
            case "XI":
                member_info[35] = 1
                member_info[36] = member_term[1]
                member_info[37] = member_term[2]
            case "XII":
                member_info[38] = 1
                member_info[39] = member_term[1]
                member_info[40] = member_term[2]
            case "XIII":
                member_info[41] = 1
                member_info[42] = member_term[1]
                member_info[43] = member_term[2]
            case "XIV":
                member_info[44] = 1
                member_info[45] = member_term[1]
                member_info[46] = member_term[2]
            case "XV":
                member_info[47] = 1
                member_info[48] = member_term[1]
                member_info[49] = member_term[2]

    driver.quit()

    print(member_info[0])    
    return member_info

    

members_df = pd.DataFrame(columns=["Name", "DOB", 
                                   "Cons", "Cons Party", "Cons Electoral District",
                                   "I", "I Party", "I Electoral District",
                                   "II", "II Party", "II Electoral District",
                                   "III", "III Party", "III Electoral District",
                                   "IV", "IVParty", "IV Electoral District",
                                   "V", "V Party", "V Electoral District",
                                   "VI", "VI Party", "VI Electoral District",
                                   "VII", "VII Party", "VII Electoral District",
                                   "VIII", "VIII Party", "VIII Electoral District",
                                   "IX", "IX Party", "IX Electoral District",
                                   "X", "X Party", "X Electoral District",
                                   "XI", "XI Party", "XI Electoral District",
                                   "XII", "XII Party", "XII Electoral District",
                                   "XIII", "XIII Party", "XIII Electoral District",
                                   "XIV", "XIV Party", "XIV Electoral District",
                                   "XV", "XV Party", "XV Electoral District"])


for i in range(20):
    l = get_member(i)
    if l!=0:
        members_df.loc[members_df.shape[0]] = l

print(members_df)

