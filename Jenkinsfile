pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                sh 'docker build -t fastapi-cicd .'
            }
        }
        stage('check images'){
            steps{
                sh 'docker images'
            }
        }

        stage('run container'){
            steps{
                sh 'docker run -d -p 80:80 fastapi-cicd'
            }
        }
       
    }
}