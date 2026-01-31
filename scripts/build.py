import os
import datetime

print("===== Python Build Script Started =====")

# Show current date and time
now = datetime.datetime.now()
print("Build Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

# Project info
project_name = "Calculator CI Project"
print("Project:", project_name)

# Path to target directory
target_dir = "target"

# Check if target directory exists
if os.path.exists(target_dir):
    print("Target directory found.")

    # Look for jar file
    files = os.listdir(target_dir)
    jar_files = [f for f in files if f.endswith(".jar")]

    if jar_files:
        print("JAR file generated successfully:")
        for jar in jar_files:
            print(" -", jar)
        print("Build verification: SUCCESS")
    else:
        print("No JAR file found in target directory.")
        print("Build verification: FAILED")
else:
    print("Target directory not found.")
    print("Build verification: FAILED")

print("===== Python Build Script Finished =====")
