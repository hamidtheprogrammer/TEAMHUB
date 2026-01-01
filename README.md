# TEAMHUB
![Last Commit](https://img.shields.io/github/last-commit/hamidtheprogrammer/TEAMHUB)
![Status](https://img.shields.io/badge/status-work%20in%20progress-yellow)
![Version](https://img.shields.io/badge/version-0.1.0--alpha-orange)

## Overview
TeamHub is a minimal backend-only internal SaaS that centralizes team, project, and user management for an organization, providing secure access control, administrative oversight, and basic lifecycle communication via email. The app is built to practice agile software development life cycle workflows, testing, documentation, and devsecops pipelines.

## Current Features
- Authentication and authorization (In progress)
- Email notification - For this project, email sending is intentionally stubbed due to domain verification requirements. In development mode, verification tokens are returned in the API response for testing purposes. In production, this service would integrate with a transactional email provider

## Planned features (Not yet implemented)
- Team and project management
- Admin controls

## Prerequisites
- Postgresql 
- python 3.+

## Tech Stack
- FastAPI, python, pydantic
- Postgres
- Github actions

## Getting started

### Environment variables
port= (add your desired port number e.g 8000)
DATABASE_URL=(add your postgresql url e.g "postgresql://username@localhost:5432/teamhub")

### Clone and install
```bash
git clone https://github.com/hamidtheprogrammer/TEAMHUB.git
cd app
pip3 install
python3 main.py
```


## Folder structure

```
app/ # main folder
├─ api/ # routes / schemas
├─ config/ # database config / env settings
├─ models/ # database models
├─ repositories/ # database querying
├─ scripts/ # database seed
├─ tests/ # integration tests
├─ utils/ # password hash / JWT token generation
├─ main.py # root file
└─ README.md # you are here
```

## Tests
(Not yet implemented)

## Documentation index
- Product requirement -> [app/docs/product-requirements.md](app/docs/product-requirements.md)
- System architecture -> [app/docs/system-architecture.md](app/docs/system-architecture.md)
- API documentation -> [app/docs/api](app/docs/api)
- Extended Entity Relational Database -> [app/docs/EERD.md](app/docs/EERD.md)
- Sequence diagrams -> [app/docs/sequence-diagrams](app/docs/sequence-diagrams)
