#!groovy
pipeline {
    agent any
    options {
        // Timeout counter starts AFTER agent is allocated
        timeout(time: 1, unit: 'SECONDS')
    }
    stages {
        stage('Example') {
            steps {
                echo 'Hello World'
            }
        }
    }
}

/* node {
    stage('Preparation') {
        deleteDir()
        checkout scm
        //sh 'git submodule update --init --recursive'
        def workspace = pwd()
        sh "pip3 install virtualenv"
        sh '''if [ ! -d "venv" ]; then
            virtualenv venv
        fi'''
        sh ". venv/bin/activate"
        sh "pip install django"
        sh "pip install -r requirements.txt"
        sh "python manage.py makemigrations"
        sh "python manage.py migrate"
    }

    stage('Test') {
        sh "python manage.py test"
    }

    stage('Staging deploy') {
        ansiColor('xterm') {
            ansiblePlaybook(
                    colorized: true,
                    inventory: 'ci/ansible/hosts',
                    playbook: 'ci/ansible/deploy-app-staging.yml',
                    sudoUser: null
            )
        }
    }

}

stage('Production deploy approval') {
    timeout(time: 5, unit: 'DAYS') {
        def deploy = input(id: 'userInput', message: 'Deploy to production?')
    }
}

node {
    stage('Production deploy') {
        ansiColor('xterm') {
            ansiblePlaybook(
                    colorized: true,
                    inventory: 'ci/ansible/hosts',
                    playbook: 'ci/ansible/deploy-app-production.yml',
                    sudoUser: null
            )
        }
    }
} */