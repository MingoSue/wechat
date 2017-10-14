from django.shortcuts import render
from .models import Code, User
from urllib.request import urlopen

# Create your views here.
def index(request):
    # 获取code
    code = request.GET.get('code')
    Code.objects.create(code=code)
    return render(request, 'info/index.html')

def get_info(request):
    appid = ''
    secret = ''
    code = Code.objects.get()

    url = 'https://api.weixin.qq.com/sns/oauth2/access_token? \
     appid={}&secret={}&code={}&grant_type=authorization_code'.format(appid, secret, code)
    # 获取access_token
    access_token = urlopen(url)
    access = access_token['access_token']

    openid = ''
    url_info = 'https://api.weixin.qq.com/sns/userinfo? \
            access_token=ACCESS_TOKEN&openid=OPENID&lang=zh_CN'.format(access, openid)
    # 获取用户信息
    info = urlopen(url_info)
    openid = info['openid']
    nickname = info['nickname']
    sex = info['sex']
    province = info['province']
    city = info['city']
    country = info['country']
    User.objects.create(openid=openid, nickname=nickname, sex=sex, province=province, \
                        city=city, country=country)

    info = User.objects.all()
    context = {'info': info}
    return render(request, 'info/form.html', context)