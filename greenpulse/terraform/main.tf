# ================================================================
# GreenPulse — Infrastructure as Code (Terraform)
# Provisions a local Docker container using Terraform
# ================================================================

terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

# ── Pull or use local image ───────────────────────────────────────
resource "docker_image" "greenpulse" {
  name         = "greenpulse:latest"
  keep_locally = true
}

# ── Run the application container ────────────────────────────────
resource "docker_container" "greenpulse_app" {
  name  = "greenpulse-app"
  image = docker_image.greenpulse.image_id

  ports {
    internal = 5000
    external = 5000
  }

  env = [
    "FLASK_ENV=production",
    "APP_NAME=GreenPulse"
  ]

  restart = "unless-stopped"

  healthcheck {
    test     = ["CMD", "python", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')"]
    interval = "30s"
    timeout  = "5s"
    retries  = 3
  }

  labels {
    label = "app"
    value = "greenpulse"
  }
}

# ── Outputs ───────────────────────────────────────────────────────
output "app_url" {
  value       = "http://localhost:5000"
  description = "GreenPulse application URL"
}

output "container_id" {
  value       = docker_container.greenpulse_app.id
  description = "Running container ID"
}
