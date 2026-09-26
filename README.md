# HackForge – College Hackathon Registration & Management Platform

HackForge is a dynamic web application developed as part of the Cloud Computing and DevOps CCA 2. It provides a simple platform for students to register their teams for a college hackathon.

The application dynamically displays hackathon information, registered teams, available slots, and accepts new team registrations through a validated web form.

---

## Features

- Dynamic hackathon information displayed using Flask.
- Team registration through a web form.
- Input validation for team details and email address.
- Support for teams of 2–4 members.
- Displays registered teams dynamically.
- Displays the number of remaining team slots.
- JSON API for retrieving registered teams.
- Health-check endpoint for application monitoring.
- Automated testing using pytest.
- Code quality checking using flake8.
- Dockerized application.
- Automated CI/CD pipeline using GitHub Actions.
- Automated Docker health smoke testing.
- Automated deployment to Render.
- Running Git commit ID displayed in the application footer.

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.12 | Application development |
| Flask | Web framework |
| HTML5 | Page structure |
| CSS3 | User interface styling |
| pytest | Automated testing |
| flake8 | Code quality and linting |
| Docker | Application containerization |
| Git | Version control |
| GitHub | Source code hosting |
| GitHub Actions | CI/CD automation |
| Render | Cloud deployment |

---

## Project Structure

```text
HackForge/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── tests/
│   └── test_app.py
│
├── app.py
├── Dockerfile
├── .dockerignore
├── .flake8
├── .gitignore
├── requirements.txt
└── README.md


---

## Application Routes

| Route | Method | Description |
|---|---|---|
| `/` | GET | Displays the HackForge homepage |
| `/register` | POST | Registers a new hackathon team |
| `/api/teams` | GET | Returns registered teams in JSON format |
| `/health` | GET | Returns the application health status |

---

## Application Functionality

### Hackathon Information

The homepage dynamically displays:

- Hackathon name
- Tagline
- Date
- Venue
- Registration deadline
- Maximum number of teams
- Remaining available slots

### Team Registration

Students can register their hackathon team by entering:

- Team name
- Team leader name
- Email address
- Number of team members
- Project idea

The submitted information is processed by the Flask server and displayed dynamically on the homepage.

### Input Validation

The application validates:

- Required fields
- Email address
- Number of team members
- Maximum team capacity

Invalid registration requests are rejected with an appropriate HTTP error response.

---

## API Endpoints

### Get Registered Teams

```text
GET /api/teams
GET /health

---

## Automated Testing and Code Quality

HackForge uses **pytest** for automated testing and **flake8** for code quality checking.

### Running Tests

Run the following command:

```bash
python -m pytest

---

## Docker Support

HackForge is containerized using Docker to provide a consistent deployment environment.

### Build the Docker Image

```bash
docker build -t hackforge .

---

## CI/CD Pipeline

HackForge uses **GitHub Actions** to automate the process of testing, building, and deploying the application.

The pipeline follows this flow:

```text
Git Push / Pull Request
          ↓
       Lint
          ↓
       Tests
          ↓
    Docker Build
          ↓
 Docker Health Check
          ↓
  Deploy to Render
          ↓
     Live Website

     ---

## CI/CD Failure Demonstration

A failure scenario was intentionally created to verify that the CI/CD pipeline prevents an invalid version of the application from being deployed.

For the failure demonstration, the expected status code in the invalid-email test was intentionally changed to an incorrect value. This caused the automated test stage to fail.

The pipeline behaved as expected:

```text
Lint              ✓ Passed
Test              ✗ Failed
Docker Build      Skipped
Deploy to Render  Skipped

---

## Running the Application Locally

Follow these steps to run HackForge on a local Windows system.

### 1. Clone the Repository

```bash
git clone https://github.com/82nupur/HackForge.git
cd HackForge

---

## Git Workflow

Git and GitHub are used for version control and collaborative-style development practices.

The project was developed using separate branches for individual features and changes.

The workflow followed was:

```text
Create Feature Branch
        ↓
Develop and Test Feature
        ↓
Commit Changes
        ↓
Push Branch to GitHub
        ↓
Create Pull Request
        ↓
CI/CD Checks
        ↓
Merge into main

---

## Deployment

HackForge is deployed as a Docker-based web application on Render.

The Render service is configured to:

- Use the `main` branch of the GitHub repository.
- Build the application using the project's `Dockerfile`.
- Use `/health` as the health-check path.
- Keep Render Auto-Deploy disabled.
- Receive deployment triggers from the GitHub Actions CI/CD pipeline.

The deployment process is:

```text
GitHub Actions
      ↓
Docker Build & Health Check
      ↓
Render Deploy Hook
      ↓
Render
      ↓
Live HackForge Application

---

## Project Links

- **GitHub Repository:** https://github.com/82nupur/HackForge
- **Live Application:** https://hackforge-zlk0.onrender.com
- **GitHub Actions:** https://github.com/82nupur/HackForge/actions

---

## Deployment Verification

The successful GitHub Actions pipeline generated the following commit:

```text
92d59e4661a6baf74dcedadf6fa206da4e64fd69

---

## Learning Outcomes

Through the development and deployment of HackForge, the following concepts were practiced:

- Developing a dynamic web application using Flask.
- Implementing server-side form handling and input validation.
- Creating and testing REST-style API endpoints.
- Writing automated tests using pytest.
- Performing code quality checks using flake8.
- Containerizing an application using Docker.
- Using Git and GitHub for version control.
- Creating feature branches and Pull Requests.
- Designing a CI/CD pipeline using GitHub Actions.
- Performing Docker health checks before deployment.
- Using GitHub Secrets for secure deployment configuration.
- Deploying a containerized application to Render.
- Verifying the deployed application using the Git commit ID.

---

## Author

**Nupur Mehta**  
B.Tech Computer Science and Engineering  
MIT World Peace University, Pune

This project was developed as an individual submission for the Cloud Computing and DevOps CCA 2.