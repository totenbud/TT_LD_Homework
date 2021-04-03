### Tom Totenberg LD Test ###
This program gives you a button to test whether you're a currently invisible or visible hobbit. I'm sure there are no negative side effects to making yourself invisible!

It uses [PyQt5](https://pypi.org/project/PyQt5/) as an interface.

##### Build instructions #####
1. Install the LaunchDarkly Python SDK and PyQt5 by running `pip install -r requirements.txt`
2. Copy your SDK key and feature flag key from your LaunchDarkly dashboard into `InvisibilityChecker.py`
3. Run `python InvisibilityChecker.py`

##### Executable instructions #####
If you would prefer to not install PyQt5, you can instead directly launch the InvisibilityChecker.exe file included here. Note that it must be contained in the same directory as the 'images' folder.