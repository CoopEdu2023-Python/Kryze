import json
import pandas
import csv


def get_user_data(name: str):
    with open(f"output/{name}/user_data.json", "r", encoding='utf-8') as file:
        user_data = json.loads(file.read())
    return user_data


def get_video_data(name: str, bvids: list, uid: int):
    videos = list()
    for bvid in bvids:
        with open(f"output/{name}/videos/{bvid}.json", "r", encoding='utf-8') as file:
            video = json.loads(file.read())
            del video['comments_data']
            video['author'] = name
            video['uid'] = uid
            videos.append(video)
    return videos


def to_csv(name: str):
    user_data = get_user_data(name)
    videos = get_video_data(name, user_data['video_list'], user_data['uid'])
    del user_data['video_list']
    keys = user_data.keys()
    with open(f"output/{name}/user_data.csv", 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(user_data)


    keys = videos[0].keys()
    for video in videos:
        with open(f"output/{name}/video_data.csv", 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(video)


to_csv("iMoore")