from O365 import Account

credentials = ('daduartes@bucaramanga.gov.co', 'Msaraeileen1979')

# the default protocol will be Microsoft Graph

account = Account(credentials, auth_flow_type='credentials', tenant_id='78683ff2-0c20-4bda-bc77-d4b2a87f2a6a')
if account.authenticate():
   print('Authenticated!')