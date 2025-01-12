import subprocess

def install_ansible():
    try:
        print("Updating system packages...")
        subprocess.run(["sudo", "apt-get", "update", "-y"], check=True)

        print("Installing Ansible dependencies...")
        subprocess.run(["sudo", "apt-get", "install", "software-properties-common", "-y"], check=True)

        print("Adding Ansible PPA repository...")
        subprocess.run(["sudo", "add-apt-repository", "--yes", "--update", "ppa:ansible/ansible"], check=True)

        print("Installing Ansible...")
        subprocess.run(["sudo", "apt-get", "install", "ansible", "-y"], check=True)

        print("Ansible installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    install_ansible()
