pipeline {
    agent any
    environment {
        PYTHONPATH = "C:/Users/saher/OneDrive/קבצים מצורפים/שולחן העבודה/repos/FinalProjectQaByeondev"
        TEST_REPORTS='test-reports'
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
        stage('Run API Tests with Pytest') {
            steps {
                script {
                    try {
                        bat 'call venv/Scripts/python.exe -m pytest test/test_end_2_end.py --html=test-reports/report.html --self-contained-html'
                    } catch (Exception e) {
                        echo "Tests failed, but the build continues."
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
                // Add deployment steps here if needed
            }
        }
    }
}
