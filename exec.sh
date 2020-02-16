docker container ls >> exec_temp_output
docker container exec -it `cut -d " " -f 1 exec_temp_output | tail -n 1` bash
