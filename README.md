# dl_probs
Download Problems from codechef and store in pdf

## Setup
1. Install Webkit HTML to PDF
	1. For Ubuntu/Debian:
		`sudo apt-get install wkhtmltopdf`
	2. Mac OS X:
		`brew install wkhtmltopdf`
	3. Windows:
		1. Download wkhtmltopdf from [releases](https://github.com/wkhtmltopdf/wkhtmltopdf/releases)
		2. Install the release [wkhtmltox-[version_number].msvc[2015|2019]-win[32|64].exe]
		3. Make sure it's in the PATH
2. Install the python modules:
	`pip install -r requirements.txt`
3. Run the script from the root directory of this repository