# Playwright Python Automation Framework

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Playwright](https://img.shields.io/badge/Playwright-1.44.0-green)
![Pytest](https://img.shields.io/badge/Pytest-8.2.0-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-In%20Progress-brightgreen)

> Automation Framework built with Playwright + Python.  
> Designed with scalability, maintainability, and CI/CD readiness in mind.

---

## Framework Architecture
```
playwright-python-framework/
│
├── pages/          # Page Object Models (POM)
├── tests/          # All test files
├── core/           # Browser setup & driver factory
├── utils/          # Helpers & data generators
├── reports/        # Allure & HTML test reports
├── data/           # JSON/CSV test data
├── .github/
│   └── workflows/  # CI/CD GitHub Actions pipelines
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Getting Started

### Prerequisites
- Python 3.11+
- pip

### Installation
```bash
# Clone the repo
git clone https://github.com/anasamante/playwright-python-framework.git
cd playwright-python-framework

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```