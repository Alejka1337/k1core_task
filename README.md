# K1CORE LTD Test Task

## How to start project
### 1️⃣ Preparing the environment

#### **Clone the repository:**

```shell
git clone https://github.com/Alejka1337/k1core_task.git 
```

```shell
cd k1core_task
```

### 2️⃣ Create and configure the .env file:

#### **There is already an .env.example in the project. Rename it to .env:**

```shell
cp .env.example .env
```

#### **Then open .env and specify the required environment variables (e.g., database credentials and message broker access details).**


### 3️⃣ Create static directory

```shell
make static
```


### 4️⃣ Launching the Project with Docker

#### **The project uses Makefile for convenient container management. It can be started with a single command:**

```shell
make up
```
#### **This command automatically:**

- **Start the application, database, and message broker containers.**
- **Apply database migrations.**
- **Launch the FastAPI server.**
- **Start the Celery worker and Celery Beat.**

### ️5️⃣ Stopping containers

#### **To stop the project, execute:**

```shell
make down
```
