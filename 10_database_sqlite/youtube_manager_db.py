import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def list_videos():
    cur.execute("SELECT * FROM videos")
    for row in cur.fetchall():
        print(row)

def add_video(name, time):
    cur.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    cur.commit()

def update_video(video_id, new_name, new_time):
    cur.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    cur.commit()

def delete_video(video_id):
    cur.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    cur.commit()

def main():
    while True:
        print("\nYoutube Maneger App With DB")
        print("=" * 50)
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit App")
        print("=" * 50)
        choice = input("Enter Your Choice : ")
        
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name : ")
            time = input("Enter the video time : ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter video ID to update : ")
            name = input("Enter the video name : ")
            time = input("Enter the video time : ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter video ID to delete : ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice!")
            
    conn.close()

if __name__ == "__main__":
    main()