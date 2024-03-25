pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate'
                bat 'pip install -r requirements.txt' // Install dependencies if needed
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                // Run your tests here
                bat 'venv\\Scripts\\python test/test_end_2_end.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
            }
        }
    }
}
