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
- openai安装，用于转议文本
`pip install openai`

- PyDub   用于分割
`pip install pydub`

- 安装ffmpeg（如果代码没有报错，可以跳过这个步骤）
`pip install ffmpeg-downloader`
安装后要重启session

##参考资料
- https://blog.csdn.net/FrenzyTechAI/article/details/131259440