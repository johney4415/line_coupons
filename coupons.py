all_codes = [{
    "name": '【第一週】國旅券',
    "codes": ['21', '32', '98', '67', '97', '410']
}, {
    "name": '【第一週】i原券',
    "codes": ['64', '85']
}, {
    "name": '【第一週】農遊券',
    "codes": ['89', '32', '54', '597', '453', '152']
}, {
    "name": '【第一週】藝fun券(數位)',
    "codes": ['96', '15', '07', '30', '73', '98', '19', '11']
}, {
    "name": '【第一週】藝fun券(紙本)',
    "codes": ['39', '37', '23', '36', '79', '08', '14', '75']
}, {
    "name":
    '【第一週】動滋券',
    "codes":
    ['97', '13', '19', '55', '71', '93', '381', '734', '644', '453', '985']
}, {
    "name": '【第一週】客庄劵2.0',
    "codes": ['81', '900']
}, {
    "name":
    '【第一週】地方創生券',
    "codes": [
        '081', '105', '594', '188', '089', '396', '521', '467', '912', '798',
        '358', '441', '367', '941', '335'
    ]
}, {
    "name": '【第二週】國旅券',
    "codes": ['87', '04', '40', '29', '71']
}, {
    "name": '【第二週】i原券',
    "codes": ['12', '59']
}, {
    "name": '【第二週】農遊券',
    "codes": ['50', '13']
}, {
    "name": '【第二週】藝fun券(數位)',
    "codes": ['78', '00', '39', '22', '61', '23', '15']
}, {
    "name": '【第二週】藝fun券(紙本)',
    "codes": ['37', '76', '31', '06', '51', '65', '81']
}, {
    "name": '【第二週】動滋券',
    "codes": ['91', '11', '04', '18', '57', '498', '756']
}, {
    "name":
    '【第二週】客庄劵2.0',
    "codes": [
        '11', '439', '841', '052', '206', '161', '457', '205', '012', '293',
        '446', '589'
    ]
}]
def get_coupons_result(my_code):
    result = []
    result_text = ''
    for i in all_codes:
        for code in i['codes']:
            if len(code) == 2:
                check_code = my_code[-2:]
            else:
                check_code = my_code
            if check_code == code:
                result.append(i.get('name'))
    for i in result:
        result_text += i
        result_text += '\n'
    return result_text