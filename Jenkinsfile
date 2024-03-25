pipeline {
    agent any

    environment {
        // Define the Docker image name
        IMAGE_NAME = 'tests'
        TAG = 'latest'
        INFRA_PATH = 'C:\Users\saher\OneDrive\קבצים מצורפים\שולחן העבודה\repos\FinalProjectQaByeondev\infra'
        LOGIC_PATH = 'C:\Users\saher\OneDrive\קבצים מצורפים\שולחן העבודה\repos\FinalProjectQaByeondev\logic'
        TEST_PATH = 'C:\Users\saher\OneDrive\קבצים מצורפים\שולחן העבודה\repos\FinalProjectQaByeondev\test'
        DOCKER_WORKDIR = '/usr/src/tests/FinalProjectQaByeondev'
    }

    stages {
        stage('Debug') {
            steps {
                echo 'Starting parallel execution...'
            }
        }

        stage('Run Tests in Parallel') {
            steps {
                script {
                    parallel(
                        'Chrome Test': {
                            echo 'Running Chrome test...'
                            bat "docker rm -f chrome_test || true"
                            bat "docker run --name chrome_test -e PYTHONPATH=${DOCKER_WORKDIR} -v ${INFRA_PATH}:${DOCKER_WORKDIR}/infra -v ${LOGIC_PATH}:${DOCKER_WORKDIR}/logic -v ${TEST_PATH}:${DOCKER_WORKDIR}/test ${IMAGE_NAME}:${TAG} python ${DOCKER_WORKDIR}/test/test_end_2_end.py --browser chrome"
                        },
                        'Edge Test': {
                            echo 'Running Edge test...'
                            bat "docker rm -f edge_test || true"
                            bat "docker run --name edge_test -e PYTHONPATH=${DOCKER_WORKDIR} -v ${INFRA_PATH}:${DOCKER_WORKDIR}/infra -v ${LOGIC_PATH}:${DOCKER_WORKDIR}/logic -v ${TEST_PATH}:${DOCKER_WORKDIR}/test ${IMAGE_NAME}:${TAG} python ${DOCKER_WORKDIR}/test/test_end_2_end.py --browser edge"
                        },
                        'Firefox Test': {
                            echo 'Running Firefox test...'
                            bat "docker rm -f firefox_test || true"
                            bat "docker run --name firefox_test -e PYTHONPATH=${DOCKER_WORKDIR} -v ${INFRA_PATH}:${DOCKER_WORKDIR}/infra -v ${LOGIC_PATH}:${DOCKER_WORKDIR}/logic -v ${TEST_PATH}:${DOCKER_WORKDIR}/test ${IMAGE_NAME}:${TAG} python ${DOCKER_WORKDIR}/test/test_end_2_end.py --browser firefox"
                        }
                    )
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // bat "docker rmi ${IMAGE_NAME}:${TAG}"
        }
    }
}
