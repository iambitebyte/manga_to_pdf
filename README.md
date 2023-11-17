# jpg漫画转pdf

## 下载漫画资源
https://pan.baidu.com/s/166mMOAq2FuEcvHs2QLwiaQ?pwd=rbsh 
 
百度网盘口令: rbsh

别人的分享，不确定是否会长期有效


## 解压缩下载到的zip文件
```
$ ls -1
Monki_第01巻.zip
Monki_第02巻.zip
Monki_第03巻.zip
Monki_第04巻.zip
Monki_第05巻.zip
Monki_第06巻.zip
Monki_第07巻.zip
......
```

解压所有zip文件，rbshu.com是zip文件的解压密码
```
$ ls -1 | grep zip | awk '{ print "unzip -P rbshu.com "$1 }' | sh

```

## 将每个文件夹中的图片转换成pdf文件
```
pip install -r requirement.txt
python app.py
```
