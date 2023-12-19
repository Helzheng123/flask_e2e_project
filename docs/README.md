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
- Authorization with Google OAuth to authenticate the user with their google account
- API Service with the API endpoint hosted within Flask's Backend
- Sentry.io for logging
- Docker for Containerization
- Azure Cloud Deployment

## Steps to run Web Service:

### Run without Docker locally:
1. First, clone your GitHub repository into the local environment with ```git clone https://github.com/Helzheng123/flask_e2e_project.git```.
2. Once you finish cloning it, change the directory with ```cd flask_e2e_project``` then ```cd app```.
3. Then in the terminal, type ```python app.py``` to run the application. Use the link that appears and it will redirect you to the Flask App.

### Run with Docker locally:
1. Follow the first two steps in the steps for running without docker locally.
2. To begin, create a [Dockerfile](https://github.com/Helzheng123/flask_e2e_project/blob/main/app/Dockerfile).
3. Then create the Docker image by typing ```docker build -t <name> .```
4. Then do ```docker images``` to show the docker images. Make sure your ```<name>``` is there.
5. Then run the command with ```docker run -d -p 5000:5000 <name>```
6. Type in ```docker ps``` to check your docker container information.
7. When you are done with your Docker image, you can stop the image from running with ```docker stop <container ID>```
8. If needed, you can delete images with ```docker system prune -a -f```
For example:
![image](https://github.com/Helzheng123/flask_e2e_project/assets/123939070/4d5c0376-aabe-4fe7-8afd-3034a0b2d92e)

 
### Deploy it through Cloud (Azure):
1. Follow the first two steps in the steps for running without docker locally.
2. In the Google Shell terminal, you will need to install [AZURE CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt) with this: ```curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash```. Copy and paste the line in and enter.
3. Then type in ```az```. Type in ```az login --use-device-code``` and wait for a link and a code to appear in the terminal. Copy the code and press the link to log in to your Azure account. This will help connect your Google Shell with your Azure account.
4. Log in to your [Azure account](https://azure.microsoft.com/en-us/). Navigate to **Resource Group** and create a new Resource Group with a unique name. Press **Review and Create**. 
5. Head back to Google Shell and in the terminal, type in ```az account list --output table``` to make sure you have the correct subscription for your Azure account. Make sure your subscription is correct.
In my case, the subscription is **Azure for Students**. If the subscription has not defaulted to the desired one, type in ```az account set --subscription <paste the desired SubscriptionId here>```.
6. Now type in ```az group list```.
7. Type in ```az webapp up --resource-group <resource group that you named> --name <replace with what you would like to name the webapp> --runtime PYTHON:3.9 --sku B1```. Once entered, the Azure app service will create the web app for you. This step may take a while to load.
8. Once the service completes the deployment, you can go to **App Service** in the Azure site to deploy the web app. Choose the appropriate web app. Then you will be redirected to the overview of the web app. The link for your application will be found at the **Default domain**. Click on the link and you will now be redirected to your web application.
For example:
![image](https://github.com/Helzheng123/flask_e2e_project/assets/123939070/c5f991cb-f11a-443f-8077-6aac0ddb378d)

![image](https://github.com/Helzheng123/flask_e2e_project/assets/123939070/dc830929-24b5-4a0f-8185-d7a23460b0d3)

[helenwebappfinal.azurewebsites.net](helenwebappfinal.azurewebsites.net)

However, I ran into issues:
![image](https://github.com/Helzheng123/flask_e2e_project/assets/123939070/b8051db7-a8ea-457b-b8c1-031badf4e9c2)


## Template of the .env file:
For the Google OAuth, I used this:
```
GOOGLE_CLIENT_ID = <place in the client-id for your web application from google cloud>
GOOGLE_CLIENT_SECRET = <place in client-secret also from google cloud>
```

For the MySQL connection and for migrations:
```
DB_HOST = <I placed my host link from azure but if it GCP place the IP address>
DB_DATABASE = <your databasename>
DB_USERNAME = <username>
DB_PASSWORD = <password>
DB_PORT = 3306
DB_CHARSET = utf8mb4
```

## Screenshots and Video:
All of the Screenshots can be found in the [```docs```](https://github.com/Helzheng123/flask_e2e_project/tree/main/docs) folder.

Here is the [video](https://github.com/Helzheng123/flask_e2e_project/blob/main/docs/NYC%20Annual%20Report%20-%20Google%20Chrome%202023-12-18%2022-26-20.mp4) on running the Flask App locally showing the Google Authorization:

Authenticate Page:

![image](https://github.com/Helzheng123/flask_e2e_project/assets/123939070/bbb4521e-430f-4422-8a47-5952de2e205e)

Home Page:

![image](https://github.com/Helzheng123/flask_e2e_project/assets/123939070/fab9583e-884e-4951-9c11-a97ade6cafd1)

Dashboard Page:

![image](https://github.com/Helzheng123/flask_e2e_project/assets/123939070/5f851d83-12d4-49e3-9bb0-e4a4f05a23c5)

HIV Page:

![image](https://github.com/Helzheng123/flask_e2e_project/assets/123939070/5ea847c1-03f4-4d39-a6c8-532947b02b87)

AIDS Page:

![image](https://github.com/Helzheng123/flask_e2e_project/assets/123939070/8d4cd9d8-0402-4dfd-8b71-caaf2ae0ae8c)

Deaths Page:

![image](https://github.com/Helzheng123/flask_e2e_project/assets/123939070/d4676731-e2de-4899-bc04-5916b9715eaf)

Report Page:

![image](https://github.com/Helzheng123/flask_e2e_project/assets/123939070/b1a6b7ad-280d-406d-9ece-b07273adf3d3)

Contact Us Page:

![image](https://github.com/Helzheng123/flask_e2e_project/assets/123939070/65f7b709-117f-4db9-ad85-18c44e3f8229)

Web App Page on Azure:

![image](https://github.com/Helzheng123/flask_e2e_project/assets/123939070/4d31b12f-5b08-4834-b3b2-d86aa379a2be)

Cloud Deployment via Azure:

![image](https://github.com/Helzheng123/flask_e2e_project/assets/123939070/5ba7cabe-78c7-43ea-8156-5df235150a10)

API Function App Page:

![image](https://github.com/Helzheng123/flask_e2e_project/assets/123939070/efb8a98e-a906-4889-9067-61b168c4110a)

API:

![image](https://github.com/Helzheng123/flask_e2e_project/assets/123939070/32198192-5c0f-4eb5-9195-0b656a6f4717)

Dockerfile output:

![image](https://github.com/Helzheng123/flask_e2e_project/assets/123939070/fb4c43d0-eab4-4553-9cb7-905bb9823e7f)
