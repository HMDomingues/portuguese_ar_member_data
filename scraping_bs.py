from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt


def get_member(BID):
    
    try:
        URL = f"https://www.parlamento.pt/DeputadoGP/Paginas/Biografia.aspx?BID={BID}"
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")
    except:
        print("Connection not established")
        return 0


    try:
        member_name_element = soup.find(id="ctl00_ctl50_g_5d3195b4_4c80_4cd5_a696_bf57c8c2232d_ctl00_ucNome_rptContent_ctl01_lblText")
        member_dob_element = soup.find(id="ctl00_ctl50_g_5d3195b4_4c80_4cd5_a696_bf57c8c2232d_ctl00_ucDOB_rptContent_ctl01_lblText")
        member_legislature_element = soup.find_all(class_="row Border-Repeater")
    except:
        return 0
    if member_name_element == None:
        return 0

    try:
        member_info = [member_name_element.get_text(), member_dob_element.get_text(),
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
    except:
        member_info = [member_name_element.get_text(), "",
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
        member_term = member_legislature_element[i].get_text().split('\n')
        match member_term[1]:
            case "Cons":
                member_info[2] = 1
                member_info[3] = member_term[2]
                member_info[4] = member_term[3]
            case "I":
                member_info[5] = 1
                member_info[6] = member_term[2]
                member_info[7] = member_term[3]
            case "II":
                member_info[8] = 1
                member_info[9] = member_term[2]
                member_info[10] = member_term[3]
            case "III":
                member_info[11] = 1
                member_info[12] = member_term[2]
                member_info[13] = member_term[3]
            case "IV":
                member_info[14] = 1
                member_info[15] = member_term[2]
                member_info[16] = member_term[3]
            case "V":
                member_info[17] = 1
                member_info[18] = member_term[2]
                member_info[19] = member_term[3]
            case "VI":
                member_info[20] = 1
                member_info[21] = member_term[2]
                member_info[22] = member_term[3]
            case "VII":
                member_info[23] = 1
                member_info[24] = member_term[2]
                member_info[25] = member_term[3]
            case "VIII":
                member_info[26] = 1
                member_info[27] = member_term[2]
                member_info[28] = member_term[3]
            case "IX":
                member_info[29] = 1
                member_info[30] = member_term[2]
                member_info[31] = member_term[3]
            case "X":
                member_info[32] = 1
                member_info[33] = member_term[2]
                member_info[34] = member_term[3]
            case "XI":
                member_info[35] = 1
                member_info[36] = member_term[2]
                member_info[37] = member_term[3]
            case "XII":
                member_info[38] = 1
                member_info[39] = member_term[2]
                member_info[40] = member_term[3]
            case "XIII":
                member_info[41] = 1
                member_info[42] = member_term[2]
                member_info[43] = member_term[3]
            case "XIV":
                member_info[44] = 1
                member_info[45] = member_term[2]
                member_info[46] = member_term[3]
            case "XV":
                member_info[47] = 1
                member_info[48] = member_term[2]
                member_info[49] = member_term[3]

    print(member_info[0])    
    return member_info

    

members_df = pd.DataFrame(columns=["Name", "DOB", 
                                   "Cons", "Cons Party", "Cons Electoral District",
                                   "I", "I Party", "I Electoral District",
                                   "II", "II Party", "II Electoral District",
                                   "III", "III Party", "III Electoral District",
                                   "IV", "IV Party", "IV Electoral District",
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


for i in range(7500):
    l = get_member(i)
    if l!=0:
        members_df.loc[members_df.shape[0]] = l
    if i % 50 == 0:
        print (f"At {i}")

print(members_df)

members_df.to_csv("C:\\Users\\hugom\\Data Frolicking\\portuguese_ar_member_data\\portuguese_ar_member_data\\outputs\\members.csv", index=False)