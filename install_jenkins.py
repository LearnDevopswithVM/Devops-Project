import subprocess

def install_jenkins():
    try:
        print("Updating system packages...")
        subprocess.run(["sudo", "apt-get", "update", "-y"], check=True)
        
        print("Installing Java (required for Jenkins)...")
        subprocess.run(["sudo", "apt-get", "install", "openjdk-11-jdk", "-y"], check=True)

        print("Adding Jenkins repository key...")
        subprocess.run(["wget", "-q", "-O", "-", "https://pkg.jenkins.io/debian-stable/jenkins.io.key"], check=True)
        subprocess.run(["sudo", "apt-key", "add", "-"], check=True)

        print("Adding Jenkins repository...")
        subprocess.run(["sudo", "sh", "-c", "echo 'deb https://pkg.jenkins.io/debian-stable binary/' > /etc/apt/sources.list.d/jenkins.list"], check=True)

        print("Updating package list after adding Jenkins repository...")
        subprocess.run(["sudo", "apt-get", "update", "-y"], check=True)

        print("Installing Jenkins...")
        subprocess.run(["sudo", "apt-get", "install", "jenkins", "-y"], check=True)

        print("Starting Jenkins service...")
        subprocess.run(["sudo", "systemctl", "start", "jenkins"], check=True)
        subprocess.run(["sudo", "systemctl", "enable", "jenkins"], check=True)

        print("Jenkins installed and started successfully!")
        print("You can access Jenkins at: http://<your-server-ip>:8080")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    install_jenkins()
