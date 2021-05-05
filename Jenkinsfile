pipeline{
    agent { dockerfile true }

    stages{
        stage("Build"){
            steps{
            echo "========installing packages========"
                poetry install
            }
        }
        stage('Test'){
            steps {
                echo "========executing tests========"
                pytest
            } 
            post{
                always{
                    echo "========always========"
                }
                success{
                    echo "========A executed successfully========"
                }
                failure{
                    echo "========A execution failed========"
                }
            }
        }
        stage("Deploy"){
            steps{
                echo "========executing B========"
            }
        }
    }
    post{
        always{
            echo "========always========"
        }
        success{
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}
