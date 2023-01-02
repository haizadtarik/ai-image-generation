# AI Image Generation Web App

This web app generate image using Stable Diffusion v2.1 from Stability AI. 
The web app use FastAPI for the backend and STreamlit for the front end
The model is obtained from [Huggingface Stable Diffusion v2-1 Model Card ](https://huggingface.co/stabilityai/stable-diffusion-2-1) 
Please comply with the term of use as indicated on the model card page when using the web app

## Setup

1. Git clone the repo
    ```
    git clone https://github.com/haizadtarik/ai-image-generation.git
    ```

2. Install Dependencies
    ```
    pip install -r requirements.txt
    ```

## Run

1. Bring up the backend server
    ```
    python server.py
    ```

2. Bring up the web app
    ```
    streamlit run app.py
    ```
    
    or if the backend server is running on different system

    ```
    streamlit run app.py -- <BACKEND_URL>
    ```


