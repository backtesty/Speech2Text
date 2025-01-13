# pip install pyannote.audio
# pip install pydub  

from pyannote.audio import Pipeline

HF_TOKEN="hf_cjDVTbMhuAkBRSKimJE"
pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-3.1",
    use_auth_token=HF_TOKEN)

import torch
pipeline.to(torch.device("cpu"))
diarization = pipeline("audio.wav")

with open("audio.rttm", "w") as rttm:
    diarization.write_rttm(rttm)

for turn, _, speaker in diarization.itertracks(yield_label=True):
    print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}")

# Convert rttm to json
import json
data_json = []
with open("audio.rttm", "r") as rttm:
    for line in rttm:
        data = line.split()
        data_json.append({"start": float(data[3]), "end": float(data[3]) + float(data[4]), "speaker": data[7]})

with open("audio_diarizado.json", "w") as json_file:
    json.dump(data_json, json_file)


from pydub import AudioSegment

song = AudioSegment.from_wav("audio.wav")

with open("audio_diarizado.json", "r") as json_file:
    data = json.load(json_file)
    for index, segment in enumerate(data):
        total_time = segment["end"] - segment["start"]
        segment_song = song[segment["start"] * 1000:segment["end"] * 1000]
        segment_song.export(f"parts/part_{index}.wav", format="wav")
        print(f"audio_{index}.wav")

from openai import OpenAI
client = OpenAI(api_key="sk-proj-hmihGtcph0vEb-jXiwRaG58OeV9hfhk6qsnrwHzoHbAEltxvkfW63iF_JXO_Us4JyA1AtCuYsA")

from pydub import AudioSegment
import os

parts_text = []
counter = 0
for file in os.listdir("parts"):
    print(f"Processing part {counter}")
    index = file.split("_")[1].split(".")[0]
    part_name = f"parts/{file}"
    part = AudioSegment.from_wav(part_name)
    part_time = len(part) / 1000

    # Minimum audio length is 0.1 seconds. OpenAI API does not accept audio files with less than 0.1 seconds.
    if part_time < 0.1:
        parts_text.append({
            "index": index,
            "text": ""
        })
        continue

    audio_file = open(part_name, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
    )
    parts_text.append({
        "index": index,
        "text": transcription.text
    })
    counter += 1

with open("transcriptions.json", "w", encoding="utf-8") as json_file:
    json.dump(parts_text, json_file, ensure_ascii=False, indent=4)


import json

with open("audio_diarizado.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

with open("transcriptions.json", "r", encoding="utf-8") as json_file:
    transcriptions = json.load(json_file)
    transcriptions = sorted(transcriptions, key=lambda x: int(x["index"]))

for index, audio_segment in enumerate(data):
    audio_segment["transcription"] = transcriptions[index]["text"]
    
with open("audio_diarizado_transcribed.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)