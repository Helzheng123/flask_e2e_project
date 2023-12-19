# flask_e2e_project
A combination of the tools and services we learned this semester for HHA 504 Cloud Computing Health Informatics Professionals. 

# Final Assignment (Product / Web Service)

## Technologies (approaches) that will be used for the final assignment:  
- Github (Version Control)
- Flask (Python; Frotend & Backend)
- MySQL (Database via GCP or Azure)
- SQLAlchemy (ORM)
- .ENV (Environment Variables)
- Tailwind (Frontend Styling)
- Authorization (Google OAuth)
- API Service (Flask Backend)
- Logger and or Sentry.io (Debugging & Logging)
- Docker (Containerization)
- GCP or Azure (Deployment) 

## Web Service: 
 - This is a web service using Flask to display the data of the New York City Department of Health and Mental Hygiene. The data displays 2011-2021 report on HIV and AIDS. It contains the different Boroughs, UHFs and the different years that the data was collected. 
 - This Flask app is deployed on Azure.
 - There are 7 tabs that you can navigate to. When running the page, the first part will be the [Google Authentication](https://github.com/Helzheng123/flask_e2e_project/blob/main/docs/NYC%20Annual%20Report%20-%20Google%20Chrome%202023-12-18%2022-26-20.mp4). This can also be found in the [**Authenticate**](https://github.com/Helzheng123/flask_e2e_project/blob/main/docs/authenticate%20page.png) tab. The [**Home**](https://github.com/Helzheng123/flask_e2e_project/blob/main/docs/Home%20page.png) page shows a brief description of the web service. The [**HIV**](https://github.com/Helzheng123/flask_e2e_project/blob/main/docs/HIV%20page.png) page shows the number of HIV diagnoses, the rate, concurrent diagnoses, HIV-related death rate, and Non-HIV related death rate. The [**AIDS**](https://github.com/Helzheng123/flask_e2e_project/blob/main/docs/AIDS%20page.png) page shows the number of AIDS diagnoses and the rate. The [**Deaths**](https://github.com/Helzheng123/flask_e2e_project/blob/main/docs/Deaths%20page.png) page shows the number of deaths associated with HIV and AIDS along with the rate. The [**Reports**](https://github.com/Helzheng123/flask_e2e_project/blob/main/docs/Report%20page.png) page shows the borough, year, and UHFs associated with this dataset. The [**Contact Us**](https://github.com/Helzheng123/flask_e2e_project/blob/main/docs/contact%20us%20page.png) page shows a page to input any questions or concerns for this web service. 
  - All of the web service's functions can be found in the [```docs```](https://github.com/Helzheng123/flask_e2e_project/tree/main/docs) folder.

## Technologies Used:

- GitHub for the Version Control
- Flask for Python; Frotend & Backend
- MySQL Database via Azure
- SQLAlchemy (Object Relational Mapper) through migrations
- .env - Environment Variables
- Tailwind for Frontend Styling
- Authorization with Google OAuth
- API Service with the API endpoint hosted within Flask's Backend
- Sentry.io for logging
- Docker for Containerization
- Azure Cloud Deployment
