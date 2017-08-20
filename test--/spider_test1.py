import  urllib.request
import  urllib.parse
import  json

url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=http://www.baidu.com/link"
keyword=str(input('请输入你要翻译的词：'))
#keyword='key'
form_data={}
form_data['i']=keyword
form_data['from']='AUTO'
form_data['to']='AUTO'
form_data['smartresult']='dict'
form_data['client']='fanyideskweb'
#form_data['salt']='1499687677478'
#form_data['sign']='5c47491182c68eea231c3e8d225bf9f6'
form_data['doctype']='json'
form_data['version']='2.1'
form_data['keyfrom']='fanyi.web'
form_data['action']='FY_BY_ENTER'
form_data['typoResult']='true'

data=urllib.parse.urlencode(form_data).encode('utf-8')

res=urllib.request.urlopen(url,data).read().decode('utf-8')
#print(res)

result=json.loads(res)
#print(result)
result=result['translateResult'][0][0]['tgt']
print("%s的翻译结果为%s"%(keyword,result))