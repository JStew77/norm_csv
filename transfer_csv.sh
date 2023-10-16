SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
ROBOT_IP= $2
OT2_PATH= "/data/user_storage/"
scp -i $3 "${SCRIPT_DIR}/$1" "root@${ROBOT_IP}:${OT2_PATH}"


