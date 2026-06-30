# 🌿 GreenPulse — Plant & Sustainability Tracker

A creative web application for tracking plants, watering schedules, and sustainability tips.
Built as a **complete DevOps project** covering all rubric requirements.

---

## 🗂️ Project Structure

```
greenpulse/
├── app.py                          # Flask web application
├── requirements.txt                # Python dependencies
├── Dockerfile                      # Container configuration
├── docker-compose.yml              # Multi-container orchestration
├── nginx.conf                      # Reverse proxy config
├── .gitignore
├── .github/
│   └── workflows/
│       └── ci-cd.yml               # ✅ Full CI/CD pipeline (build → test → deploy)
├── terraform/
│   └── main.tf                     # ✅ Infrastructure as Code (Terraform)
├── ansible/
│   └── deploy.yml                  # ✅ Automated deployment (Ansible)
└── templates/
    ├── index.html                  # Home / Dashboard
    ├── detail.html                 # Plant detail page
    └── add.html                    # Add new plant form
```

---

## ✅ DevOps Rubric Coverage

| Rubric Metric | How It's Covered | Score Target |
|---|---|---|
| **Version Control & Collaboration** | Git branching (`main`, `develop`), PR workflow, meaningful commits | Excellent |
| **CI/CD Pipeline** | GitHub Actions: Build → Test → Docker Build → Deploy (3 full stages) | Excellent |
| **Containerization & Deployment** | Dockerfile + Docker Compose with 2 replicas + Nginx reverse proxy | Excellent |
| **Infrastructure as Code (IaC)** | Terraform (`terraform/main.tf`) + Ansible (`ansible/deploy.yml`) | Excellent |

---

## 🚀 How to Run

### Option 1 — Plain Python
```bash
pip install -r requirements.txt
python app.py
```
Visit: **http://localhost:5000**

### Option 2 — Docker
```bash
docker build -t greenpulse .
docker run -p 5000:5000 greenpulse
```

### Option 3 — Docker Compose (with Nginx)
```bash
docker compose up --build
```
Visit: **http://localhost** (via Nginx reverse proxy)

### Option 4 — Ansible (automated deploy)
```bash
cd ansible
ansible-playbook deploy.yml
```

### Option 5 — Terraform (IaC)
```bash
cd terraform
terraform init
terraform apply
```

---

## 🌿 App Features

- 📊 **Dashboard** — View all your plants with health scores
- 💧 **Water Tracking** — Log when each plant was watered
- ➕ **Add Plants** — Add new plants with name, type, emoji, notes
- 🌱 **Sustainability Tips** — Eco-friendly gardening tips
- 🔍 **Health API** — `/health` endpoint for container monitoring

---

## 🔀 Git Workflow (for Viva)

```bash
# Initialize
git init
git add .
git commit -m "feat: initial GreenPulse project"

# Feature branch workflow
git checkout -b feature/add-plant-form
git add templates/add.html app.py
git commit -m "feat: add plant creation form"
git checkout main
git merge feature/add-plant-form
git push origin main
```

---

## 💬 What to Say in Viva

- *"GreenPulse is a plant tracker built with Flask, containerized using Docker, and deployed via GitHub Actions."*
- *"The CI/CD pipeline has three stages: build & test, Docker build, and deploy — all automated on every push."*
- *"Docker Compose runs two replicas of the app behind an Nginx reverse proxy — this is orchestration."*
- *"Terraform provisions the Docker container as Infrastructure as Code — fully reproducible."*
- *"Ansible automates the full deployment — install, build, and run — without manual steps."*

---

Built with ❤️ as a DevOps learning project.
