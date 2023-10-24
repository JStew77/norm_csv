SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
ROBOT_IP=$2
OT2_PATH="/data/user_storage/"
# scp -i $SCRIPT_DIR/ot2_ssh_key $1 "root@${ROBOT_IP}:${OT2_PATH}"
scp -i ~/ot2_ssh_key $1 "root@${ROBOT_IP}:${OT2_PATH}"


