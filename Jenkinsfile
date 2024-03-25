pipeline {
    agent any
    environment {
        // Define the Docker image name

        INFRA_PATH = 'C:\Users\saher\OneDrive\קבצים מצורפים\שולחן העבודה\repos\FinalProjectQaByeondev\infra'
        LOGIC_PATH = 'C:\Users\saher\OneDrive\קבצים מצורפים\שולחן העבודה\repos\FinalProjectQaByeondev\logic'
        TEST_PATH = 'C:\Users\saher\OneDrive\קבצים מצורפים\שולחן העבודה\repos\FinalProjectQaByeondev\test'
    
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