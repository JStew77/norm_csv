curl -H 'Content-Type: application/json' -d "{\"key\":\"$(cat $1)\"}" $2:31950/server/ssh_keys