# MakeBook_ISN_30001
给Mia同学做英文教科书

## 操作步骤
- ffmpeg把mp4转mp3
命令:
```
ffmpeg -i E:/BaiduNetdiskDownload/1-25.mp4 -vn -c:a libmp3lame -q:a 4 E:/BaiduNetdiskDownload/1-25.mp3
```
- 执行xxx脚本


## 安装软件
ffmpeg  用于转mp4到mp3


## 安装库
- 安装环境
```
conda create --name makebook python=3.9
conda activate makebook
```
- PyDub   用于分割
`pip install pydub`

##参考资料
- https://blog.csdn.net/FrenzyTechAI/article/details/131259440