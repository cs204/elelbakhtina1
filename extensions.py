filename = input("File name: ")
media_type = ""
if filename.lower().endswith('.gif'):
    media_type = 'image/gif'
elif filename.lower().endswith(('.jpg', '.jpeg')):
    media_type = 'image/jpeg'
elif filename.lower().endswith('.png'):
    media_type = 'image/png'
elif filename.lower().endswith('.pdf'):
    media_type = 'application/pdf'
elif filename.lower().endswith('.txt'):
    media_type = 'text/plain'
elif filename.lower().endswith('.zip'):
    media_type = 'application/zip'
if media_type != "":
    print(media_type)
else:
    print("Media type: application/octet-stream")