from pydub import AudioSegment
# import pydub
import os


#------ 设置
file_mp3 = "E:/BaiduNetdiskDownload/1-25.mp3"
work_folder = os.path.join(os.path.dirname(file_mp3), "makebook_results")
os.makedirs(work_folder, exist_ok=True)  # 不存在就创建，存在也不会报错

print(work_folder)



#------ mp3切割15分钟

podcast = AudioSegment.from_mp3(file_mp3)

# PyDub handles time in milliseconds
ten_minutes = 15 * 60 * 1000
 
total_length = len(podcast)
 
start = 0
index = 0
while start < total_length:
    end = start + ten_minutes
    if end < total_length:
        chunk = podcast[start:end]
    else:
        chunk = podcast[start:]
    with open(  os.path.join(work_folder, f"generative_ai_topics_{index}.mp3") , "wb") as f:
        chunk.export(f, format="mp3")
    start = end
    index += 1


#----------转录文本
# prompt = ""
# for i in range(index):
#     clip = os.path.join(work_folder, f"generative_ai_topics_{i}.mp3")
#     audio_file= open(clip, "rb")
#     transcript = openai.Audio.transcribe("whisper-1", audio_file, 
#                                      prompt=prompt)
#     # mkdir ./data/transcripts if not exists
#     if not os.path.exists("./data/transcripts"):
#         os.makedirs("./data/transcripts")
#     # write to file
#     with open(f"./data/transcripts/generative_ai_topics_{i}.txt", "w") as f:
#         f.write(transcript['text'])
#     # get last sentence of the transcript
#     sentences = transcript['text'].split("。")
#     prompt = sentences[-1]

