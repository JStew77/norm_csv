SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
ssh-keygen -f "${SCRIPT_DIR}/ot2_ssh_key"
mv ot2_ssh_key ~
chmod 600 ~/ot2_ssh_key
# key_path=$(cat "${SCRIPT_DIR}/ot2_ssh_key.pub")
echo $1
curl -H 'Content-Type: application/json' -d "{\"key\":\"$(cat "${SCRIPT_DIR}/ot2_ssh_key.pub")\"}" $1:31950/server/ssh_keys