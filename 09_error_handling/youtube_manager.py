
import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def list_all_videos(videos):
    pass

def add_video(videos):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass

def main():
    videos = load_data()
    while True:
        print("\nYoutube Manager | Choose an Option")
        print("\n1. List all Youtube Videos ")
        print("\n2. Add a Youtube Video ")
        print("\n3. Update a Youtube Video Details ")
        print("\n4. Delete a Youtube Video ")
        print("\n5. Exit the App ")
        choice = input("Enter your Choice : ")
        
        match choice:
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