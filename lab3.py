import requests
import json
import csv


headers = {
    'Authorization': '',
    'API-Key': '',
    'Accept': 'application/json',
}

p = {
    'severities': ''
}
response = requests.get('https://apptwo.contrastsecurity.com/Contrast/api/ng/ORGID/traces/APPID/filter', params=p,headers=headers)
app = requests.get('https://apptwo.contrastsecurity.com/Contrast/api/ng/ORGID/applications/APPID/', headers=headers)
result=json.loads(response.text)
appName=json.loads(app.text)
print(result)
"""
with open('contrast.csv', mode='w') as csv_file:
    fieldnames=['AppName','VulnID', 'Title', 'Status', 'Severity']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for i in range (0, len(result['traces'])):
        writer.writerow({'AppName': appName['application']['name'],'VulnID': result['traces'][i]['uuid'], 'Title': result['traces'][i]['title'], 'Status': result['traces'][i]['status'], 'Severity': result['traces'][i]['severity']})
"""
