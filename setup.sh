SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
ssh-keygen -f $SCRIPT_DIR/ot2_ssh_key
curl -H 'Content-Type: application/json' -d "{\"key\":\"$(cat $SCRIPT_DIR/ot2_ssh_key.pub)\"}" $2:31950/server/ssh_keys