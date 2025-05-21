from google import genai



def video2text(filename,txtsavename):
  client = genai.Client(api_key="IzaSyAyh4qkpm-7dZVP5ja2XruyWfReIXMT6c8")

  myfile = client.files.upload(file=filename)
  prompt = 'Generate a transcript of the speech.'

  response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents=[prompt, myfile]
  )

  print(response.text)
  #保存文件
  if txtsavename !="" or txtsavename!= None:
    with open(txtsavename, "w", encoding="utf-8") as f:
          f.write(response.text)


# 正式运行
if __name__ == "__main__":

  filename = 'E:/BaiduNetdiskDownload/makebook_results/generative_ai_topics_0.mp3'
  txtsavename = 'E:/BaiduNetdiskDownload/makebook_results/generative_ai_topics_0.txt'
  video2text(filename,txtsavename)


