import requests
S=print
w=requests.post
T={'api':'53d19baf0d9db6abc41bc92f2c50c38c-f7910792-ae9ff402'}
m='sandbox5b325091bd334c5792decfea9d1f14c2.mailgun.org'
f={"from":"Zenmark Mail <sandbox5b325091bd334c5792decfea9d1f14c2@mailgun.org>","to":"tcsion@mail.com","subject":"New Survivio+ JS Error Report!",}
def b():
 f["text"]="Testing the Mailgun API from Sandbox env"
 r=w('https://api.mailgun.net/v3/{}/messages'.format(m),auth=('api',T['api']),data=f)
 S(r.status_code)
b()
