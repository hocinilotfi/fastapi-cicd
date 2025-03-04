pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                sh 'docker build -t fastapi-cicd .'
            }
        }
        stage('Deploy'){
            steps{
                sh 'docker images'
            }
        }
       
    }
}