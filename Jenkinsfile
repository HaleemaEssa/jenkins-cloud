pipeline {
    agent { label "aws" }
    environment {
        DOCKERHUB_CREDENTIALS=credentials('haleema-dockerhub')
    }
    stages {
        stage('GitClone') {
            steps {
                git branch: 'main', url: 'https://github.com/HaleemaEssa/first_jenkins_project.git'
            }
        }
    stage('Createdockerimage on cloud') {
            steps {
                sh 'sudo docker build -t haleema/docker-cloud:latest .'
            }
        }     
    stage('Login to Dockerhub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        } 
     stage('pushimage to Dockerhub') {
            steps {
                sh 'sudo docker push haleema/docker-cloud:latest'
            }
        }  
        
    stage('runimage') {
         
            steps {
                sh 'sudo docker run --privileged -t haleema/docker-cloud'
            }
         }    
    
   
         
    
    }
    post {
        always {
            sh 'sudo docker logout'
        }
    }
}
