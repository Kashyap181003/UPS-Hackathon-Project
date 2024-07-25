### Project Title
**UPS Hackathon Project**

### Project Description
This project is a web application designed to streamline the process of validating and storing product information. The application utilizes various Google Cloud Platform (GCP) services, including Vertex AI for generating product descriptions and Firestore as a NoSQL database for storing the data. The core functionalities of the application include:

1. **Product URL Processing:**
   - Users can input a product URL, which is then processed to extract relevant information.

2. **Description Generation:**
   - The extracted product information is used to generate descriptive content using Vertex AI.

3. **Data Validation:**
   - The generated descriptions and extracted information are displayed to the user for validation.

4. **Data Storage:**
   - Validated data is stored in a Firestore NoSQL database.

5. **Data Display and Download:**
   - Users can view the stored data and download it as an Excel file for further analysis or reporting.

### Key Features
- **User-Friendly Interface:** Built with Flask, the application provides an intuitive web interface for interacting with the system.
- **Google Cloud Integration:** Utilizes GCP services such as Vertex AI for natural language processing and Firestore for data storage.
- **Scalable and Flexible:** Designed to handle a variety of product information, making it adaptable to different use cases.
- **Secure and Reliable:** Incorporates Google Cloud's robust security features to ensure data integrity and privacy.

### Technologies Used
- **Python 3.7 or higher:** The core programming language used for developing the application.
- **Flask:** A lightweight WSGI web application framework for building the web interface.
- **Google Cloud SDK:** A set of tools for managing resources and applications hosted on GCP.
- **Firestore:** A scalable, flexible database for mobile, web, and server development from Firebase and Google Cloud Platform.
- **Vertex AI:** A suite of machine learning tools provided by Google Cloud for building, deploying, and scaling ML models.

### Components
1. **Frontend:**
   - HTML templates (`base.html`, `index.html`, `validatedata.html`, `display.html`) for rendering the user interface.
   - CSS (`styles.css`) for styling the web pages.

2. **Backend:**
   - Flask routes (`app.py`, `views.py`) to handle user requests and application logic.
   - Service scripts (`GenAI.py`, `web_scrape.py`, `WebScrapping.py`, `HTSPrediction.py`, `HTSPred.py`) for processing product data and interacting with GCP services.
   - Model scripts (`model.py`) for interacting with the Firestore database.

3. **Configuration:**
   - `requirements.txt` listing all the dependencies required to run the application.
   - GCP service account credentials (`qwiklabs-gcp-04-091cbe4fed8b`) for authenticating API requests.

### Table of Contents
1. [Installation](#installation)
2. [Setup](#setup)
3. [Usage](#usage)
4. [Project Structure](#project-structure)
5. [API Endpoints](#api-endpoints)
6. [License](#license)

### Installation

#### Prerequisites
Before you begin, ensure you have the following software installed on your system:
- **Python 3.7 or higher**
- **Google Cloud SDK**
- **Git** (for cloning the repository)

#### Step-by-Step Installation Guide

1. **Clone the Repository:**
   First, clone the project repository from GitHub to your local machine:
   ```bash
   git clone https://github.com/yourusername/UpsHackathonProject.git
   cd UpsHackathonProject
   ```

2. **Install Required Packages:**
   Install the necessary Python packages listed in the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Google Cloud SDK:**
   - **Install the Google Cloud SDK:**
     Follow the instructions [here](https://cloud.google.com/sdk/docs/install) to install the Google Cloud SDK on your system.
   - **Initialize the SDK and Authenticate:**
     Initialize the Google Cloud SDK and authenticate using your Google account:
     ```bash
     gcloud init
     gcloud auth application-default login
     ```
     
4. **Configure Firestore:**
   - **Create a Firestore Database:**
     In your GCP project, create a Firestore database. You can follow the guide [here](https://cloud.google.com/firestore/docs/quickstart).
   - **Update Firestore Configuration:**
     Ensure your Firestore database is set up with the necessary collections and documents as per your project requirements.

5. **Configure Vertex AI:**
   - **Set Up Vertex AI:**
     In your GCP project, set up Vertex AI. You can find the setup instructions [here](https://cloud.google.com/vertex-ai/docs/start).
   - **Ensure Permissions:**
     Make sure your service account has the necessary permissions to access Vertex AI services.

6. **Run the Application:**
   Finally, start the Flask application using the following command:
   ```bash
   flask run
   ```
   This will start the development server, and you can access the application by navigating to `http://127.0.0.1:5000/` in your web browser.

### Setup

1. **Set Up Environment Variables:**
   The project relies on environment variables for configuration. Create a `.env` file in the root directory of the project and add the following variables:
   ```plaintext
   GOOGLE_CLOUD_PROJECT=<your-gcp-project-id>
   FIRESTORE_COLLECTION=<your-firestore-collection-name>
   ```
   
2. **Service Account Configuration:**
   Ensure that the service account JSON key (`qwiklabs-gcp-04-091cbe4fed8b`) is placed in the root directory of the project. This file contains the credentials required to authenticate and interact with Google Cloud services.

3. **Firestore Configuration:**
   Make sure your Firestore database is set up with the necessary collections and documents. You can create and manage your Firestore database through the Google Cloud Console. Follow these steps to configure Firestore:
   - Open the [Firestore Console](https://console.cloud.google.com/firestore).
   - Select your project.
   - Create a new Firestore database if you haven't already.
   - Create a collection that matches the name specified in your `.env` file.

4. **Vertex AI Configuration:**
   Set up Vertex AI in your Google Cloud project:
   - Open the [Vertex AI Console](https://console.cloud.google.com/vertex-ai).
   - Ensure that Vertex AI API is enabled for your project.
   - Set up any required resources, such as datasets and models, as per your project needs.

### Usage

This section provides detailed instructions on how to use the Project once it is set up and running.

#### Accessing the Application
1. **Start the Application:**
   Run the Flask development server using the following command:
   ```bash
   flask run
   ```

2. **Open the Application in a Browser:**
   Open your web browser and navigate to `http://127.0.0.1:5000/` to access the application.

#### Features and User Interface

1. **Home Page:**
   - **URL:** `http://127.0.0.1:5000/`
   - **Functionality:** Provides an interface to input a product URL for processing.
   - **Usage:**
     - Enter the product URL in the input field.
     - Click the "Submit" button to process the URL.

2. **Validate Data Page:**
   - **URL:** `http://127.0.0.1:5000/process_url`
   - **Functionality:** Displays the product details and generated descriptions, allowing the user to validate and submit the data.
   - **Usage:**
     - Review the product details and generated descriptions.
     - Click the "Submit Data" button to store the validated data in Firestore.

3. **Display Data Page:**
   - **URL:** `http://127.0.0.1:5000/display`
   - **Functionality:** Displays the latest products stored in the Firestore database and provides an option to download the data as an Excel file.
   - **Usage:**
     - Review the displayed product data.
     - Click the "Download Excel File" button to download the data as an Excel file.

#### Data Flow and Interaction

1. **Input Product URL:**
   - User inputs a product URL on the home page and submits the form.

2. **Process URL:**
   - The application processes the URL to extract product information and generate descriptions using Vertex AI.
   - Extracted data and generated descriptions are displayed on the Validate Data page.

3. **Validate Data:**
   - User reviews and validates the displayed data.
   - User submits the validated data, which is then stored in the Firestore database.

4. **Display Data:**
   - User can view the latest data stored in Firestore on the Display Data page.
   - User can download the displayed data as an Excel file.

By following these usage instructions, users can effectively interact with the UI to process, validate, store, and retrieve product information.

### Project Structure

The UPS Hackathon Project is organized into several directories and files, each serving a specific purpose. Below is an overview of the project structure:

```plaintext
UpsHackathonProject/
├── __init__.py                       # Initialization file for the Flask application
├── app.py                            # Main Flask application file containing routes
├── templates/                        # Directory for HTML templates
│   ├── base.html                     # Base template for the application
│   ├── index.html                    # Template for the home page
│   ├── validatedata.html             # Template for the data validation page
│   ├── display.html                  # Template for displaying stored data
├── services/                         # Directory for service scripts
│   ├── GenAI.py                      # Script for interacting with Vertex AI
│   ├── web_scrape.py                 # Script for web scraping product data
│   ├── WebScrapping.py               # Another web scraping script (possibly different functionality)
│   ├── HTSPrediction.py              # Script for HTS predictions
│   ├── HTSPred.py                    # Another script related to HTS predictions
├── model/                            # Directory for model scripts
│   ├── model.py                      # Script for interacting with Firestore database
├── static/                           # Directory for static files
│   ├── css/                          # Directory for CSS files
│   │   ├── styles.css                # Main stylesheet for the application
│   ├── images/                       # Directory for image files
│   │   ├── icon.png                  # Icon image used in the application
├── requirements.txt                  # File listing all the dependencies required for the project
├── qwiklabs-gcp-04-091cbe4fed8b  # GCP service account credentials
└── README.md                         # README file for the project (this document)
```

### Detailed Breakdown

#### `__init__.py`
This file is used to initialize the Flask application and configure necessary settings.

#### `app.py`
The main Flask application file that contains the route definitions and application logic for handling requests and rendering templates.

#### `templates/`
This directory contains HTML templates used by the Flask application to render web pages. Templates extend from a base template (`base.html`) to ensure consistent layout and styling.

- **`base.html`**: The base template that includes common HTML structure and elements.
- **`index.html`**: The home page template where users can input product URLs.
- **`validatedata.html`**: The template for displaying and validating product data.
- **`display.html`**: The template for displaying stored product data from Firestore.

#### `services/`
This directory contains various service scripts that handle different functionalities:

- **`GenAI.py`**: Script for generating product descriptions using Vertex AI.
- **`web_scrape.py`**: Script for scraping product data from given URLs.
- **`WebScrapping.py`**: Another script for web scraping, potentially with different methods or targets.
- **`HTSPrediction.py`**: Script for making HTS (Harmonized Tariff Schedule) predictions.
- **`HTSPred.py`**: Another script related to HTS predictions.

#### `model/`
This directory contains model scripts that interact with the Firestore database:

- **`model.py`**: Script that defines the Firestore database interaction logic.

#### `static/`
This directory contains static files such as CSS and images:

- **`css/`**: Directory for CSS files.
  - **`styles.css`**: Main stylesheet that defines the styles for the application.
- **`images/`**: Directory for image files.
  - **`icon.png`**: Icon image used in the application header.

#### `requirements.txt`
A text file that lists all the dependencies required to run the project. These dependencies can be installed using `pip`.

#### `qwiklabs-gcp-04-091cbe4fed8b`
The JSON file containing GCP service account credentials needed to authenticate API requests and interact with Google Cloud services.

### API Endpoints

This project exposes several API endpoints to handle various functionalities related to product data processing, validation, and storage. Below is a detailed description of each endpoint:

#### 1. Home Page
- **URL:** `/`
- **Method:** `GET`
- **Description:** Displays the home page where users can input a product URL for processing.
- **Response:** Renders the `index.html` template.

#### 2. Process URL
- **URL:** `/process_url`
- **Method:** `POST`
- **Description:** Accepts a product URL from the user, processes the URL to extract product information, and generates descriptions using Vertex AI. The extracted data and generated descriptions are displayed to the user for validation.
- **Request Data:**
  - `productUrl`: The URL of the product to be processed.
- **Response:** Renders the `validatedata.html` template with the extracted product data and generated descriptions.

#### 3. Submit Description
- **URL:** `/submit_description`
- **Method:** `POST`
- **Description:** Submits the validated product data and generated descriptions to the Firestore database.
- **Request Data:**
  - `json_data`: The JSON string containing the validated product data.
  - `generated_descriptions`: The generated descriptions for the product.
- **Response:** Redirects to the home page.

#### 4. Display Data
- **URL:** `/display`
- **Method:** `GET`
- **Description:** Displays the latest product data stored in the Firestore database.
- **Response:** Renders the `display.html` template with the product data fetched from Firestore.

#### 5. Download Excel
- **URL:** `/download_excel`
- **Method:** `GET`
- **Description:** Downloads the product data stored in Firestore as an Excel file.
- **Response:** Sends the generated Excel file as an attachment to the user.

### Summary of Endpoints

| URL                  | Method | Description                                                            | Request Data                                           | Response                          |
|----------------------|--------|------------------------------------------------------------------------|--------------------------------------------------------|-----------------------------------|
| `/`                  | GET    | Displays the home page where users can input a product URL.            | None                                                   | Renders `index.html`              |
| `/process_url`       | POST   | Processes the product URL and displays the extracted data for validation. | `productUrl` (URL of the product)                      | Renders `validatedata.html`       |
| `/submit_description`| POST   | Submits the validated product data to Firestore.                       | `json_data` (validated product data), `generated_descriptions` | Redirects to the home page        |
| `/display`           | GET    | Displays the latest product data from Firestore.                       | None                                                   | Renders `display.html`            |
| `/download_excel`    | GET    | Downloads the product data as an Excel file.                           | None                                                   | Sends the Excel file as an attachment |

### Usage Examples

#### Example 1: Submitting a Product URL
- **Step 1:** Navigate to the home page (`http://127.0.0.1:5000/`).
- **Step 2:** Enter a product URL and click "Submit".
- **Step 3:** The `process_url` endpoint processes the URL and displays the extracted data for validation.

#### Example 2: Validating and Submitting Data
- **Step 1:** After processing the URL, review the extracted product data and generated descriptions.
- **Step 2:** Click "Submit Data" to store the validated data in Firestore via the `submit_description` endpoint.

#### Example 3: Viewing Stored Data
- **Step 1:** Navigate to the display page (`http://127.0.0.1:5000/display`).
- **Step 2:** View the latest product data stored in Firestore.

#### Example 4: Downloading Data as Excel
- **Step 1:** On the display page, click "Download Excel File".
- **Step 2:** The `download_excel` endpoint generates and downloads an Excel file containing the product data.

