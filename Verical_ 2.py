import requests
import os.path
from datetime import datetime
import time
import datetime
import pandas as pd
global df1
df1 = pd.DataFrame({'mpn': pd.Series(dtype='str'),
                    'manufacturerName': pd.Series(dtype='str'),
                   'eccnCode': pd.Series(dtype='str'),
                    'exceedsSVHC': pd.Series(dtype='str'),
                    'hazmatFlag': pd.Series(dtype='str'),
                    'includesSVHC': pd.Series(dtype='str'),
                    'lowestPrice': pd.Series(dtype='str'),
                    'manufacturerCode': pd.Series(dtype='str'),
                   'manufacturerId': pd.Series(dtype='str'),
                    'manufacturerImageUrl': pd.Series(dtype='str'),
                    'militaryFlag': pd.Series(dtype='str'),
                    'originalDataSheetUrl': pd.Series(dtype='str'),
                    'partCategoryId': pd.Series(dtype='str'),
                    'partCategoryUnique': pd.Series(dtype='str'),
                   'partDescription': pd.Series(dtype='str'),
                    'partId': pd.Series(dtype='str'),
                    'quantity': pd.Series(dtype='str'),
                    'rohsCompliant': pd.Series(dtype='str'),
                    'searchableMpn': pd.Series(dtype='str'),
                    'specSource': pd.Series(dtype='str'),
                   'weight': pd.Series(dtype='str')})
global file_name
file_name=datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p") + '.csv'
df1.to_csv(file_name, mode='a', index=False)
def write(l, df1):
    if (os.path.exists(file_name) == True):
        df2 = df1.head(0).copy()
        df2.loc[0] = l
        df2.to_csv(file_name, mode='a', index=False, header=False)
    else:
        df1 = pd.DataFrame({'mpn': pd.Series(dtype='str'),
                    'manufacturerName': pd.Series(dtype='str'),
                   'eccnCode': pd.Series(dtype='str'),
                    'exceedsSVHC': pd.Series(dtype='str'),
                    'hazmatFlag': pd.Series(dtype='str'),
                    'includesSVHC': pd.Series(dtype='str'),
                    'lowestPrice': pd.Series(dtype='str'),
                    'manufacturerCode': pd.Series(dtype='str'),
                   'manufacturerId': pd.Series(dtype='str'),
                    'manufacturerImageUrl': pd.Series(dtype='str'),
                    'militaryFlag': pd.Series(dtype='str'),
                    'originalDataSheetUrl': pd.Series(dtype='str'),
                    'partCategoryId': pd.Series(dtype='str'),
                    'partCategoryUnique': pd.Series(dtype='str'),
                   'partDescription': pd.Series(dtype='str'),
                    'partId': pd.Series(dtype='str'),
                    'quantity': pd.Series(dtype='str'),
                    'rohsCompliant': pd.Series(dtype='str'),
                    'searchableMpn': pd.Series(dtype='str'),
                    'specSource': pd.Series(dtype='str'),
                   'weight': pd.Series(dtype='str')})
        df1.to_csv(file_name, index=False, header=True)
        df2 = df1.head(0).copy()
        df2.loc[0] = l
        df2.to_csv(file_name, mode='a', index=False, header=False)
cookies = {
    'liveagent_oref': 'https://www.google.com/',
    'fidelius': '8464dfdc-0b64-4575-86e3-1a38ee1b1eeb',
    'alohomora': '93bf0503-ba6d-465d-85d9-88b09046648f',
    'AMCV_90241DD164F13A460A495C3A%40AdobeOrg': 'MCMID|45218505429704241083069688084999301691',
    'liveagent_ptid': 'ff372037-1636-43f6-8ffd-a64a79d97445',
    '__qca': 'P0-1337655814-1724826248588',
    'dfp': '6ef4506393ae4cd8d636a28355eea161',
    '_gcl_au': '1.1.962558814.1734245938',
    'SERVERID': '.30-81',
    'liveagent_sid': '3739d776-b35a-4e05-b3ea-6a6d9e395037',
    'liveagent_vc': '6',
    'bm_s': 'YAAQBDwSAjX9HrmTAQAAZi0bRgISgwjY+eCZDy5N4U9TJtFfgbjs/sOOuvOmre+OXbrR7VY9T6SvgC0ERWmW4Sif/f1Il8rY/7PIvGeRqhI1WPUI8KVnVtizy0nge5h30vKAgZSviZn9xavpjSLd6QnhFGLNn+/cEYavE33Ro3Ni41bYVFhJB1iDRx+eHe5x0PgeGQKm9kjSncmLSYzFTLOo+0WAuPAxte6Vf9P3mkqD2AZ7Lj1x4BvjPO1E8pN5ZFHYdEjPlgU62BYLzSKtyJCf2PYRWtRgG7tNQDweSLfMMFh6wawm7l0ov5StSAJ/4+NMfs0mrZTwKYknDuXpAT7kipXgu7w=',
    'bm_so': '814F4CB2F5214C1F9D9977B805F9ABA2DD8008BA1C2ED39B1AA9D74C6711B40E~YAAQBDwSAjb9HrmTAQAAZi0bRgLTdipeTfGP7cyYfXCdnLyUNlhPFbBCeo8XclpCh0Gv8/XYwxGi9oncf6jsLq3LDrCt8HL6xSxiEavJeKDtE/D5V2GYdxx68uDp/VR77m6vpEBDCa6I4ZpMqa/YCzbYyuMsa5x7I/R3Moc/yUIQdBVzqSpQjiwRe5VgCGjWwRPATKg1zeELtkHgAy8+x0TfjsdJlABnZ981PruZC1As6DujCLknMV+Jx2++4KLDmbDBDJFp16USQEd19OQ0VlYhykbh/Yk2UwJOWQxEK7cjJ1xAAsoXT5Y099rIJ9X8osIlZYDu+Uk4AifFYA83tikiANJVM3c/ilPIODpJY5IbMXWO9Jt9DgxwvCZuYe1TlXUiWKpVMBbrm9KihP/T4vsUNyeJZo0AAsP/JLQvfkGDbo9QIl/s9ZyTZ7174j+bczCOUsgUz8eaHNCfTyk=',
    '_gid': 'GA1.2.1116597753.1736342976',
    'kndctr_90241DD164F13A460A495C3A_AdobeOrg_identity': 'CiY0NTIxODUwNTQyOTcwNDI0MTA4MzA2OTY4ODA4NDk5OTMwMTY5MVIRCK--n72ZMhgBKgRJUkwxMAHwAeP57LDEMg==',
    'bm_lso': '814F4CB2F5214C1F9D9977B805F9ABA2DD8008BA1C2ED39B1AA9D74C6711B40E~YAAQBDwSAjb9HrmTAQAAZi0bRgLTdipeTfGP7cyYfXCdnLyUNlhPFbBCeo8XclpCh0Gv8/XYwxGi9oncf6jsLq3LDrCt8HL6xSxiEavJeKDtE/D5V2GYdxx68uDp/VR77m6vpEBDCa6I4ZpMqa/YCzbYyuMsa5x7I/R3Moc/yUIQdBVzqSpQjiwRe5VgCGjWwRPATKg1zeELtkHgAy8+x0TfjsdJlABnZ981PruZC1As6DujCLknMV+Jx2++4KLDmbDBDJFp16USQEd19OQ0VlYhykbh/Yk2UwJOWQxEK7cjJ1xAAsoXT5Y099rIJ9X8osIlZYDu+Uk4AifFYA83tikiANJVM3c/ilPIODpJY5IbMXWO9Jt9DgxwvCZuYe1TlXUiWKpVMBbrm9KihP/T4vsUNyeJZo0AAsP/JLQvfkGDbo9QIl/s9ZyTZ7174j+bczCOUsgUz8eaHNCfTyk=^1736343011158',
    '_uetsid': '9b91b760cdc411efa2a0b1ed3e1af70b',
    '_uetvid': '22d62ca0650611ef9df4d5a14ab83cbc',
    '_ga': 'GA1.1.397335291.1735816166',
    '_ga_GQQZK61FEJ': 'GS1.1.1736342977.2.1.1736343097.0.0.0',
    '_ga_WJ42GVMDR9': 'GS1.1.1736342977.1.1.1736343794.0.0.0',
    '_ga_ZC3EBH21E8': 'GS1.1.1736342978.1.1.1736343794.0.0.0',
    'JSESSIONID': 'A11B1848B327DB4100246EB29EAF9566',
    '_abck': '1557D472902CE177726A12A0991E5C08~0~YAAQuF6MT9aQy6uTAQAAvDbDSQ2s02K3LoaIFOyMGEt9pYRT4QpNHglcnz2a4ZPelkalNnSQ+pReMxrpd6UxjB6D2GYAk4GUWNryHCYeWhcqEN2nGeDwyqGsD7IVmF6rARLE1g/yA9P05gdBlyinvPTZs3/sdUKGOVkcaBHggudNqT81irJ0d4216Bmb3TCa5A10ADaIH0sb9SgqYxOtjc6rQFWxh+fpVmDOebDKlsEGvFHeH/nkD7AMgDJxfPMBaV+Bn1nXi6gOjIsFnY/oS6Jdz680wnAol1UfwcjsigZbQwROk50bnafZ1GhjJLNgzWhotmLR9/i4Fc5zyCvGgWZZ/3MCppFIcTrrvvWcrpl1PBSWx35cupAdYMsc7fV/V0V8KvYIjU1vrV258CcwiKZymmR9DnDHcelFQZ9dsIqwLDbYwL9DkmA/cICZ/L/NiVdJK3FMwcSy6qn+C6AN2plyD5/yYJsmq7qZAZMaOrlgRgrKr02AKG5vbn1MZC61RD4wiQjm8WEXPI5RLui+TygEAm/kretxOQ3jWKetENS9Ip4UPnQ4uHYiP4i3CeqbVueQpBgBoVi3ky+/a735TsSS/qTtw3yLmDiLGCFT7RKZ1KCH7jOGqsGxVWt7+A==~-1~-1~-1',
    'ak_bmsc': '0CCC3AF8A078E2616AD4424C02392258~000000000000000000000000000000~YAAQuF6MT9eQy6uTAQAAvDbDSRpThxfOhrnJ3xsHXfebp2FdH+S05DZWXUrWY74eLTwVo4rnjYBaiocQGtrhbWBHiDL+prVRuZw/EjR5GRsDoe08m7DuHKzKMOJLEVqwdP+PZ1lOhCrYgQ7yiPjWi9hN7KaN5EtPJA7Q5Rxx+b9SexxZMVNLT+RJN2gfLBiiS1Z9wqE+D4QEZUCHK2vdA5E5G7thCxoXdOLayFOC+fSMWIUbQV+bipzY7mLIGEBFZSG9AzRworCaMxZ6qA6GZXepJbfGjrFQgrD/IvW4Nqzyvjtud0nqflziKTxwJrQAGXiDzrOBAWL0bfiD+DjdquNNVwfIF4yjja09NJor3FtVE0U+Vw2wvaarMapVjFRcBb+aT5ULp77hW8jO',
    '_gat_coreTracker': '1',
}

headers = {
        'authority': 'www.verical.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'dfp': '6512826d0bfd42def94a6a460d885c61',
        'expires': 'Sat, 01 Jan 2000 00:00:00 GMT',
        'if-modified-since': '0',
        'origin': 'https://www.verical.com',
        'pragma': 'no-cache',
        'referer': 'https://www.verical.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

params = {
    'format': 'json',
}

json_data = {
    'parameters': [
        {
            'key': 'search_term',
            'values': [
                '*',
            ],
        },
        {
            'key': 'part_category_id',
            'values': [
                776,
            ],
        },
        {
            'key': 'start_index',
            'values': [
                0,
            ],
        },
        {
            'key': 'quantity_min',
            'values': [
                0,
            ],
        },
    ],
}

response = requests.post(
    'https://www.verical.com/server-webapp/api/rest/search/parametric',
    params=params,
    #cookies=cookies,
    headers=headers,
    json=json_data,
)
data=response.json()
if response.status_code == 200:
    print("Request was successful")  
else:
    print(f"Request failed with status code: {response.status_code}")
for i in range(0,data['numResultsFound'],15):
    print(data['numResultsFound'])
    headers2 = {
        'authority': 'www.verical.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'dfp': '6512826d0bfd42def94a6a460d885c61',
        'expires': 'Sat, 01 Jan 2000 00:00:00 GMT',
        'if-modified-since': '0',
        'origin': 'https://www.verical.com',
        'pragma': 'no-cache',
        'referer': 'https://www.verical.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    json_data2 = {
    'parameters': [
        {
            'key': 'search_term',
            'values': [
                '*',
            ],
        },
        {
            'key': 'part_category_id',
            'values': [
                776,
            ],
        },
        {
            'key': 'start_index',
            'values': [
                i,
            ],
        },
        {
            'key': 'quantity_min',
            'values': [
                0,
            ],
        },
        {
            'key': 'facet_field',
            'values': [
                'manufacturer_id',
                'category_unique',
            ],
        },
    ],
}
    
    try:
        response2 = requests.post(
            'https://www.verical.com/server-webapp/api/rest/search/parametric',
             params=params,
             #cookies=cookies,
             headers=headers,
             json=json_data2,
	     timeout= 5,
) 
    except:
        continue
    try:
        data2=response2.json()['records']
    except:
        continue
    if len(data2)==0:
        continue
    for j in range(0, len(data2)):
         mpn=(data2[j].get('mpn', ''))
         manufacturerName=(data2[j].get('manufacturerName', ''))
         eccnCode=(data2[j].get('eccnCode', ''))
         exceedsSVHC=(data2[j].get('exceedsSVHC', ''))
         hazmatFlag=(data2[j].get('hazmatFlag', ''))
         includesSVHC=(data2[j].get('includesSVHC', ''))
         lowestPrice=(data2[j].get('lowestPrice', ''))
         manufacturerCode=(data2[j].get('manufacturerCode', ''))
         manufacturerId=(data2[j].get('manufacturerId', ''))
         manufacturerImageUrl=(data2[j].get('manufacturerImageUrl', ''))
         militaryFlag=(data2[j].get('militaryFlag', ''))
         originalDataSheetUrl=(data2[j].get('originalDataSheetUrl', ''))
         partCategoryId=(data2[j].get('partCategoryId', ''))
         partCategoryUnique=(data2[j].get('partCategoryUnique', ''))
         partDescription=(data2[j].get('partDescription', ''))
         partId=(data2[j].get('partId', ''))
         quantity=(data2[j].get('quantity', ''))
         rohsCompliant=(data2[j].get('rohsCompliant', ''))
         searchableMpn=(data2[j].get('searchableMpn', ''))
         specSource=(data2[j].get('specSource', ''))
         weight=(data2[j].get('weight', ''))
         l = [mpn,manufacturerName, eccnCode, exceedsSVHC, hazmatFlag, includesSVHC, lowestPrice,
	      manufacturerCode,manufacturerId,manufacturerImageUrl,militaryFlag,originalDataSheetUrl,
	      partCategoryId,partCategoryUnique,partDescription,partId,quantity,rohsCompliant
	      ,searchableMpn,specSource,weight]
         print(l)
         write(l, df1)
    else:
         print(f"Request failed with status code: {response2.status_code}")

