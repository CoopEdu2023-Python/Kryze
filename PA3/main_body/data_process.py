import os
import json
import pandas as pd
import setup


def generate_xlsx(user_data: dict, video_data: list):
    try:
        os.makedirs(f"output/{user_data['name']}")
    except:
        pass
    try:
        os.makedirs(f"output/{user_data['name']}/videos")
    except:
        pass
    for video in video_data:
        res = json.dumps(video.json_output, indent=2, ensure_ascii=False)
        final = '\n'.join(line for line in res.splitlines())
        with open(f"output/{user_data['name']}/videos/{video.json_output['bvid']}.json", "w", encoding='utf-8') as json_file:
            json_file.write(final)

    with open(f"output/{user_data['name']}/user_data.json", 'w', encoding='utf-8') as json_file:
        res = json.dumps(user_data, indent=2, ensure_ascii=False)
        final = '\n'.join(line for line in res.splitlines())
        json_file.write(final)