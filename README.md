# OAuth
User login using OAuth

Visit the Google Developers Console at https://console.developers.google.com and create a new project. In the "APIs & auth" section, click on "Credentials", and then click the "Create a new Client ID" button. Select "Web Application" for the application type, and click the "Configure consent screen" button. Put in your application information, and click Save. Once you’ve done that, you’ll see two new fields: "Authorized JavaScript origins" and "Authorized redirect URIs". Set the authorized redirect URI to http://localhost:5000/login/google/authorized, and click "Create Client ID".
