#!/bin/bash

exec python3 server.py &
exec streamlit run app.py