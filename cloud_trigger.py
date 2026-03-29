import subprocess

def trigger_gcp_instance():
    try:
        print("🚀 Creating GCP VM instance...")

        subprocess.run([
            "gcloud", "compute", "instances", "create", "auto-scale-vm",
            "--zone=us-central1-a",
            "--machine-type=e2-micro",
            "--image-family=debian-11",
            "--image-project=debian-cloud"
        ], check=True)

        print("✅ GCP instance created successfully!")

    except subprocess.CalledProcessError as e:
        print("❌ Failed to create GCP instance")
        print(e)
