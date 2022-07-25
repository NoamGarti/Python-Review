def create_youtube_video(title,description):
	dict1= {"title":title,"description":description,"likes":0,"dislikes":0,"comments":{}}
	return dict1
def likes(dict1):

	dict1["likes"] += 1
	return dict1
def dislikes(dict1):
	dict1["dislikes"] += 1
	return dict1
def comments_text(comments,username,dict1):
	dict1["comments"][username] = comments
	return dict1


dict1 = create_youtube_video("fun vid" , "this vid is fun")
dict1 = comments_text("cool!" , "Noam" , dict1)
likes(dict1)
for i in range(494):
	likes(dict1)
dislikes(dict1)
print(dict1)
#create_youtube_video()