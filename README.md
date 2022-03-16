# Wridr
>Howdy! Welcome to Wridr 🤠 and interactive blog posting app. Where the user is able to sign up, create, edit, and delete a post. Also the user is able to leave a comment on another user's post.

# Technologies Used
>Used Django for frontend and also backend.
>Database used : PosgresSQL
>CSS styling with Bulma.

## Backend Models
>Post model:
consist of a title, image, body_text, created_at, and a user.

>Comment model:
consist of inheriting the post model. Also using comment_text and user attributes.

## User stories
>As a user, when the app is open they will see a Latest Post page, that will show the latest post of user's.

>As a user, when clicking through the tabs they will be prompted to log in. If they do not have an account, they will drop down the more tab to sign up.

>As a user, once the account is created or the user has logged in, it will direct them to their All post page, where they are able to create their first post.

>As a user, if they do not signup or log in they will only be able to see the Latest post page. 

>As a user, they are able to leave comments on other user's post and it will show the comment and the user's tag name.

Stretch Goal:
I would like for the user to be able to delete their comment. 
I would like for the user to have a profile and avatar showing on their page. 
I would like for the user to be able to delete their account along with their content.



