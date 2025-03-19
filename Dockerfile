# Step 1: Use the correct base image
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the application code into the container
COPY . /app

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose the correct port (Flask default is 5000)
EXPOSE 5000

# Step 6: Set the correct entry point to run the app
CMD ["python", "app.py"]
