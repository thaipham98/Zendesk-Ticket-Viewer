# Zendesk Ticket Viewer



Zendesk Ticket Viewer is a CLI-based application where users can retrieve information about a ticket system. Users have the options to view multiple tickets at once through page index, or view a single ticket's details. This is an implementation of the Zendesk Intern Coding Challenge 2021.



## Usage



1. Clone this Github repo.
2. Open terminal of choice and cd into the Zendesk-Ticket-Viewer directory.
3. First we'll need to install dependencies by entering:



```bash
pip install -r requirements.txt
```
4. To run the application (user instructions available upon opening), enter:
```bash
python3 src/main.py
```
5. To run unit tests, enter:
```bash
pytest src/api_test.py
```
## Repo Content
1. `README`:
Containing information about the repo and its usage.
2. `src/`: Containing source code and tests, including:
- `main.py`: Main file to handle user interactions and route to correct API functions.
- `api.py`: API handlers (retrieve ticket entries through HTTP requests, handle pagination, etc...)
- `api_test.py`: Unit test file for `api.py`.
- `helper.py`: Printing helper functions.




## Summary & Caveats
### Summary
The application is an attempt for the Zendesk coding challenge. Specifically, it contains:
- All required basic functionalities as stated in the challenge such as pagination, options to view all, view one ticket, or quit the application.
- An easy to use UI with handling of corner cases or invalid user inputs, HTTP error handling.
- Design separating API handlers from user-interaction handlers and helper functionalities.
- Preliminary unit tests.
- README and easy dependency installations.
### Caveats
The project can be improved given more time, for examples in some areas like:
- Robustness: More extensive testing and design to bring more OOP or other design patterns (MVC) to increase robustness and maintenance ease.
- Scalability: Currently, the application fetches all data upon the first viewing request, however this might make the first viewing request slower than the rest and grow worst as the database of ticket increases in size. Since the viewing is limited per page size, in the future, we can optimize it to fetch per page request to make it more scalable.
