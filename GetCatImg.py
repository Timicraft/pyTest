import urllib.request as url
import random


n = input("输入要下载的猫咪图片的数量：")
n = int(n)

#IP = ['210.72.14.142:80','112.12.37.196:53281','180.110.6.221:3128']

for x in range(n):

    #proxy_support = url.ProxyHandler({'http':random.choice(IP)})

    #opener = url.build_opener(proxy_support)

    #url.install_opener(opener)
    
    size_x = 500+int(random.randint(1,20))
    size_y = 500+int(random.randint(1,20))
    
    name_url = 'http://placekitten.com/g/'+str(size_x)+'/'+str(size_y)
    response = url.urlopen(name_url)
    
    img = response.read()
    name = 'cat_'+str(size_x)+'_'+str(size_y)+'_'+str(x)+'.jpg'
    
    with open(name,'wb') as f:
        f.write(img)

    
