# !streamlit run 1_app/app.py --server.port $CDSW_APP_PORT --server.address 127.0.0.1
import subprocess

print(subprocess.run(["streamlit run ./1_app/app.py --server.port $CDSW_APP_PORT --server.address 127.0.0.1"], shell=True))