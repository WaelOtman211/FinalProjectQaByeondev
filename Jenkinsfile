pipeline {
    agent any
    environment {
        PYTHONPATH = "C:/Users/saher/OneDrive/קבצים מצורפים/שולחן העבודה/repos/FinalProjectQaByeondev"
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                bat 'pip install -r requirements.txt' // Install dependencies if needed
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                // Run your tests here
                bat 'python test/test_end_2_end.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
            }
        }
    }
}
