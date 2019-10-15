from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response
def fun(funtion):
    def http(request):
        hhead='<div class="header">' \
                '<div class="heading_con">' \
                    '<div class="dw">' \
                        '<div class="heading">' \
                        '<div class="logo fl"><a href="#"><img src="/static/images/logo.png" alt="logo" /></a></div>' \
                        '<div class="top_right_con fr">' \
                    '<div class="head_save_site"><a class="a1" href="javascript:addfavorite();">收藏本站</a><a class="a2" href="javascript:setHomepage();">设为主页</a></div>' \
                        '<div class="head_tel"> <img src="/static/images/tel.png" alt="logo" /> </div>' \
                        '</div>' \
                        '<div class="c">' \
                        '</div>' \
                    '</div>' \
                '</div>' \
              '</div>'
        str=""
        http = 'http://127.0.0.1:8000/'
        head=['index','about','product_list','#','#','contact']
        head1=['网站首页','关于我们','产品中心','服务支持','招贤纳士','联系我们']
        for i in range(0,6):
            if i in [3,4]:
                str += "<li id ='m{}'><h3><a href='{}'>{}</a></h3>".format(i + 1,head[i], head1[i])
            else:
                str+="<li id ='m{}'><h3><a href='{}{}'>{}</a></h3>".format(i+1, http, head[i],head1[i])

        ford='<div class="myfooter">' \
             '<a href="#">首  页</a>|' \
             '<a a href="#">产品中心</a>|' \
             '<a a href="#">人才招聘</a>|' \
             '<a a href="#">技术服务</a>|' \
             '<a a href="#">联系我们</a>|' \
             '<a a href="#"><img src="/static/images/2.gif"> 57889</a>' \
             '<p>版权所有：浙江戴卡宏鑫科技有限公司</p>' \
             '</div>'
        str2=""
        for i in range(5):
            if i==1:
                str2+='<a class="pmenu_a pmenu_cuta" href="{}product_list">锻造绞线盘</a></li>'.format(http)
            elif i==2:
                str2+='<li><a class="pmenu_a" href="{}product_article">绞线盘</a></li>'.format(http)
            else:
                str2+='<li><a class="pmenu_a" href="{}product_list">锻造绞线盘</a></li>'.format(http)
        hhhed='<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">' \
              '<html xmlns="http://www.w3.org/1999/xhtml">' \
              '<head>' \
              '<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />' \
              '<link rel="stylesheet" type="text/css" href="/static/css/basic.css"/>' \
              '<link rel="stylesheet" type="text/css" href="/static/css/style.css"/>' \
              '<title>戴卡宏鑫</title>' \
              '<meta name="keywords" content="戴卡宏鑫" />' \
              '<meta name="description" content="戴卡宏鑫" />' \
              '</head>' \
              '<body>' \
              '<script type="text/javascript" src="js/jquery1.42.min.js"></script>' \
              '<script type="text/javascript" src="js/jquery.SuperSlide.2.1.js"></script>' \
              '<script type="text/javascript" src="js/share.js"></script>'
        ret=funtion(request,str,ford,str2,hhead,hhhed)
        return ret
    return http

def anok(request):
    return HttpResponse(12)
@fun
def about_html(request,*http):
    ok='<div class="conbg">'\
  '<div class="dw">'\
     '<div class="pmenu">'\
        '<ul>'\
            '<li><a class="pmenu_a pmenu_cuta" href="/">公司介绍</a></li>'\
        '</ul>'\
    '</div>'\
    '<div class="content">'\
  '<div class="about_com fl">'\
      '<img src="/static/images/company.jpg" alt="" />'\
    '</div>'\
  '<div class="about_comtext fr">'\
      '<h2>浙江戴卡宏鑫科技有限公司</h2>'\
    '<p>浙江戴卡宏鑫科技有限公司是专业生产锻造铝轮毂和锻造绞线盘的企业，公司坐落于浙江台州市黄岩区，一期占地面积30000㎡。公司拥有一流的生产工艺、设备和一流的检测仪器，并建立了完整的企业生产标准、通过了ISO9001质量保证体系，确保产品质量。公司一贯坚持“信誉第一、客户至上”，以最完善的服务体系和最细致的工作作风，为全球客户提供最优质的服务。</p>'\
    '<p>公司技术力量雄厚，采用世界一流的锻造工艺和设备，分别从德国、日本、意大利等国引进国际最先进的大型数控锻造、旋压等加工、涂装、检测设备。公司生产的锻造铝轮毂产品已通过美国SMITHES实验室产品认证、DOT认证、日本VIA认证、ISO/TS16949认证等多项国际认证，远销北美、欧洲、亚、澳、非洲各地。</p>'\
     '<p>公司生产的锻造绞线盘，采用高强度的铝合金材料经过高压锻造、热处理、精车、自动焊接、表面硬质氧化等多步工艺加工而成，具有造型美观，抗拉强度高、不断裂、不变形等特点。产品规格齐全，型号有14" x 14"，,17" x 17"，21" x 21"，30" x 21"，30" x 42"等，还可以根据客户具体需要生产其它规格产品，可以与各类中外经编机配套。</p>'\
  '<p>我们用手握手的承诺、心贴心的服务，与各界通力协作共创辉煌。宏鑫公司热忱欢迎广大客户惠顾，洽谈业务，进行广泛的经贸、技术合作。我们对您的光临，以及您与我们的任何形式的合作和支持，表示法子内心的深切感谢！</p>'\
    '</div>'\
  '</div>'\
      '<div class="c"></div>'\
  '</div>'\
 '</div>'\
'</div>'
    return render_to_response('about.html',locals())
@fun
def contact_html(request,*http):
    ok='<div class="conbg">'\
  '<div class="dw">'\
     '<div class="pmenu">'\
        '<ul>'\
            '<li><a class="pmenu_a pmenu_cuta" href="/">联系我们</a></li>'\
        '</ul>'\
    '</div>'\
    '<div class="content">'\
	'<h2 class="t_contact">浙江戴卡宏鑫科技有限公司</h2>'\
	'<ul class="c_contact">'\
         '<li><span>公司名称:</span> 浙江戴卡宏鑫科技有限公司</li>'\
         '<li><span>所在地:</span> 浙江/台州市</li>'\
		 '<li><span>联系人:</span> 徐小姐</li>'\
         '<li><span>联系方式:</span> 13906587665</li>'\
		 '<li><span>注册资本:</span> 94117600人民币</li>'\
		 '<li><span>公司规模:</span> 200-500人</li>'\
		 '<li><span>注册年份:</span> 2006年</li>'\
		 '<li><span>公司类型:</span> 企业单位制造商</li>'\
		 '<li><span>公司地址:</span> 浙江省台州市黄岩区经济开发区食品工业园三期</li>'\
		 '<li><span>经营范围:</span> 经编机配件</li>'\
        '</ul>'\
	    '</div>'\
        '<div class="c"></div>'\
        '</div>'\
        '</div>'\
        '</div>'
    return render_to_response('contact.html',locals())
@fun
def index_html(request,*http):
    ok='<div class="dw">'\
    '<div class="headline"><span><img src="/static/images/titlebg.jpg" alt="" />关于我们 <b>ABOUT US</b></span></div>'\
  '<div class="about_company_img fl">'\
      '<img src="/static/images/gc.jpg" alt="" />'\
    '</div>'\
  '<div class="about_company_text fr">'\
      '<h2>浙江戴卡宏鑫科技有限公司</h2>'\
    '<p>浙江戴卡宏鑫科技有限公司是专业生产锻造铝轮毂和锻造绞线盘的企业，公司坐落于浙江台州市黄岩区，一期占地面积30000㎡。公司拥有一流的生产工艺、设备和一流的检测仪器，并建立了完整的企业生产标准、通过了ISO9001质量保证体系，确保产品质量。公司一贯坚持“信誉第一、客户至上”，以最完善的服务体系和最细致的工作作风，为全球客户提供最优质的服务。公司技术力量雄厚，采用世界一流的锻造工艺和设备，分别从德国、日本、意大利等国引进国际最先进的大型数控锻造、旋压等加工、涂装、检测设备。公司生产的锻造铝轮毂产品已通过美国SMITHES实验室产品认证、DOT认证、日本VIA认证、ISO/TS16949认证等多项国际认证，远销北美、欧洲、亚、澳、非洲各地。<a href="#" class="cor_red">查看更多 →</a></p>'\
    '</div>'\
      '<div class="c"></div>'\
  '</div>'\
  '<!--about-->'\
'<div class="conbg">'\
  '<div class="dw">'\
  '<div class="contact_text fl">'\
       '<h2>联系方式</h2>'\
     '<p><span>浙江戴卡宏鑫科技有限公司</span></p>'\
     '<p>联系人：徐小姐</p>'\
     '<p>联系电话：13906587665</p>'\
     '<p>企业官网：www.hxbeam.com.cn</p>'\
     '<p>邮箱：hongxin17@hxtwheel.com</p>'\
     '<p>公司地址：浙江省台州市黄岩区经济开发区食品工业园三期</p>'\
    '</div>'\
  '<div class="contact_tit fl">'\
     '<img src="/static/images/contact.jpg" alt="" />'\
    '</div>'\
  '<div class="contact_kefu fl">'\
     '<img src="/static/images/kefu.jpg" alt="" />'\
    '</div>'\
      '<div class="c"></div>'\
  '</div>'\
'</div>'\
'</div>'
    count=[i for i in range(8)]
    return render_to_response('index.html',locals())
@fun
def product_article_html(request,*http):
    return render_to_response('product_article.html',locals())
@fun
def product_list_html(request,*http):
    return render_to_response('product_list.html',locals())

