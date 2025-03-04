pipeline {
    agent any
    stages {
        stage('Cleanup Previous Container') {
            steps {
                sh '''
                docker ps -q --filter "name=fastapi-cicd" | grep -q . && docker stop fastapi-cicd && docker rm fastapi-cicd || echo "No existing container found"
                '''
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t fastapi-cicd .'
            }
        }
        stage('Run Container') {
            steps {
                sh 'docker run -d --network fastapi-net -p 8000:80 --name fastapi-cicd fastapi-cicd'
            }
        }
    }
}
