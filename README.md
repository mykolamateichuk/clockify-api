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

4) Either create .env file or set environment variable in terminal
    
    **Create .env file**

    Create `.env` file and paste this line in it `CLOCKIFY_API_KEY={your api key}`

    **Set environment variable in terminal**
    
    MacOS
    
    ```
    export CLOCKIFY_API_KEY={your api key}
    ```
   
    Windows 

    ```
    set CLOCKIFY_API_KEY={your api key}
    ```

5) Launch script

    ```
    python clockify_report.py
    ```
