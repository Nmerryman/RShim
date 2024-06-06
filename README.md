# RShim
This is a server that acts as a middleman between a redis server and outside connections. It should provide the minimum needed security to allow connections from outside the local network.

## There is no real consideration for security.
I wanted to provide a simple and generally available place to store low value data. 
The largest concern is likely the inability to limit the amount of data that an unauthenticated user can store. 
Due to the low importance of the project, and it's generality, I have not implemented any security measures that may help mitigate these issues as bandaid solutions will not  stop a determined person.

## Running
Simply run this command to get the basic thing to run.
`uvicorn main:app --reload`