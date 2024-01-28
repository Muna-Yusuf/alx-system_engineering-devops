what is a server?
A server refers to both the hardware and software that provide services or resources to other computers. The server hardware is the physical machine designed to handle the demands of serving multiple clients, and the server software includes programs like operating systems, web servers, database servers, and more.

What is the role of the domain name?
It translates IP addresses to be a human-readable and memorable label for accessing resources on the Internet.

What type of DNS record www is in www.foobar.com?
Is a CNAME record.

What is the role of the web server?
To handle HTTP requests from clients (usually web browsers) and deliver static content.

What is the role of the application server?
Is responsible for executing server-side code and managing dynamic content generation.

What is the role of the database?
Stores, manages, and retrieves data required by the web application. It provides a structured storage system for the application's data.

What is the server using to communicate with the computer of the user requesting the website?
Occurs over the Hypertext Transfer Protocol (HTTP) or its secure version, HTTPS (HTTP Secure).


ISSUES:
SPOF (Single Point Of Failure) -> In this design, if any server fail, the entire system will fail. So, there're many SPOF.
Downtime when maintenance needed -> When we need to run some maintenance checks on any component, they have to be put down or the server has to be turned off. Since there's only one server, the website would be experiencing a downtime.
Cannot scale if too much incoming traffic -> when the server receives many requests, it is impossible to scale up.
