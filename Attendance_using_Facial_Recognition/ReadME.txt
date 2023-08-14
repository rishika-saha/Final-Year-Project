Attendance Mechanism Using Facial Recognition

We are using webcam.js to capture realtime webcam feed. On that image
we are applying harcascade to detect the face.

We have two Websites - Admin and Student Website

On the Admin Website, the administrator will upload the student details 
and images. The student id, name will be updated in the PostgreSQL
Database and each student's image will be updated against its id
in the Firebase Database.

On the Student Website, the student enter their roll number and click their image,
where the image will be compared with the image uploaded by the admin
using Siamese Model.

At the end of the month the database will be mailed to the concerned teacher and the database will be reset. 

Thats how the Database will be updated.