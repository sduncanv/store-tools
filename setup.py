import os
import setuptools


def get_environment():

    environment_variables = {}
    environment_filename = ".env"

    if not os.path.exists(environment_filename):
        return environment_filename

    with open(environment_filename, mode="r", encoding="utf-8") as f:

        for line in f:
            key, _, value = line.strip().partition('=')
            if key and value:
                environment_variables[key] = value

    return environment_variables


def get_requirements(filename="requirements.txt", write=False):

    # Defining placeholders
    environment_keys = ['USERNAME', 'PASSWORD', 'TOKEN']
    requirements_lock = 'requirements-lock.txt'

    if not os.path.exists(requirements_lock):
        return []

    # Getting environment variables
    environment_variables = get_environment()
    user = environment_variables.get('REPO_USER')
    password = environment_variables.get('REPO_PASS')
    token = environment_variables.get('TOKEN')

    requirements = []

    with open(requirements_lock, mode="r", encoding="utf-8") as req_lock:
        lines = req_lock.readlines()

    with open(filename, 'w' if write else 'r') as f:

        for line in lines:
            content = line.strip()

            for variable in environment_keys:
                if variable in content:
                    content = content.replace('USERNAME', user).replace(
                        'PASSWORD', password).replace('TOKEN', token)

            if not write:
                if "#egg=" in content:
                    package, egg = content.split('#egg=')
                    content = f"{egg.strip()} @ {package.strip()}"

            requirements.append(content)

            if write:
                f.write(content + '\n')

    return requirements


if __name__ == "__main__":

    requirements = get_requirements()

    setuptools.setup(
        name="store-tools",
        version="0.0.1",
        author="Samuel Duncan",
        author_email="srduncanv1217@gmail.com",
        url="https://github.com/sduncanv/store-tools.git",
        project_urls={
            "Bug Tracker": "https://github.com/sduncanv/store-tools.git",
        },
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: Other/Proprietary License",
            "Operating System :: OS Independent",
        ],
        package_dir={
            'Tools.Classes': 'Classes',
            'Tools.Models': 'Models',
            'Tools.Database': 'Database',
            'Tools.Utils': 'Utils',
        },
        packages=[
            'Tools.Classes', 'Tools.Models', 'Tools.Database', 'Tools.Utils'
        ],
        python_requires=">=3.8",
        install_requires=requirements
    )
