# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pathlib import Path
import streamlit as st

# Gets the absolute path of the current file
main_file_path = Path(__file__).resolve()

# Gets the directory containing the file
root_dir = main_file_path.parent

st.write(f"Main file path: {main_file_path}")
st.write(f"Project root directory: {root_dir}")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
