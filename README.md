# Midterm Lab Exam - Development Lab

- **Name:** Nauman Ali Murad  
- **Registration Number:** 2022479  

---

## Overview
This project is part of the midterm lab exam for the Development Lab course. The goal of this project is to develop a Flask web application, add new features, fix issues, containerize it, deploy it using Kubernetes, and set up monitoring using Prometheus.

## **1. Project Setup and Development**
### **Initial Setup**
- Created a Flask web application.
- Integrated a PostgreSQL database.
- Developed models, routes, and views.
- Used Docker for containerization.
- Deployed using Kubernetes.
- Set up Prometheus for monitoring.

## **2. Creating New Features**

### **Feature 1: Add Laptop Field to Web App**
- **(i)** Modified the frontend to include an additional field for entering laptop details.
- **(ii)** Updated the backend Flask application to handle the new field and store it in the database.
- **(iii)** Modified the database schema to add a new column in the table for laptop details.

### **Feature 2: Improve Validation**
- **(i)** Added client-side validation to ensure the email field contains a valid email address.
- **(ii)** Added server-side validation to ensure the phone number is numeric and exactly 10 digits long.
- **(iii)** Improved UI styling.

## **3. Analyzing Issues and Fixing Scripts**

### **(a) Fixing `build.sh` Script**
- The provided `build.sh` script was incomplete or contained errors.
- Fixed the script to correctly install dependencies from `requirements.txt`.

### **(b) Fixing `test.sh` Script**
- The `test.sh` script was also incomplete or contained errors.
- Updated it to properly run unit tests and integration tests.

## **4. Containerization of the Application**

### **(a) Updating the Dockerfile**
- **(i)** Used the correct base image for Flask.
- **(ii)** Copied the application code into the container.
- **(iii)** Installed all dependencies.
- **(iv)** Exposed the correct port (5000 for Flask).
- **(v)** Set the correct entry point/command to run the application.

### **(b) Building and Pushing the Container Image**
- Built the Docker image with the correct configuration.
- Tagged the container image with the student ID: `2022479`
- Pushed the image to a container registry.

## **5. Kubernetes Deployment**

### **(a) Creating Kubernetes Files**
- **(i)** Created a Kubernetes deployment file for the web app (`deployment.yaml`).
- **(ii)** Created a Kubernetes deployment file for the database (`postgres-deployment.yaml`).
- **(iii)** Created Kubernetes service files for the web app and database (`service.yaml`).

### **(b) Deploying the Application and Database**
- Applied the Kubernetes configurations to deploy the app and database.
- Ensured that the web application and PostgreSQL database were running inside the Kubernetes cluster.

## **6. Evaluating the Application and Setting Up Monitoring**

### **(a) Setting Up Monitoring**
- **(i)** Created a configuration file for Prometheus (`prometheus.yml`).
- **(ii)** Deployed Prometheus using the configuration file.

### **(b) Verifying Prometheus Configuration**
- Deployed Prometheus using Kubernetes.
- Verified the deployment status using:
  ```sh
  kubectl get pods
  kubectl get services
  ```
- Checked Prometheus dashboard at `http://<minikube-ip>:30090`

---

## **Conclusion**
This project covered full-stack development, including:
- Web application development with Flask.
- Database integration with PostgreSQL.
- Dockerization and container management.
- Kubernetes deployment.
- Application monitoring with Prometheus.

With these steps, the application was successfully developed, deployed, and monitored. 🚀

