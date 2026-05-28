Create the venv with Python 3.11 explicitly:

1. Navigate to your project folder:
cd C:\Users\user\Desktop\ML-AI-Data\Personal-Projects\Python

2. Create the venv using Python 3.11:
C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe -m venv jupyter-env

This uses the exact Python 3.11 path shown in your screenshot's error message.

3. Activate it:
jupyter-env\Scripts\activate

4. Install ipykernel and Jupyter:
pip install jupyter ipykernel notebook

5. Register the kernel:
python -m ipykernel install --user --name=jupyter-env --display-name "Python 3.11 (jupyter-env)"

Then in VS Code, click the kernel selector (top-right of your notebook) and pick "Python 3.11 (jupyter-env)".

You can verify it's using the right Python version anytime with:
python --version

It should say Python 3.11.x ✓