# DOCUMENTATION

	VERSION: v.1.0
	BY: Atta Badu Kwabena
	
# ABOUT THIS PROJECT
This is a simple news and social media web app. 
Users can use this app to share their thoughts
on latest and trending stories around the world.

	PROJECT NAME: HashInn
		
# FUNCTIONALITY
This project is divided into multiple apps. 
Each app has it own functionality, 
but all the apps interact with each other 
to provide an overall functionality of the 
web application. Each app is responsible 
for creating the required database tables/models, 
retrieving and inserting data in the database table, 
and converting/serializing data from the database tables
into JSON format.
	
	APPS
		Posts: An app for creating, viewing and 
		managing posts. This include likes, 
		comments and hash tags.
		
		Profiles: An app for managing user profiles, 
		including editing profile information and viewing 
		other user profiles.
		
		Notifications: An app for handling notifications 
		for likes, comments, etc
		
		Chats: An app for managing private conversation 
		between users.

# DATABASE MODELS/TABLES

	Profile: Stores user related data.
		first_name
		last_name
		username
		bio
		profile_image

	Post: Stores details about a post.
		message
		user
		image
		posted_at
		modified_at

	Tag: Stores hash tags.
		tag
		created_at
		modified_at

	PostTag: Keeps track of posts and hash tags.
		post
		hashtag
		created_at
		modified_at

	Like: Keeps track of likes on a post.
		user
		post
		is_active
		created_at
		modified_at

	Comment: Keeps track of comments on a post.
		user
		post
		message
		image
		posted_at
		modified_at

# API ENDPOINTS

	GET api/posts/id
	{
		url,
		user: {
			url,
			first_name,
			last_name,
			username,
			profile_picture,
		}
		message,
		image,
		posted_at,
		hashtags: [
			{
				url,
				tag, 
			}
			...
			...
		]
		likes,
		comments: [
			{
				url,
				user: {
					url,
					first_name,
					last_name,
					username,
					profile_picture,
				}
				message,
				image,
				posted_at,
				modified_at,
			},
			...
			...
		]
			
	}

	GET /api/trending
	[
		{
			url,
			user: {
				url,
				first_name,
				last_name,
				username,
				profile_picture,
			}
			message,
			image,
			posted_at,
			modified_at,
			hashtags: [
				{
					url,
					tag, 
				}
				...
				...
			]
			likes,
			comments,
			
		},
		...
		...
	]

	GET /hashtags
	[
		{
			url,
			tag,
			count,
		},
		...
		...
	]
	
	GET /hashtags/tag
	{
		url,
		tag,
		count,
		posts: [
			{
				url,	
				message,
				image,
				posted_at,
				modified_at,
				hashtags: [
					{
						url,
						tag, 
					}
					...
					...
				]
				likes,
				comments,
			}
		]
	}

	GET /profile 
	{
		url
		first_name,
		username,
		profile_picture,
		bio,
		posts: [
			{
				url,	
				message,
				image,
				posted_at,
				modified_at,
				hashtags: [
					{
						url,
						tag, 
					}
					...
					...
				]
				likes,
				comments,
			}
		]
	}
