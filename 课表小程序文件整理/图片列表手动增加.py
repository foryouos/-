import json



if __name__ == '__main__':
    picture_list_json={"imgUrls":[]}
    """手动添加图片URL"""
    picture_list=\
    [
        "http://r.photo.store.qq.com/psc?/V51tNpWb2FonU036uaZ52J0vZx42hUZ3/45NBuzDIW489QBoVep5mcRbpRuo0YtCJLZ4lSIZeUEz.9gGrL5dMuNhdFZ.x*eZVFxMzLoILGoHxHrZRrFoL3PIwaPajXQWhc6qkDxNVaHM!/r",
        "http://r.photo.store.qq.com/psc?/V51tNpWb2FonU036uaZ52J0vZx42hUZ3/45NBuzDIW489QBoVep5mcbEIWmSznNp9xiqwvjAtcaDWQDWWeups5YU0fKHxrSc8VoNOLjZlomlQhqbRPoT2*w1JBEAMHEYk67QEc*pItOQ!/r",
        "http://r.photo.store.qq.com/psc?/V51tNpWb2FonU036uaZ52J0vZx42hUZ3/45NBuzDIW489QBoVep5mcVcDOaXXblCYMqO1JUopb.RgbpNr7RxjSsmWg8QGbOZLP3mj0EwjNpJH1OhZs2S9zXCL5A1xq0BdRNa3120XbKI!/r",
        "http://r.photo.store.qq.com/psc?/V51tNpWb2FonU036uaZ52J0vZx42hUZ3/45NBuzDIW489QBoVep5mcVcDOaXXblCYMqO1JUopb.Syuk3RaqRBWW*uMUmdIegkj9MEJa7YuRbv0p7Th2R2euK4tKzh4dmboTNX.8sF2iI!/r",
        "http://r.photo.store.qq.com/psc?/V51tNpWb2FonU036uaZ52J0vZx42hUZ3/45NBuzDIW489QBoVep5mcYjRLwctrHIr0y*okvpiPSYrDQHXOUuLMTZh4xh6I9g5Lfj77*Kzj9wyZzXDUPQcFbqCJL5LpKDbJaW6dMQe9.c!/r",
        "http://r.photo.store.qq.com/psc?/V51tNpWb2FonU036uaZ52J0vZx42hUZ3/45NBuzDIW489QBoVep5mcdrAflS9cWsEXZQagyAxdw.gf3N29FtcRJfv6NOBbVwSfQ8.gMYWeSUzAl7iplZ4Kof.ybetTwVaWM13umHwjNM!/r",
        "http://r.photo.store.qq.com/psc?/V51tNpWb2FonU036uaZ52J0vZx42hUZ3/45NBuzDIW489QBoVep5mcRbpRuo0YtCJLZ4lSIZeUEwvGzsvONlW5EvRB5qu8u6ty4ddc6bdmgoRQeAXfJis15PK57.jX0cQC7G6Ug0OMHE!/r",
        "http://r.photo.store.qq.com/psc?/V51tNpWb2FonU036uaZ52J0vZx42hUZ3/45NBuzDIW489QBoVep5mcTjNMbkBQzyY5Qaqw24aFTMNK7ZvygosNitxuTM3flcUrNAYbW21ii.iCbJpDU077ctM7NPLy2IOiHtN35VvBPo!/r",
        "http://r.photo.store.qq.com/psc?/V51tNpWb2FonU036uaZ52J0vZx42hUZ3/45NBuzDIW489QBoVep5mcTjNMbkBQzyY5Qaqw24aFTM4.07pbpVsUmDZRn*EMRJsAw.*0wcnWMIrtTnP*H.LgM5BSTJtp.3vWDGPfwkM8Es!/r",

    ]
    picture_list_json["imgUrls"]=picture_list
    # vacant_data_jsons = json.dumps(picture_list_json, indent=4, ensure_ascii=False, separators=(',', ':'))

    """优化空间设计"""
    vacant_data_jsons = json.dumps(picture_list_json, ensure_ascii=False)
    with open("./上传小程序文件/图片列表/图片列表.json", "w", encoding='utf-8') as f:
        f.write(vacant_data_jsons)
        print(vacant_data_jsons)
        f.close()