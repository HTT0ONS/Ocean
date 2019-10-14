from django.http import HttpResponse



def juju(request):
    head='<html><head>'
    title='<title>Hello World</title>'

    body='<body style="text-align:center">'
    end_body='</body>'
    chengfa=r''
    rotate=0
    div='<div style="width:1px;height:1px;margin-right:auto;margin-left:auto;margin-top:200px">'
    x = 20
    y = 20
    end_div='</div>'
    def css(rotate,x,y):
        style = 'style=' \
                "\"-moz-transform: rotate(31deg);" \
                "-webkit-transform: rotate({}deg);" \
                "-o-transform:rotate(30deg);"\
                "-ms-transform:rotate(20deg);"\
                "display: block;" \
                "position: absolute;" \
                "width:{}px;" \
                "transform-origin: 150px 150px;" \
                "height:{}px;" \
                "filter:progid:DXImageTransform.Microsoft.BasicImage(rotation=3)\"".format(rotate,x,y)
        return style
    #'''''''''''''''''''''''''
    id_i=1
    id_j=1
    for i in range(1, 10):
        if id_i<1:
            id_i=9
        for j in range(1, i + 1):
            rotate+=8
            if id_j>9:
                id_j=1
            chengfa=chengfa+'<div {} >{:2}*{:2}={:>5}</div>'.format(css(rotate,x,y),j, i, (i) * (j))
            id_j+=1
        id_i-=1
        # chengfa=chengfa+'</br>'
    #''''''''''''''''''''''''''


    HR=head+title+body+div+chengfa+end_div+end_body
    return HttpResponse(HR)