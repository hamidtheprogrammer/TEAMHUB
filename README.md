# TEAMHUB
![Last Commit](https://img.shields.io/github/last-commit/hamidtheprogrammer/TEAMHUB)
![Status](https://img.shields.io/badge/status-work%20in%20progress-yellow)
![Version](https://img.shields.io/badge/version-0.1.0--alpha-orange)

## Overview
TeamHub is a minimal backend-only internal SaaS that centralizes team, project, and user management for an organization, providing secure access control, administrative oversight, and basic lifecycle communication via email. The app is built to practice agile software development life cycle workflows, testing, documentation, and devsecops pipelines.

## Planned features (Not yet implemented)
- Authentication and authorization
- Team and project management
- Admin controls
- Email notification
- Background tasks
- Cache

## Tech Stack
- FastAPI, python, pydantic
- Postgres, rabitmq
- Docker, Github actions

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

## Getting started
### Clone and install
```bash
git clone https://github.com/hamidtheprogrammer/TEAMHUB.git
cd app
pip3 install
python3 main.py
```

## Environment variables
port= 

## Tests
(Not yet implemented)


