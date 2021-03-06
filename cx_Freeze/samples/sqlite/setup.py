# A setup script to demonstrate the use of sqlite3
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the script without Python

from cx_Freeze import setup, Executable

buildOptions = {}#dict(zip_include_packages=["*"], zip_exclude_packages=[])
executables = [Executable("test_sqlite3.py")]

setup(name='test_sqlite3',
      version='0.1',
      description='cx_Freeze script to test sqlite3',
      executables=executables,
      options=dict(build_exe=buildOptions))
