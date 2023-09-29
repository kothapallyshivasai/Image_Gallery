# Image_Gallery
Django Image Gallery with User Authentication

Project setup:
pip install django <br> 
cd image_gallery <br>
python manage.py makemigrations <br>
python manage.py migrate <br>
python manage.py runserver <br>

Description:
You've created a feature-rich image gallery web application using Django, a popular Python web framework. The application integrates seamlessly with the built-in SQLite database, making it easy to manage and store image data. One of the key features you've implemented is user authentication, which enhances security and ensures that only registered users can access and view the images within the gallery.

Key Features:

User Authentication: User authentication is the backbone of your image gallery. Users must register and log in to gain access to the gallery. This ensures that only authorized individuals can interact with the images.

User Registration: Users can create accounts by providing essential information like a username, password, and email address. Django's built-in authentication system manages user registration and password hashing, keeping user data secure.

Login System: Users can log in securely using their credentials. Django handles session management, ensuring that users remain logged in until they choose to log out.

Image Upload: Registered users can upload images to the gallery. This functionality is intuitive and user-friendly, allowing individuals to contribute to the gallery's content.

Image Display: Authenticated users can view all the images in the gallery. Images are displayed elegantly with details like title, date, and uploader's information.

Authorization Checks: Django's built-in authentication and authorization mechanisms prevent unauthorized users from accessing the gallery. This ensures data privacy and security.

User Profile: Users have their profiles where they can update their information and see their uploaded images.

Responsive Design: The gallery's user interface is designed to be responsive, adapting to various screen sizes and devices, ensuring a seamless user experience on desktops, tablets, and smartphones.

Database Integration: SQLite, a lightweight relational database, is integrated into the application to store image metadata, user information, and authentication data. This allows for efficient data management.

Security Measures: You've taken precautions to secure the application, including protecting against common web vulnerabilities like SQL injection, cross-site scripting (XSS), and cross-site request forgery (CSRF).

Scalability: The application is designed with scalability in mind, allowing for future expansion and the addition of new features.

User-Friendly Experience: The user interface is intuitive and aesthetically pleasing, enhancing the overall user experience.

Your Django-based image gallery with user authentication is a robust and secure platform for sharing and viewing images. It combines the power of Django's built-in features with the flexibility to expand and improve upon it as needed. It's an excellent foundation for building a community of users who can interact with and appreciate the images in your gallery.

![Screenshot (89)](https://github.com/kothapallyshivasai/Image_Gallery/assets/135272141/a456b178-0cbb-45d8-b8f5-141d157af8e5)
Login Page

![Screenshot (90)](https://github.com/kothapallyshivasai/Image_Gallery/assets/135272141/48be061b-8bb0-4ed5-89b9-8df516f7edd8)
Registration Page

![Screenshot (91)](https://github.com/kothapallyshivasai/Image_Gallery/assets/135272141/e15ffaae-656e-4439-8f75-f91fcd3ea088)
User Profile

![Screenshot (92)](https://github.com/kothapallyshivasai/Image_Gallery/assets/135272141/e8eec5f6-2ef4-415e-9a1f-13b7bfee91db)
Image Modifications to set public users to see the image or not

![Screenshot (93)](https://github.com/kothapallyshivasai/Image_Gallery/assets/135272141/658f6572-7fa5-4fc0-8d91-9a4f2cdd184d)
Pagination and Footer







