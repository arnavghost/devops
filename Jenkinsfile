pipeline {
    agent any

    environment {
        IMAGE_NAME = "hello-flask"
        CONTAINER_NAME = "hello-flask-container"
        PORT = "5000"
    }

    stages {
        stage("Clone Code") {
            steps {
                echo "🔁 Cloning the code from GitHub..."
                git branch: "main", url: "https://github.com/arnavghost/devops.git"
            }
        }

        stage("Clean Old Containers & Images") {
            steps {
                echo "🧹 Removing old containers and images..."
                sh '''
                if docker ps -q --filter "name=${CONTAINER_NAME}" | grep -q .; then
                    docker stop ${CONTAINER_NAME}
                    docker rm ${CONTAINER_NAME}
                fi
                if docker images -q ${IMAGE_NAME} | grep -q .; then
                    docker rmi -f ${IMAGE_NAME}
                fi
                '''
            }
        }

        stage("Build Docker Image") {
            steps {
                echo "⚙️ Building Docker image..."
                sh "docker build -t ${IMAGE_NAME}:latest ."
            }
        }

        stage("Deploy Container") {
            steps {
                echo "🚀 Deploying container..."
                sh "docker run -d --name ${CONTAINER_NAME} -p ${PORT}:5000 ${IMAGE_NAME}:latest"
            }
        }
    }

    post {
        success {
            echo "✅ Deployment successful! Flask app running at http://localhost:${PORT}"
        }
        failure {
            echo "❌ Deployment failed! Check Jenkins logs for details."
        }
    }
}
