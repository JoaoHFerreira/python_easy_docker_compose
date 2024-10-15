# Easy Python Docker - Quick Development Setup

Follow these steps to quickly set up a Python development environment using Docker.

1. **Navigate to the Docker directory:**
   ```bash
   cd docker
   ```

2. **Optional: Edit the Dockerfile**
   If needed, modify the `Dockerfile` located at:
   ```
   python_easy_docker_compose/docker/Dockerfile
   ```

3. **Add your required libraries:**
   Specify any additional Python libraries in:
   ```
   python_easy_docker_compose/docker/requirements
   ```

4. **Build the Docker image:**
   ```bash
   docker-compose build python-service
   ```

5. **Run the container:**
   Launch the container with:
   ```bash
   docker-compose run --rm -it python-service bash
   ```
