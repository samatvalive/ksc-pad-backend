#!/usr/bin/env python.
import subprocess
import os
import shutil
# config


# Production
productId= 'lucid-dynamo-310207' 
dockerImageName = 'gatherdao-prod'
region = 'europe-north1'
concurrency = '--concurrency=4'
cpu = '--cpu=1 '
memory = '--memory=512Mi'
minInstance = '--min-instances=4'
maxInstance = '--max-instances=50'
timeout = '--timeout=60'
rateLimit = 'RATELIMIT_ENABLE=False'
vpcConnector = '--vpc-connector=gd-cloud-run-cloud-sql'

dbConfig = 'ENVIRONMENT=production,DATABASE_HOST=172.25.61.2,DATABASE_NAME=gatherdao-prod-db,DATABASE_USER=db-user,DATABASE_PASSWORD=k1b0HuE8DAq1nOaB,DATABASE_PORT=5432'

# Local production

# productId = 'psychic-raceway-307117'
# dockerImageName = 'gatherdao'
# region = 'us-central1'
# concurrency = '--concurrency=4'
# cpu = '--cpu=1 '
# memory = '--memory=512Mi'
# minInstance = '--min-instances=1'
# maxInstance = '--max-instances=10'
# timeout = '--timeout=60'
# rateLimit = 'RATELIMIT_ENABLE=False'
# vpcConnector = '--vpc-connector=default-vpc-connector'
# dbConfig = 'DATABASE_HOST=172.16.128.3,DATABASE_NAME=testdb,DATABASE_USER=postgres,DATABASE_PASSWORD=654321,DATABASE_PORT=5432'


evnVars = f'--set-env-vars="{dbConfig},{rateLimit}"'


def switch():
    print('''Press 1 to Update build folder
    \nPress 2 build Docker Image & run
    \nPress 3 to Submit files to gcp & deploy
    \nPress 4 to Resolve Docker permission issue
    \nPress 5 to Kill running port
    ''')

    option = int(input("Your option : "))

    def updateBuildFolder():
        src_dir = "/home/hopevik/gatherdao/GatherDAOFrontend/build"
        dest_dir = "/home/hopevik/gatherdao/GatherDAODapp"
        cmd = 'rsync -a "%s" "%s"' % (src_dir, dest_dir)
        status = subprocess.call(cmd, shell=True)
        status = subprocess.call(cmd, shell=True)
        print("Task executed = ", status)

    def dockerBuildAndRun():
        status = subprocess.call(
            'docker build -t "%s":latest .' % (dockerImageName), shell=True)
        status = subprocess.call(
            'docker run --rm -it -p 8080:8080 "%s":latest' % (dockerImageName), shell=True)
        print("Task executed = ", status)

    def killPort():
        portNumber = input("Specify port no : ")
        if portNumber == '':
            portNumber = 5432
        cmd = 'sudo kill -9 $(sudo lsof -t -i:"%s")' % (portNumber)
        out = subprocess.run(cmd, shell=True, check=True)
        print("Killed : ", out)

    def fixDockerIssue():
        out = subprocess.run(
            'sudo chmod 666 /var/run/docker.sock', shell=True, check=True)
        print("Fixed : ", out)

    def submitFilesAndDeployOnGCP():
        # status = subprocess.call(
        #     'gcloud builds submit --tag gcr.io/"%s"/"%s":latest' % (productId, dockerImageName), shell=True)
        # print("Files Submitted = ", status)
        deployCmd = f'gcloud run deploy {dockerImageName} --image gcr.io/{productId}/{dockerImageName}:latest --platform=managed --port=8080 --region={region} --allow-unauthenticated {vpcConnector} {concurrency} {cpu} {memory} {minInstance} {maxInstance} {timeout} {evnVars}'
        status = subprocess.call(deployCmd, shell=True)
        print("Deployed = ", status)

# If user enters invalid option then this method will be called
    def updateEnvVariables():
        # --vpc-connector='gd-cloud-run-cloud-sql'
        print('Test')

    def default():
        print("Invalid Choice, try again")
        switch()

# Dictionary Mapping
    dict = {
        1: updateBuildFolder,
        2: dockerBuildAndRun,
        3: submitFilesAndDeployOnGCP,
        4: fixDockerIssue,
        5: killPort,
        6: updateEnvVariables,
    }
    # get() method returns the function matching the argument
    dict.get(option, default)()


switch()  # Call switch() method
