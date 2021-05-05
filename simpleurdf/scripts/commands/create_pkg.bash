#!/usr/bin/env bash
set -e
. "$BAGCLI_WORKDIR/common"

cli_help_deploy() {
  echo "
Command: deploy
Usage: 
  deploy project_name"
  exit 1
}

[ ! -n "$1" ] && cli_help_deploy

export BAGCLI_PROJECT_NAME=$1

MODEL_NAME = &1

$NAME_PKG_CREATED = ${MODEL_NAME}_description

ros2 pkg create --build-type ament_python $NAME_PKG_CREATED
mv $SIMPLEURDF_FOLDER_INSTALLED/demo.launch.py demo.launch.py
mkdir $NAME_PKG_CREATED/launch
sed -i "s/<package_name>/$NAME_PKG_CREATED/g" $NAME_PKG_CREATED/launch/demo.launch.py
sed -i "s/<model_name/$MODEL_NAME/g" demo.launch.py
sed -i "s/<model_name>/$MODEL_NAME/g" state_publisher.py


cli_log "Deployment BEGIN"

cli_log "ENV variables"
env | grep "BAGCLI_*"

cli_log "Executing helm upgrade --install ..."
# Example
# helm upgrade --install \
#   --wait \
#   --values $BAGCLI_PROJECTS_PATH/$BAGCLI_PROJECT_NAME/values.yaml \
#   --namespace $BAGCLI_K8S_NAMESPACE $BAGCLI_PROJECT_NAME $BAGCLI_REPO_PATH

cli_log "Deployment END"