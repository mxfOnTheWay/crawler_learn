import requests

class HtmlDownloader(object):

    def download(self,url):
        if url is None:
            return None
        user_agent='User-Agent,Mozilla/5.0'
        headers={'user-agent':user_agent}
        try:
            r=requests.get(url,headers=headers)
            r.raise_for_status()
            r.encoding=r.apparent_encoding
            return r.text
        except Exception as e:
            return 'error:',e

