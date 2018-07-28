from astrodemo.settings import DB_URL,HYDRUS_SERVER_URL,PORT,API_NAME
from sqlalchemy import create_engine
from hydrus.data.db_models import Base
from sqlalchemy .orm import sessionmaker
from hydrus.parser.openapi_parser import parse
from hydrus.data import doc_parse
from hydrus.app import app_factory
from gevent.pywsgi import WSGIServer
from hydrus.utils import (set_session, set_doc, set_hydrus_server_url,
                          set_token, set_api_name, set_authentication)
import yaml

if __name__ == "__main__":
    with open("./astrodemo.yaml", 'r') as stream:
        try:
            documentation = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    api_doc = parse(documentation)
    # print(api_doc)
    engine = create_engine(DB_URL)
    session = sessionmaker(bind=engine)()

    print("Droping database if exist")

    Base.metadata.drop_all(engine)
    print("Creating models....")
    Base.metadata.create_all(engine)
    print("Done")
    classes = doc_parse.get_classes(api_doc.generate())

    properties = doc_parse.get_all_properties(classes)

    doc_parse.insert_classes(classes, session)
    doc_parse.insert_properties(properties, session)

    session = sessionmaker(bind=engine)()
    app = app_factory(API_NAME)
    with set_doc(app, api_doc):
        with set_hydrus_server_url(app, HYDRUS_SERVER_URL):
            with set_session(app, session):
                http_server = WSGIServer(('', PORT), app)
                http_server.serve_forever()


