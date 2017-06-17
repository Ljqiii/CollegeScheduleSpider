import  requests
import re
#Cookies需要每次登录后修改
cookies=dict(JSESSIONID='cbhZfD-PkD2-vee5Ob0Yv')
url="http://urp.hebau.edu.cn/jhFakzsViewAction.do?fajhh=5105&type=fa"

r=requests.get(url=url,cookies=cookies)
encoding=r.apparent_encoding

#print(r.text)

np=re.compile(r'"(\d+)","(-?\d+)","(.*?)","xxInfoAction\.do\?kzh=(\d+)&amp;fajhh=5105&amp;infoType=kcxx&amp;kch=(.+)","","ifra"')
name = re.findall(np, r.text)

url2="http://urp.hebau.edu.cn/xxInfoAction.do?kzh={kzh}&fajhh=5105&infoType=kcxx&kch={kch}"
xuenianxueqikemu=[]
for i in name:
    result=requests.get(url=url2.format(kzh=i[3],kch=i[4]),cookies=cookies)
    jihuaxuenian = re.findall('计划学年</td>\r\n\t\t\t\t\t\t <td >(.*?)</td>',result.text)
    jihuaxueqi = re.findall('计划学期\r\n\t\t\t\t\t\t</td>\r\n\t\t\t\t\t\t<td width="3">&nbsp;</td>\r\n\t\t\t\t\t\t<td>  (.*?)</td>\r\n',result.text)
    print(jihuaxuenian[0]+"\t"+jihuaxueqi[0]+"  "+i[2])
    xuenianxueqikemu.append((jihuaxuenian[0],jihuaxueqi[0],i[2]))

#筛选出大二要学的课程
for ii in xuenianxueqikemu:
    if(ii[0]=='2017-2018学年'):
        print(ii)
