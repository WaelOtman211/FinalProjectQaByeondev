pipeline {
    agent any
    environment {
        PYTHONPATH = "C:/Users/saher/OneDrive/קבצים מצורפים/שולחן העבודה/repos/FinalProjectQaByeondev"
        TEST_REPORTS='test-reports'
        PASSWORD = credentials('JIRA_TOKEN')
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
                echo 'Running API Tests with Pytest..'
                script {
                    try {
                        // Run pytest with pytest-html plugin to generate HTML report
                        bat "C:/AutomationWithTsahi/pythonProjectBeyondev/venv/Scripts/pytest.exe test/test_end_2_end.py --html=test-reports/report.html"
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
