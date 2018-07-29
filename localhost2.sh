cd $VIRTUAL_ENV

cd src
ls
cd hydra_agent
python3 setup.py install
cd hydra_redis
python3 querying_mechanism.py
