import json

def load_data():
    try:
        with open('yt.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('yt.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("=" * 50)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']}, Time: {video['time']}")
    print("=" * 50)

def add_video(videos):
    name = input("Enter video name : ")
    time = input("Enter video time : ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update : "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name : ")
        time = input("Enter the new video time : ")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid index selected!")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted : "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index selected!")


def main():
    videos = load_data()
    while True:
        print("Youtube Manager App | Choose an Option")
        print("-" * 40)
        print("1. List all Youtube Videos")
        print("2. Add a Youtube Video")
        print("3. Update a Youtube Video Details")
        print("4. Delete a Youtube Video")
        print("5. Exit")
        print("-" * 40)
        choose = input("Enter Your Choice : ")
        
        match choose:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice!")

if __name__ == "__main__":
    main()