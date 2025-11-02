pipeline {
    agent any

    environment {
        IMAGE_NAME = "hello-flask"
        CONTAINER_NAME = "hello-flask-container"
        PORT = "5001"
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
                echo "Listing containers..."
                docker ps -a

                echo "Stopping and removing containers..."
                docker ps -aq | xargs -r docker rm -f || true

                echo "Removing images..."
                docker images -q | xargs -r docker rmi -f || true
                '''
            }
        }

        stage("Build Docker Image") {
            steps {
                echo "⚙️ Building Docker image..."
                sh '''
                docker build -t ${IMAGE_NAME}:latest .
                '''
            }
        }

        stage("Deploy Container") {
            steps {
                echo "🚀 Deploying container..."
                sh '''
                docker run -d --name ${CONTAINER_NAME} -p ${PORT}:5000 ${IMAGE_NAME}:latest
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Deployment successful! Application is running at http://localhost:${PORT}"
        }
        failure {
            echo "❌ Deployment failed! Check Jenkins logs for details."
        }
    }
}
