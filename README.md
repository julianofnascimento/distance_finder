Distance Finder APP

Run app locally:

To run the application locally with Docker, follow these instructions:

Execute the following commands in the terminal:

    docker build -t distance_finder .
    docker run -p 8000:8000 distance_finder

The app can be accessed locally at port 8000 using the following URLs:

    localhost:8000
    or
    127.0.0.1:8000

Routes:

The main route is where you input the source and destination addresses:

localhost:8000/

The history route displays previous searches:

localhost:8000/history

Comments and assumptions regarding the case:

I chose a simpler approach for the code structure, rather than a more sophisticated object-oriented approach, because the functionality is straightforward.

I used the address search open query in the Nominatim API, instead of the more strict search requiring all address fields. I understand this might generate unwanted results, as noticed during testing, but I opted for this solution because it makes the form cleaner and more direct.

The API can return multiple results for one query; therefore, I am selecting only the address at index 0 in the returned array.

For the layout of the templates, I used GPT to generate a simple Bootstrap based design.