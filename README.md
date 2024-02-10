# Clockify API

### Installation

1) Clone the repository and go into the created folder
    
    ```
    git clone https://github.com/mykolamateichuk/clockify-api
    ```
   
    ```
    cd clockify-api
    ```

2) Create virtual environment

    MacOS
    ```
    python3 -m venv venv
    ```
   
    ```
    source venv/bin/activate
    ```
   
    Windows
    ```
    python -m venv venv
    ```
   
    ```
    .\venv\Scripts\activate
    ```

3) Install requirements

    ```
    pip install -r requirements.txt
    ```

4) Create .env file containing environment variables

    Create `.env` file and paste this lines in it with right values 
    ```
    CLOCKIFY_API_KEY={your api key}
    WORKSPACE_ID={your workspace id}
    PROJECT_ID={your project id}
    USER_ID={your user id}
    ```

5) Launch script

    ```
    python clockify_report.py
    ```
