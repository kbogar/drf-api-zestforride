# Table of Contents
* [Validator Testing](#validator-testing)
    * [Python Validator](#python-validator)
* [Manual Testing](#manual-testing)

# Testing

## Validator Testing
### Python Validator
- All the Python files were tested using [CI Python Linter](https://pep8ci.herokuapp.com/) and there were no errors found.

**settings.py**

![](/docs/settings.png)

**urls.py**

![](/docs/urls.png)

**views.py**

![](/docs/views.png)

**permissions.py**

![](/docs/permissions.png)

**serializers.py**

![](/docs/serializers.png)

**profiles/views.py**

![](/docs/profiles4.png)

**profiles/urls.py**

![](/docs/profiles3.png)

**profiles/serializers.py**

![](/docs/profiles2.png)

**profiles/models.py**

![](/docs/profiles1.png)

**posts/views.py**

![](/docs/posts4.png)

**posts/urls.py**

![](/docs/posts3.png)

**posts/serializers.py**

![](/docs/posts2.png)

**posts/models.py**

![](/docs/posts1.png)

**likes/views.py**

![](/docs/likes4.png)

**likes/urls.py**

![](/docs/likes3.png)

**likes/serializers.py**

![](/docs/likes2.png)

**likes/models.py**

![](/docs/likes1.png)

**interested/views.py**

![](/docs/interested4.png)

**interested/urls.py**

![](/docs/interested3.png)

**interested/serializers.py**

![](/docs/interested2.png)

**interested/models.py**

![](/docs/interested1.png)

**followers/views.py**

![](/docs/followers4.png)

**followers/urls.py**

![](/docs/followers3.png)

**followers/serializers.py**

![](/docs/followers2.png)

**followers/models.py**

![](/docs/followers1.png)

**events/views.py**

![](/docs/events4.png)

**events/urls.py**

![](/docs/events3.png)

**events/serializers.py**

![](/docs/events2.png)

**events/models.py**

![](/docs/events1.png)

**contact/views.py**

![](/docs/contact4.png)

**contact/urls.py**

![](/docs/contact3.png)

**contact/serializers.py**

![](/docs/contact2.png)

**contact/models.py**

![](/docs/contact1.png)

**comments/views.py**

![](/docs/comment4.png)

**comments/urls.py**

![](/docs/comment3.png)

**comments/serializers.py**

![](/docs/comment2.png)

**comments/models.py**

![](/docs/comment1.png)

[Back to top](#table-of-contents)

## Manual Testing
- This project was tested manually several times throughout the development, ensuring the database was being updated as expected when creating, reading, updating or deleting data, where appropriate.
- Manually verified each url path created works and opens without error.
- Verified that the CRUD functionality is available in each app via the development version: Comments, Contact, Events, Interested, Followers, Likes, Posts and Profile.

### Comments
- List View (Read, Create if logged in)
- List View (Read if not logged in)
- Detail View (Read, Update, Delete if owner)
- Detail View (Read if not owner)
- Detail View (Read if not logged in)

### Contact
- Logged in user can create a contact message

![](/docs/contact_list.png)

![](/docs/contact_list_loggedin.png)

### Events 
- List View (Read, Create if logged in)
- List View (Read if not logged in)
- Detail View (Read, Update, Delete if owner)
- Detail View (Read if not owner)
- Detail View (Read if not logged in)

### Interested
- List View (Read, Create if logged in)
- List View (Read if not logged in)
- Detail View (Read, Delete if owner)
- Detail View (Read if not owner)
- Detail View (Read if not logged in)

### Followers
- List View (Read, Create if logged in)
- List View (Read if not logged in)
- Detail View (Read, Delete if owner)
- Detail View (Read if not owner)
- Detail View (Read if not logged in)

### Likes
- List View (Read, Create if logged in)
- List View (Read if not logged in)
- Detail View (Read, Delete if owner)
- Detail View (Read if not owner)
- Detail View (Read if not logged in)

### Posts
- List View (Read, Create if logged in)
- List View (Read if not logged in)
- Detail View (Read, Update, Delete if owner)
- Detail View (Read if not owner)
- Detail View (Read if not logged in)

![](/docs/posts_loggedout.png)

![](/docs/posts_loggedinowner.png)

### Profile
- List View (Read if logged in)
- List View (Read if not logged in)
- Detail View (Read, Update if owner)
- Detail View (Read if not owner)
- Detail View (Read if not logged in)

[Back to top](#table-of-contents)