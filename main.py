from tiktok_uploader.auth import AuthBackend
from tiktok_uploader.upload import upload_videos
number_of_posts_times_6 = 1
x = 0
videos = [
    {
        'path': 'C:\\Users\\abiko\\Documents\\Uploader\\a.mp4',
        'description': 'this is my description'
    },
    {
        'path': 'C:\\Users\\abiko\\Documents\\Uploader\\a.mp4',
        'description': 'this is also my description'
    },
    {
        'path': 'C:\\Users\\abiko\\Documents\\Uploader\\a.mp4',
        'description': 'this is my description'
    },

]
while x <= number_of_posts_times_6:
    auth = AuthBackend(cookies='C:\\Users\\abiko\\Documents\\Uploader\\cookies.txt')
    upload_videos(videos=videos, auth=auth, headless=True)
    x = x+1
