pipeline {
    agent any

    environment {
        SONARQUBE_SCANNER_HOME = tool 'SonarQubeScanner'
        SONAR_TOKEN = credentials('sonar-token')
    }

    stages {
        stage('Setup Python') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    export PYTHONPATH=.
                    mkdir -p reports
                    pytest tests/test_app.py --html=reports/report.html --self-contained-html
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    python3 tests/test_selenium.py
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQubeServer') {
                    sh '''
                        . venv/bin/activate
                        sonar-scanner -Dproject.settings=sonar-project.properties
                    '''
                }
            }
        }
    }
}
