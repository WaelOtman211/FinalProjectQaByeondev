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
        stage('Non-Functional Test') {
            steps {
                echo 'Testing..'
                // Run your tests here
                script {
                    try {
                        bat 'python -k test_run_grid_parallel_incorrect_location'

                    } catch (Exception e) {
                        echo "Test failed, but the build continues."
                    }
                }
            }
        }
        stage('Test End To End Test') {
            steps {
                echo 'Testing..'
                // Run your tests here
                script {
                    try {
                        bat 'python -k test_run_grid_parallel_add_book_to_specific_list_and_note'
                    } catch (Exception e) {
                        echo "Test failed, but the build continues."
                    }
                }
            }
        }
        stage('API Tests') {
            steps {
                echo 'Testing..'
                // Run your tests here
                script {
                    try {
                        bat 'python test/test_api/test_book.py'
                    } catch (Exception e) {
                        echo "Test failed, but the build continues."
                    }
                }
            }
        }
        stage('Run API Tests with Pytest') {
            steps {
                echo 'Running API Tests with Pytest..'
                script {
                    try {
                        // Run pytest with pytest-html plugin to generate HTML report
                        bat "C:/AutomationWithTsahi/pythonProjectBeyondev/venv/Scripts/pytest.exe test/test_api/test_book.py --html=test-reports/reportAPI.html"
                    } catch (Exception e) {
                        echo "Tests failed, but the build continues."
                    }
                }
            }
        }
        stage('Run Non-Functional Tests with Pytest') {
            steps {
                echo 'Running API Tests with Pytest..'
                script {
                    try {
                        // Run pytest with pytest-html plugin to generate HTML report
                        bat "C:/AutomationWithTsahi/pythonProjectBeyondev/venv/Scripts/pytest.exe -k test_run_grid_parallel_incorrect_location --html=test-reports/reportEndToEnd.html"
                    } catch (Exception e) {
                        echo "Tests failed, but the build continues."
                    }
                }
            }
        }
        stage('Run End To End Tests with Pytest') {
            steps {
                echo 'Running API Tests with Pytest..'
                script {
                    try {
                        // Run pytest with pytest-html plugin to generate HTML report
                        bat "C:/AutomationWithTsahi/pythonProjectBeyondev/venv/Scripts/pytest.exe -k test_run_grid_parallel_add_book_to_specific_list_and_note --html=test-reports/reportNonFunctional.html"
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
