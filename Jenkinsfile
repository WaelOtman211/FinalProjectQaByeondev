pipeline {
    agent any
    environment {

        INFRA_PATH = 'C:/Users/odehm/Desktop/repos/petsore/infra'
        LOGIC_PATH = 'C:/Users/odehm/Desktop/repos/petsore/logic'
        TEST_PATH = 'C:/Users/odehm/Desktop/repos/petsore/test'

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