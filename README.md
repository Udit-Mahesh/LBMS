# ✨Library Management System✨
This project allows an admin to see details of books, members, staff and transactions like borrowing and returning that take place.
This project allows the admin to also update data in several tables by adding and deleting records.
Each page of this website has a specific search bar at the top-right corner to search for a particular record based on a particular value.

Technologies used:-
* ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
* ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]
* ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
* ![Jinja](https://img.shields.io/badge/Jinja-B41717?style=for-the-badge&logo=jinja&logoColor=white)

## Database schema
The database 'library' has the following tables:-
* books(book_id, book_name, author, publisher, author, date_of_entry)
* members(member_id, member_name, email, phone_no,membership_date)
* staff(staff_id, staff_name, role, email, password, phone_no, entry_date)
* transactions(transaction_id, book_id, member_name, issue_date, due_date, return_date)

## User Interface
### Homepage
<img width=1437 alt='Screenshot 2025-06-10 232036' src='https://github.com/user-attachments/assets/f3676905-bebb-48dd-a6da-c0ce6774f793'>

### Members
![Screenshot 2025-06-10 235234](https://github.com/user-attachments/assets/56009b11-e98a-4e69-b14d-e6b0f94f6863)

### Staff
![Screenshot 2025-06-10 235458](https://github.com/user-attachments/assets/326a38d0-87a1-402f-a74f-07eb26f6e56d)


### Transactions
![Screenshot 2025-06-10 235607](https://github.com/user-attachments/assets/ca5274d5-619c-4666-855b-88c680f3a09f)



<!--![Screenshot 2025-06-10 232036](https://github.com/user-attachments/assets/f3676905-bebb-48dd-a6da-c0ce6774f793)

**Udit-Mahesh/Udit-Mahesh** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
