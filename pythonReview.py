def createYouTubeVideo(title: str, description: str, tags: list):
    if tags is None:
        tags = []
    elif len(tags) > 5: # if there are more than 5 tags, only use the first 5
        tags = tags[:5]
    return {"title": title, "description": description, "likes": 0, "dislikes": 0, "comments" : {}, "tags": tags}

def like(video: dict):
    video["likes"] += 1
    return video

def dislike(video: dict):
    video["dislikes"] += 1
    return video

def addComment(video: dict, username: str, comment: str):
    video["comments"][username] = comment
    return video

def addTags(video: dict, tags: list):
    if len(tags) > 5: tags = tags[:5] #if there are more than 5 tags, only use the first 5
    video["tags"] = tags
    return video

def compareVideos(video1: dict, video2: dict):
    count = 0
    for i in range(len(video1["tags"])):
        if video1["tags"][i] is video2["tags"][i]:
            count+=1
    return f"Similarity: {count/len(video1['tags'])}"

def main():

    video = createYouTubeVideo("My Video", "This is my video", [])
    print(video)


main()