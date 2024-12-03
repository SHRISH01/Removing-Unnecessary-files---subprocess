import subprocess

def remove_packages(packages):
    """Remove a list of packages using pip."""
    for package in packages:
        try:
            print(f"Removing {package}...")
            subprocess.check_call(["pip", "uninstall", "-y", package])
        except subprocess.CalledProcessError:
            print(f"Failed to remove {package}.")

# List of packages to be removed
unwanted_packages = [
    # List of unwanted packages
]

# Remove the unwanted packages
remove_packages(unwanted_packages)
