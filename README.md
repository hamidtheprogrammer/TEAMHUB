# TEAMHUB
![Last Commit](https://img.shields.io/github/last-commit/hamidtheprogrammer/TEAMHUB)
![Status](https://img.shields.io/badge/status-work%20in%20progress-yellow)
![Version](https://img.shields.io/badge/version-0.1.0--alpha-orange)
![Coverage](https://img.shields.io/codecov/c/github/hamidtheprogrammer/REPO)
![Build](https://github.com/hamidtheprogrammer/TEAMHUB/actions/workflows/ci.yml/badge.svg)


## Overview
TeamHub is a minimal backend-only internal SaaS that centralizes team, project, and user management for an organization, providing secure access control, administrative oversight, and basic lifecycle communication via email. The app is built to practice agile software development life cycle workflows, testing, documentation, and devsecops pipelines.

## Current Features
- Authentication and authorization (In progress)
- Email notification - For this project, email sending is intentionally stubbed due to domain verification requirements. In development mode, verification tokens are returned in the API response for testing purposes. In production, this service would integrate with a transactional email provider
- User management (admin)

## Planned features (Not yet implemented)
- view teams and projects (user)
- Team management (admin)
- Project management (admin)

## Prerequisites
- Postgresql 
- python 3.+

## Tech Stack
- FastAPI, python, pydantic
- Postgres
- Github actions

## Getting started

### Environment variables
```
port= (add your desired port number e.g 8000)
DATABASE_URL=(add your postgresql url e.g "postgresql://username@localhost:5432/teamhub")
MAILERSEND_API_KEY=(your mailer send api key - mail is not functional in this project)
MAIL_FROM_EMAIL=
MAIL_FROM_NAME=
FRONTEND_VERIFY_URL=http://localhost:3000/auth/verify
env="DEVELOPMENT"
SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
```

### Clone and install
```bash
# Clone the TEAMHUB repository from GitHub to your local machine
git clone https://github.com/hamidtheprogrammer/TEAMHUB.git

# Upgrade pip to the latest version to avoid any installation issues
python -m pip install --upgrade pip

# Install all Python dependencies listed in requirements.txt
# This ensures your environment has FastAPI, SQLAlchemy, Alembic, etc.
pip install -r requirements.txt

# Apply database migrations using Alembic
# This creates tables and updates schema to the latest version
alembic upgrade head 

# Start the FastAPI server with auto-reload enabled
# --reload will automatically restart the server when code changes
uvicorn app.main:app --reload 

# Optionally run tests using the command below
cd app
pytest

```


## Folder structure

```
├─app/ # main folder
│   ├─ api/ # routes / schemas
│   ├─ config/ # database config / env settings
│   ├─docs/  # ADRs, architecture diagrams, decisions
│   ├─ models/ # database models
│   ├─ repositories/ # database querying
│   ├─ scripts/ # database seed
│   ├─ tests/ # integration tests
│   ├─ utils/ # password hash / JWT token generation
│   ├─ main.py # root file
├─README.md # you are here
├─alembic/ #  migration folder
├─alembic.ini
├─requirements.txt #  packages
├─.env
├─.gitignore
```

## Documentation index
- Product requirement -> [app/docs/product-requirements.md](app/docs/product-requirements.md)
- System architecture -> [app/docs/system-architecture.md](app/docs/system-architecture.md)
- API documentation -> [app/docs/api](app/docs/api)
- Extended Entity Relational Database -> [app/docs/EERD.md](app/docs/EERD.md)
- Sequence diagrams -> [app/docs/sequence-diagrams](app/docs/sequence-diagrams)
