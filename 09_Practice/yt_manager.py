import json


def list_all_videos(videos):
    pass

def add_video(videos):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass


def main():
    videos = []
    while True:
        print("Youtube Manager App | Choose an Option\n")
        print("-" * 20)
        print("1. List all Youtube Videos")
        print("2. Add a Youtube Video")
        print("3. Update a Youtube Video Details")
        print("4. Delete a Youtube Video")
        print("5. Exit")
        print("-" * 20)
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