# MakeBook_ISN_30001
给Mia同学做英文教科书

## 操作步骤
- ffmpeg把mp4转mp3
命令:
```
ffmpeg -i E:/BaiduNetdiskDownload/1-25.mp4 -vn -c:a libmp3lame -q:a 4 E:/BaiduNetdiskDownload/1-25.mp3
```
- 执行xxx脚本，切割
- 执行b脚本，得到text

- 把文本一个一个送进gpt翻译英文，指令`请把下面的文本，翻译成小孩子能懂的英文。并且删除出版社等等相关内容`


## 安装软件
ffmpeg  用于转mp4到mp3


## 安装库
- 新建python环境
```
conda create --name makebook python=3.9
conda activate makebook
```
- 环境设置gemina密钥
ref:https://ai.google.dev/gemini-api/docs/api-key?hl=zh-cn#windows
```
// win平台在gitbash等terminal中使用
export GEMINI_API_KEY=your_key_here

// 测试连接

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${GEMINI_API_KEY}" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Write a story about a magic backpack."
          }
        ]
      }
    ]
  }'


```

- 安装google-genai库
`pip install google-genai`

- PyDub   用于分割
`pip install pydub`

- 安装ffmpeg（如果代码没有报错，可以跳过这个步骤）
`pip install ffmpeg-downloader`
安装后要重启session

##参考资料
- https://blog.csdn.net/FrenzyTechAI/article/details/131259440