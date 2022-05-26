import folium


def generate_shiyanshi():
    '''创建Map对象'''
    m = folium.Map(location=[30.5103, 114.4128], zoom_start=12, tiles='Stamen Toner')
    m.add_child(folium.LatLngPopup())
    folium.Marker(
        location=[30.5103, 114.4128],
        popup='华中科技大学无损检测实验室',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
    folium.CircleMarker(
        location=[30.5103, 114.4128],
        radius=50,
        popup='华中科技大学无损检测实验室',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(m)
    
    folium.Marker(
        location=[30.4556, 114.4748],
        popup='武汉喻远智能检测有限公司',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
    folium.CircleMarker(
        location=[30.4556, 114.4748],
        radius=50,
        popup='武汉喻远智能检测有限公司',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(m)
    
    folium.Marker(
        location=[30.6957, 114.5284],
        popup='武钢维尔卡钢绳制品有限公司',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
    folium.CircleMarker(
        location=[30.6957, 114.5284],
        radius=50,
        popup='武钢维尔卡钢绳制品有限公司',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(m)

    folium.Marker(
        location=[32.8362, 116.1748],
        popup='安徽口孜东矿',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
    folium.CircleMarker(
        location=[32.8362, 116.1748],
        radius=50,
        popup='安徽口孜东矿',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(m)

    folium.Marker(
        location=[38.8423, 109.4787],
        popup='内蒙古伊化矿',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
    folium.CircleMarker(
        location=[38.8423, 109.4787],
        radius=50,
        popup='内蒙古伊化矿',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(m)

    #114.4748，纬度：30.4556
    '''显示m'''
    m.save("E:/myhtml/shiyanshi.html")


def generate_weierka():
    '''创建Map对象'''
    m = folium.Map(location=[30.6957, 114.5284], zoom_start=12, tiles='Stamen Toner')
    m.add_child(folium.LatLngPopup())
    folium.Marker(
        location=[30.5103, 114.4128],
        popup='华中科技大学无损检测实验室',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
    folium.CircleMarker(
        location=[30.5103, 114.4128],
        radius=50,
        popup='华中科技大学无损检测实验室',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(m)
    
    folium.Marker(
        location=[30.4556, 114.4748],
        popup='武汉喻远智能检测有限公司',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
    folium.CircleMarker(
        location=[30.4556, 114.4748],
        radius=50,
        popup='武汉喻远智能检测有限公司',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(m)
    
    folium.Marker(
        location=[30.6957, 114.5284],
        popup='武钢维尔卡钢绳制品有限公司',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
    folium.CircleMarker(
        location=[30.6957, 114.5284],
        radius=50,
        popup='武钢维尔卡钢绳制品有限公司',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(m)

    folium.Marker(
        location=[32.8362, 116.1748],
        popup='安徽口孜东矿',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
    folium.CircleMarker(
        location=[32.8362, 116.1748],
        radius=50,
        popup='安徽口孜东矿',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(m)

    folium.Marker(
        location=[38.8423, 109.4787],
        popup='内蒙古伊化矿',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
    folium.CircleMarker(
        location=[38.8423, 109.4787],
        radius=50,
        popup='内蒙古伊化矿',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(m)

    #114.4748，纬度：30.4556
    '''显示m'''
    m.save("E:/myhtml/weierka.html")

def generate_yuyuan():
    '''创建Map对象'''
    m = folium.Map(location=[30.4556, 114.4748], zoom_start=12, tiles='Stamen Toner')
    m.add_child(folium.LatLngPopup())
    folium.Marker(
        location=[30.5103, 114.4128],
        popup='华中科技大学无损检测实验室',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
    folium.CircleMarker(
        location=[30.5103, 114.4128],
        radius=50,
        popup='华中科技大学无损检测实验室',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(m)
    
    folium.Marker(
        location=[30.4556, 114.4748],
        popup='武汉喻远智能检测有限公司',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
    folium.CircleMarker(
        location=[30.4556, 114.4748],
        radius=50,
        popup='武汉喻远智能检测有限公司',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(m)
    
    folium.Marker(
        location=[30.6957, 114.5284],
        popup='武钢维尔卡钢绳制品有限公司',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
    folium.CircleMarker(
        location=[30.6957, 114.5284],
        radius=50,
        popup='武钢维尔卡钢绳制品有限公司',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(m)

    folium.Marker(
        location=[32.8362, 116.1748],
        popup='安徽口孜东矿',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
    folium.CircleMarker(
        location=[32.8362, 116.1748],
        radius=50,
        popup='安徽口孜东矿',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(m)

    folium.Marker(
        location=[38.8423, 109.4787],
        popup='内蒙古伊化矿',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
    folium.CircleMarker(
        location=[38.8423, 109.4787],
        radius=50,
        popup='内蒙古伊化矿',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(m)

    #114.4748，纬度：30.4556
    '''显示m'''
    m.save("E:/myhtml/yuyuanzhineng.html")


def generate_kouzidong():
    '''创建Map对象'''
    m = folium.Map(location=[32.8362, 116.1748], zoom_start=10, tiles='Stamen Toner')
    m.add_child(folium.LatLngPopup())
    folium.Marker(
        location=[30.5103, 114.4128],
        popup='华中科技大学无损检测实验室',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
    folium.CircleMarker(
        location=[30.5103, 114.4128],
        radius=50,
        popup='华中科技大学无损检测实验室',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(m)
    
    folium.Marker(
        location=[30.4556, 114.4748],
        popup='武汉喻远智能检测有限公司',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
    folium.CircleMarker(
        location=[30.4556, 114.4748],
        radius=50,
        popup='武汉喻远智能检测有限公司',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(m)
    
    folium.Marker(
        location=[30.6957, 114.5284],
        popup='武钢维尔卡钢绳制品有限公司',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
    folium.CircleMarker(
        location=[30.6957, 114.5284],
        radius=50,
        popup='武钢维尔卡钢绳制品有限公司',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(m)

    folium.Marker(
        location=[32.8362, 116.1748],
        popup='安徽口孜东矿',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
    folium.CircleMarker(
        location=[32.8362, 116.1748],
        radius=50,
        popup='安徽口孜东矿',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(m)

    folium.Marker(
        location=[38.8423, 109.4787],
        popup='内蒙古伊化矿',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
    folium.CircleMarker(
        location=[38.8423, 109.4787],
        radius=50,
        popup='内蒙古伊化矿',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(m)

    #114.4748，纬度：30.4556
    '''显示m'''
    m.save("E:/myhtml/kouzidong.html")


def generate_yihua():
    '''创建Map对象'''
    m = folium.Map(location=[38.8423, 109.4787], zoom_start=10, tiles='Stamen Toner')
    m.add_child(folium.LatLngPopup())
    folium.Marker(
        location=[30.5103, 114.4128],
        popup='华中科技大学无损检测实验室',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
    folium.CircleMarker(
        location=[30.5103, 114.4128],
        radius=50,
        popup='华中科技大学无损检测实验室',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(m)
    
    folium.Marker(
        location=[30.4556, 114.4748],
        popup='武汉喻远智能检测有限公司',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
    folium.CircleMarker(
        location=[30.4556, 114.4748],
        radius=50,
        popup='武汉喻远智能检测有限公司',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(m)
    
    folium.Marker(
        location=[30.6957, 114.5284],
        popup='武钢维尔卡钢绳制品有限公司',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
    folium.CircleMarker(
        location=[30.6957, 114.5284],
        radius=50,
        popup='武钢维尔卡钢绳制品有限公司',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(m)

    folium.Marker(
        location=[32.8362, 116.1748],
        popup='安徽口孜东矿',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
    folium.CircleMarker(
        location=[32.8362, 116.1748],
        radius=50,
        popup='安徽口孜东矿',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(m)

    folium.Marker(
        location=[38.8423, 109.4787],
        popup='内蒙古伊化矿',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
    folium.CircleMarker(
        location=[38.8423, 109.4787],
        radius=50,
        popup='内蒙古伊化矿',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(m)

    #114.4748，纬度：30.4556
    '''显示m'''
    m.save("E:/myhtml/yihua.html")

def generate_main():
    '''创建Map对象'''
    m = folium.Map(location=[31.9149, 108.5449], zoom_start=5, tiles='Stamen Toner')
    m.add_child(folium.LatLngPopup())
    folium.Marker(
        location=[30.5103, 114.4128],
        popup='华中科技大学无损检测实验室',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)

    
    folium.Marker(
        location=[30.4556, 114.4748],
        popup='武汉喻远智能检测有限公司',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
   
    
    folium.Marker(
        location=[30.6957, 114.5284],
        popup='武钢维尔卡钢绳制品有限公司',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
    

    folium.Marker(
        location=[32.8362, 116.1748],
        popup='安徽口孜东矿',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
   

    folium.Marker(
        location=[38.8423, 109.4787],
        popup='内蒙古伊化矿',
        icon=folium.Icon(icon='info-sign',color='red')
    ).add_to(m)
   

    #114.4748，纬度：30.4556
    '''显示m'''
    m.save("E:/myhtml/main.html")




'''
/*
* @brief 主程序，程序由此执行
* @param 无
* @retval 无
*/
'''
if __name__ == '__main__':
    generate_main()
    generate_kouzidong()
    generate_shiyanshi()
    generate_weierka()
    generate_yihua()
    generate_yuyuan()
