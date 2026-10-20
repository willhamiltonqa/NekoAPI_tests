# Neko API tests
## Project purpose is to obtain deep understanding of creating fully automated testing solutions for RESTful APIs

Main topics which are covered in this project:
* 💻 BackEnd API testing
* 🤖 Test Automation with Python programing language & pyTest framework
* 🎨 Design Patterns in Automation Frameworks

### [Neko API](https://nekosapi.com/) is used as application under test. 
#### Technical documentation for Neko API can be found at **[here](https://api.nekosapi.com/v5/docs)**.

### Tech Stack 💻:
* 🐍 Python as main programming language
* 🛠️ Pytest as testing framework
* 🐳 Docker Engine for tests containerization

## Project Structure
`tests/` - folder that contains all tests of the project in which assertions apply

`conftest.py` - contains methods & arrangements required for API request

`requirements.txt` - contains names of libraries which is needed to be imported

`Dockerfile` - contains instructions for building the test container


## ▶️Getting Started
### Prerequisites

- Python 3.14
- `pip` for dependency management

### Installation

```bash
git clone https://github.com/willhamiltonqa/NekoAPI_tests.git
cd NekoAPI_tests
python3 -m venv .venv
source .venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Test  launch 🚀
Use default pytest default commands to run tests. 
For example, you can execute all tests buy running the following command in terminal:
```bash
pytest . -v
```

### 📄 License
This project is open-source and available under the MIT License.
